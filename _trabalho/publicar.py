"""Conferir e publicar o site IHFC em 1 comando (ferramenta para modelo menor, 13/11/2026).
  python _trabalho/publicar.py conferir                 só confere (sai com erro se algo não bate)
  python _trabalho/publicar.py publicar "msg" arq1 arq2  confere, commita SÓ esses arquivos, push e espera ficar no ar
Rodar de dentro de _clinica/site-ihfc. Leia _trabalho/LEIA-ME-publicar.md."""
import re, os, sys, json, glob, time, subprocess, hashlib, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
# páginas que DEVEM ter noindex (prévias, cópias e páginas só de anúncio); o resto NÃO pode ter
NOINDEX_OK = {"novo.html", "v5.html", "contato-jaiane-previa.html", "equipe-previa.html"} | set(glob.glob("lp-*.html"))
SEM_ZAP_OK = {"links.html", "privacidade.html"}
PROIBIDO_NO_GIT = [r"^_aprovados/", r"pedido-recepcao", r"\bpaciente", r"\.(heic|raw)$"]


def conferir():
    erros = []
    for p in sorted(glob.glob("*.html")):
        h = open(p, encoding="utf-8").read()
        tem_noindex = bool(re.search(r'<meta name="robots" content="noindex', h))
        if tem_noindex and p not in NOINDEX_OK:
            erros.append(f"{p}: tem noindex e não é prévia/anúncio (some do Google)")
        if not re.search(r"<title>.+?</title>", h, re.S):
            erros.append(f"{p}: sem <title>")
        if 'name="viewport"' not in h:
            erros.append(f"{p}: sem viewport (quebra no celular)")
        if p not in SEM_ZAP_OK and 'class="zap' not in h:
            erros.append(f"{p}: sem botão fixo do WhatsApp")
        for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                json.loads(b)
            except Exception as e:
                erros.append(f"{p}: JSON-LD inválido ({e})")
        for i in re.findall(r"<img[^>]*>", h):
            if "alt=" not in i:
                erros.append(f"{p}: imagem sem alt: {i[:60]}")
        for u in re.findall(r'(?:href|src)="([^"#:?]+)', h):
            if not u.startswith(("http", "mailto", "tel", "//", "data")) and not os.path.exists(u.split("#")[0]):
                erros.append(f"{p}: link quebrado -> {u}")
    sm = open("sitemap.xml", encoding="utf-8").read() if os.path.exists("sitemap.xml") else ""
    for u in re.findall(r"<loc>https://www\.ihfc\.com\.br/([^<]*)</loc>", sm):
        if u and not os.path.exists(u):
            erros.append(f"sitemap aponta para arquivo inexistente: {u}")
        if u in NOINDEX_OK:
            erros.append(f"sitemap lista página noindex: {u}")
    r = subprocess.run([sys.executable, "_trabalho/checar_afirmacoes.py"], capture_output=True, text=True)
    if r.returncode:
        erros.append("checar_afirmacoes: " + r.stdout.strip()[-400:])
    for f in subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split("\n"):
        if any(re.search(x, f, re.I) for x in PROIBIDO_NO_GIT):
            erros.append(f"arquivo proibido no repositório PÚBLICO: {f}")
    return erros


def git(*a):
    for tentativa in range(6):  # a republicação do mestre (tarefa de 10 em 10 min) às vezes segura o index.lock
        r = subprocess.run(["git", *a], capture_output=True, text=True, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
        if "index.lock" not in r.stderr:
            return r
        time.sleep(10)
    return r


def assinatura(b):
    """o Git do Windows guarda CRLF no disco e LF no GitHub: compara sem o \\r"""
    return hashlib.sha1(b.replace(b"\r\n", b"\n")).hexdigest()


def no_ar(arq, esperado, limite=300):
    url = f"https://www.ihfc.com.br/{'' if arq == 'index.html' else arq}?v={int(time.time())}"
    fim = time.time() + limite
    while time.time() < fim:
        try:
            corpo = urllib.request.urlopen(url, timeout=20).read()
            if assinatura(corpo) == esperado:
                return True
        except Exception:
            pass
        time.sleep(20)
    return False


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "conferir"
    erros = conferir()
    for e in erros:
        print("ERRO", e)
    if erros:
        sys.exit(f"PAROU: {len(erros)} problema(s). Corrija na fonte (gerador) e rode de novo.")
    print("conferência ok")
    if modo != "publicar":
        sys.exit(0)
    msg, arqs = sys.argv[2], sys.argv[3:]
    if not arqs:
        sys.exit("PAROU: diga quais arquivos publicar (nunca 'git add -A').")
    if git("add", "--", *arqs).returncode:
        sys.exit("PAROU: git add falhou")
    r = git("commit", "-m", msg + "\n\nCo-Authored-By: Claude <noreply@anthropic.com>", "--", *arqs)
    if r.returncode and "nothing to commit" not in r.stdout:
        sys.exit("PAROU: commit falhou: " + r.stdout + r.stderr)
    if git("push").returncode:
        sys.exit("PAROU: push falhou (rode de novo; se repetir, sobe de modelo)")
    print("enviado; esperando o GitHub Pages (até 5 min por arquivo)...")
    for a in arqs:
        if a.endswith((".html", ".pdf", ".xml", ".txt")):
            h = assinatura(open(a, "rb").read())
            print(("NO AR  " if no_ar(a, h) else "ATRASO ") + a)
    print("pronto. Se algo ficou ATRASO: o build do Pages está na fila; confira de novo em 10 min, não republique.")
