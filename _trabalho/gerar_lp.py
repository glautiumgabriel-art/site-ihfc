"""Páginas de destino dos anúncios (ordem do Dr. 13/11/2026 via TRIAGEM): Papada, Lábios, Corpo e Avaliação (T1).
- Antes e depois e depoimentos SÓ com material aprovado pela recepção, com termo assinado, lido de
  _aprovados/<chave>/aprovado.json (pasta fora do git). Sem material aprovado, a seção NÃO aparece.
  Nunca foto de banco, exemplo ou IA no lugar de resultado real (regra 59 / CFO 196/2019).
- Pixel da Meta: ID em _trabalho/pixel-id.txt (só números). Sem o arquivo, a página sai sem pixel.
  Evento Contact no clique de qualquer link do WhatsApp.
- UTM: a origem do anúncio (utm_campaign / utm_content) vai no fim da mensagem do WhatsApp.
Rodar: python _trabalho/gerar_lp.py   (de dentro de _clinica/site-ihfc)

aprovado.json (exemplo):
{"fotos":[{"antes":"a1.jpg","depois":"d1.jpg","procedimento":"Lipo de papada","termo_assinado":true,
           "aprovado_por":"recepção","data":"2026-11-13","sem_filtro":true}],
 "depoimentos":[{"texto":"...","autor":"M. S.","autorizado":true,"data":"2026-11-13"}]}
"""
import os, json, shutil, re
from html import escape
from gerar_frentes import FRENTES, ICONE_ZAP, zap

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APROV = os.path.join(RAIZ, "_aprovados")
F = {f["arq"]: f for f in FRENTES}
DR = ("img/ihfc-equipe-glautium-gabriel.webp", "Dr. Glautium Gabriel",
      "Cirurgião e Traumatologista Bucomaxilofacial - Especialista em Harmonização Orofacial", "CRO-BA 16384")

LPS = [
    dict(arq="lp-papada.html", chave="PAPADA", pasta="papada", titulo="Papada",
         h1="Papada que não sai com dieta <em>tem causa</em>.",
         dor=F["papada-e-rosto.html"]["dor"], foto=F["papada-e-rosto.html"]["foto"],
         itens=F["papada-e-rosto.html"]["itens"][:4], quem=[DR],
         botao="Quero avaliar minha papada", texto="Quero uma avaliação de papada."),
    dict(arq="lp-labios.html", chave="LABIOS", pasta="labios", titulo="Lábios",
         h1="Lábios naturais, <em>planejados com o rosto</em>.",
         dor="Lábios finos, sem contorno ou com o lábio de cima comprido. O Dr. Glautium avalia o rosto inteiro antes de indicar o caminho, para o resultado ficar natural.",
         foto="img/ihfc-rosto-fino.webp",
         itens=[("Preenchimento com ácido hialurônico", "Volume e contorno na medida do seu rosto."),
                ("Lip lift", "Elevação do lábio superior, com cicatriz escondida."),
                ("Queiloplastia", "Correção cirúrgica do lábio, quando indicada."),
                ("Harmonização natural", "Lábios planejados junto com queixo, nariz e sorriso.")],
         quem=[DR], botao="Quero avaliar meus lábios", texto="Quero uma avaliação de lábios."),
    dict(arq="lp-corpo.html", chave="CORPO", pasta="corpo", titulo="Corpo",
         h1=F["corpo.html"]["h1"], dor=F["corpo.html"]["dor"], foto=F["corpo.html"]["foto"],
         itens=F["corpo.html"]["itens"][:4], quem=F["corpo.html"]["quem"],
         botao=F["corpo.html"]["botao"], texto=F["corpo.html"]["texto"]),
    dict(arq="lp-avaliacao.html", chave="AVALIACAO", pasta="geral", titulo="Avaliação",
         h1="Cuidado completo, <em>do rosto ao corpo</em>.",
         dor="Médicos, dentistas e especialistas em um só lugar, em Jequié. Comece por uma avaliação: a equipe entende a sua queixa e indica o profissional certo.",
         foto="img/ihfc-hero-rosto.webp",
         itens=[("Rosto e papada", "Harmonização natural, papada e contorno."),
                ("Corpo", "Gordura localizada, flacidez e celulite."),
                ("Sorriso e implantes", "Odontologia estética e reabilitação."),
                ("Pele, cabelo e nutrição", "Tratamentos com a equipe multiprofissional.")],
         quem=[DR], botao="Quero agendar minha avaliação", texto="Quero agendar uma avaliação."),
]

PROVA = ('<p class="v5-prova"><b>5,0 ★</b> · 99 avaliações de pacientes no Google · '
         '<a href="https://www.google.com/maps/search/?api=1&query=IHFC+R.+Dr.+Jo%C3%A3o+Braga+640+Jequiezinho+Jequi%C3%A9+BA" '
         'target="_blank" rel="noopener">ver no Google Maps</a></p>')


def aprovado(lp):
    """Só itens com termo assinado / autorização explícita; copia as fotos para img/resultados/."""
    arq = os.path.join(APROV, lp["pasta"], "aprovado.json")
    if not os.path.exists(arq):
        return [], []
    d = json.load(open(arq, encoding="utf-8"))
    fotos, deps = [], []
    destino = os.path.join(RAIZ, "img", "resultados")
    for i, f in enumerate(d.get("fotos", [])):
        if not (f.get("termo_assinado") is True and f.get("sem_filtro") is True and f.get("procedimento") and f.get("aprovado_por")):
            continue
        par = []
        for lado in ("antes", "depois"):
            src = os.path.join(APROV, lp["pasta"], f[lado])
            if not os.path.exists(src):
                par = None; break
            nome = f"ihfc-{lp['pasta']}-resultado{i + 1}-{lado}{os.path.splitext(src)[1].lower()}"
            os.makedirs(destino, exist_ok=True)
            shutil.copy2(src, os.path.join(destino, nome))
            par.append("img/resultados/" + nome)
        if par:
            fotos.append((par[0], par[1], f["procedimento"]))
    for t in d.get("depoimentos", []):
        if t.get("autorizado") is True and t.get("texto"):
            deps.append((t["texto"], t.get("autor", "")))
    return fotos, deps


def pixel_id():
    p = os.path.join(RAIZ, "_trabalho", "pixel-id.txt")
    if os.path.exists(p):
        v = open(p, encoding="utf-8").read().strip()
        if re.fullmatch(r"\d{10,20}", v):
            return v
    return None


def pixel_head(pid):
    if not pid:
        return ""
    return f'''<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{pid}');fbq('track','PageView');</script>
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id={pid}&ev=PageView&noscript=1"></noscript>
'''


def pagina(lp, pid):
    link = zap(lp["chave"], lp["texto"])
    fotos, deps = aprovado(lp)
    itens = "".join(f'<div class="proc"><h3>{t}</h3><p>{d}</p></div>' for t, d in lp["itens"])
    quem = "".join(f'<div class="pessoa"><img src="{i}" alt="{n}" loading="lazy"><h3>{n}</h3><p>{p}</p>{f"<span>{r}</span>" if r else ""}</div>' for i, n, p, r in lp["quem"])
    sec_ad = ""
    if fotos:
        cards = "".join(f'<figure class="ad-par"><div><img src="{a}" alt="Antes: {escape(p)}" loading="lazy"><span>Antes</span></div>'
                        f'<div><img src="{d}" alt="Depois: {escape(p)}" loading="lazy"><span>Depois</span></div>'
                        f'<figcaption>{escape(p)}</figcaption></figure>' for a, d, p in fotos)
        sec_ad = f'''<section class="v5-bloco" id="resultados"><div class="wrap">
    <span class="eyebrow">Antes e depois</span><h2>Resultados <em>de pacientes reais</em>.</h2>
    <div class="ad-grade">{cards}</div>
    <p class="aviso-cfo">Fotos publicadas com autorização por escrito dos pacientes, sem filtro. Os resultados variam de pessoa para pessoa. Responsável técnico: Dr. Glautium Gabriel, CRO-BA 16384.</p>
  </div></section>'''
    sec_dep = ""
    if deps:
        cards = "".join(f'<blockquote class="dep">“{escape(t)}”{f"<cite>{escape(a)}</cite>" if a else ""}</blockquote>' for t, a in deps)
        sec_dep = f'''<section class="v5-bloco" id="depoimentos"><div class="wrap">
    <span class="eyebrow">Depoimentos</span><h2>Quem já <em>passou por aqui</em>.</h2>
    <div class="dep-grade">{cards}</div>
    <p class="aviso-cfo">Depoimentos publicados com autorização. A experiência de cada pessoa é individual.</p>
  </div></section>'''
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, follow">
<title>{lp["titulo"]} · IHFC Jequié</title>
<meta name="description" content="{escape(lp["dor"])}">
<link rel="canonical" href="https://www.ihfc.com.br/{lp["arq"]}">
<link rel="icon" href="img/ihfc-favicon-32.png" sizes="32x32">
<meta name="theme-color" content="#0e0c0a">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="estilo.css?v=20261027c">
<style>
.v5-bloco{{padding:64px 0}}
.v5-passos{{list-style:none;display:grid;gap:12px;margin:0 0 1.8rem;padding:0;counter-reset:p}}
@media(min-width:900px){{.v5-passos{{grid-template-columns:repeat(3,1fr)}}}}
.v5-passos li{{counter-increment:p;padding:20px 22px;border:1px solid var(--linha);border-radius:16px}}
.v5-passos li:before{{content:counter(p);display:block;font-family:var(--serif);font-size:2rem;color:var(--ouro);line-height:1}}
.v5-passos b{{display:block;color:var(--creme);font-weight:500;margin:.4rem 0 .2rem}}
.v5-passos span{{color:var(--creme2);font-size:.95rem}}
.v5-prova{{margin-top:1.4rem;color:var(--creme2);font-size:.95rem}}
.v5-prova b{{color:var(--ouro);font-weight:600}} .v5-prova a{{color:var(--ouro)}}
.ad-grade{{display:grid;gap:18px}} @media(min-width:900px){{.ad-grade{{grid-template-columns:1fr 1fr}}}}
.ad-par{{margin:0;display:grid;grid-template-columns:1fr 1fr;gap:6px}}
.ad-par div{{position:relative}} .ad-par img{{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:12px}}
.ad-par span{{position:absolute;left:8px;top:8px;background:rgba(14,12,10,.7);color:var(--creme);font-size:.75rem;padding:3px 8px;border-radius:8px}}
.ad-par figcaption{{grid-column:1/-1;color:var(--creme2);font-size:.9rem}}
.dep-grade{{display:grid;gap:12px}} @media(min-width:900px){{.dep-grade{{grid-template-columns:repeat(3,1fr)}}}}
.dep{{margin:0;padding:20px 22px;border:1px solid var(--linha);border-radius:16px;color:var(--creme2);font-style:italic}}
.dep cite{{display:block;margin-top:.8rem;font-style:normal;color:var(--ouro);font-size:.85rem}}
main{{padding-bottom:70px}}
</style>
{pixel_head(pid)}</head>
<body>
<!-- gerado por _trabalho/gerar_lp.py: editar lá, não aqui -->
<header id="topo">
  <div class="wrap nav">
    <a href="./" aria-label="IHFC, página inicial"><img src="img/ihfc-logo-branco.png" alt="IHFC"></a>
    <a class="btn btn-ouro" href="{link}" target="_blank" rel="noopener">Agendar</a>
  </div>
</header>

<main>
<section class="hero-interna">
  <div class="wrap duas-col" style="align-items:center">
    <div>
      <span class="eyebrow">{lp["titulo"]} · IHFC Jequié</span>
      <h1>{lp["h1"]}</h1>
      <p>{lp["dor"]}</p>
      <p style="margin-top:2rem"><a class="btn btn-ouro" href="{link}" target="_blank" rel="noopener">{ICONE_ZAP}{lp["botao"]}</a></p>
      {PROVA}
    </div>
    <img class="foto-alta" src="{lp["foto"]}" alt="" style="aspect-ratio:4/4.4">
  </div>
</section>

<section class="seguranca" style="padding-top:40px">
  <div class="wrap">
    <span class="eyebrow">O que pode ser feito</span>
    <h2>Caminhos que a avaliação <em>pode indicar</em>.</h2>
    <div class="procs" style="margin-top:2.2rem">{itens}</div>
    <p class="aviso-cfo">A indicação é individual e só é feita na avaliação presencial. O resultado varia de pessoa para pessoa. Imagens ilustrativas.</p>
  </div>
</section>
{sec_ad}
{sec_dep}
<section class="equipe">
  <div class="wrap">
    <span class="eyebrow">Quem faz</span>
    <h2>Quem cuida <em>de você</em>.</h2>
    <div class="grade-equipe">{quem}</div>
  </div>
</section>

<section class="v5-bloco" id="agendar">
  <div class="wrap">
    <span class="eyebrow">Como agendar</span>
    <h2>Três passos, <em>sem complicação</em>.</h2>
    <ol class="v5-passos">
      <li><b>Conte o que te incomoda</b><span>Toque no botão: a mensagem já vai pronta para a recepção.</span></li>
      <li><b>Escolha o melhor horário</b><span>A recepção encontra o dia e o profissional certos para você.</span></li>
      <li><b>Venha para a avaliação</b><span>R. Dr. João Braga, 640, Jequiezinho, Jequié/BA.</span></li>
    </ol>
    <a class="btn btn-ouro" href="{link}" target="_blank" rel="noopener">{ICONE_ZAP}{lp["botao"]}</a>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <img src="img/ihfc-logo-branco.png" alt="IHFC">
    <span>IHFC · Instituto de Harmonização Facial e Corporal · Responsável técnico: Dr. Glautium Gabriel, CRO-BA 16384 · EPAO 5145 · CNES 4327152</span>
    <span class="rodape-links"><a href="./">Início</a><a href="procedimentos.html">Procedimentos</a><a href="equipe.html">Equipe</a><a href="privacidade.html">Privacidade</a></span>
  </div>
</footer>

<a class="zap btn btn-ouro" href="{link}" target="_blank" rel="noopener">{ICONE_ZAP}Falar com a recepção</a>
<script>
(function(){{
  var q=new URLSearchParams(location.search),o={{}};
  try{{o=JSON.parse(sessionStorage.getItem('ihfc_utm')||'{{}}')}}catch(e){{}}
  ['utm_source','utm_campaign','utm_content'].forEach(function(k){{if(q.get(k))o[k]=q.get(k)}});
  try{{sessionStorage.setItem('ihfc_utm',JSON.stringify(o))}}catch(e){{}}
  var tag=[o.utm_campaign,o.utm_content].filter(Boolean).join(' / ');
  document.querySelectorAll('a[href*="wa.me"]').forEach(function(a){{
    if(tag){{a.href=a.href+encodeURIComponent(' (anúncio: '+tag.slice(0,80)+')');}}
    a.addEventListener('click',function(){{if(window.fbq)fbq('track','Contact',{{content_name:'{lp["chave"]}'}});}});
  }});
  var topo=document.getElementById('topo');
  addEventListener('scroll',function(){{topo.classList.toggle('sol',scrollY>40)}},{{passive:true}});
}})();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    pid = pixel_id()
    for lp in LPS:
        h = pagina(lp, pid)
        open(os.path.join(RAIZ, lp["arq"]), "w", encoding="utf-8").write(h)
        print(lp["arq"], "pixel" if pid else "sem pixel", "A/D" if 'id="resultados"' in h else "sem A/D",
              "dep" if 'id="depoimentos"' in h else "sem dep")
