"""PRÉVIA (fora do ar, noindex, sem link no site): 'Face' com quadrados por assunto do rosto.
Pedido do Dr. 14/11 23:13 via Olívia (L-1185). Textos só de procedimentos.html. Rodar de _trabalho/."""
import re, os, html
from urllib.parse import quote
from gerar_frentes import FRENTES, pagina, zap, ICONE_ZAP
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
proc = open(os.path.join(RAIZ, "procedimentos.html"), encoding="utf-8").read()
desc = {t: d for t, d in re.findall(r'<div class="proc"><h3>(.*?)</h3><p>(.*?)</p>', proc, re.S)}
QUADROS = [
 ("Papada e rosto", "FACE-PAPADA", None, ["Lipo de papada", "Platismoplastia", "Cervicoplastia"]),
 ("Linhas de expressão", "FACE-LINHAS", "Testa, glabela e olhos.", ["Toxina botulínica"]),
 ("Lábios", "FACE-LABIOS", "Contorno e volume planejados junto com o rosto.", ["Lábios", "Lip lift"]),
 ("Olheiras e contorno", "FACE-CONTORNO", "Volume e contorno de olheiras, malar, mandíbula e queixo.", ["Ácido hialurônico", "Mentoplastia", "Bichectomia"]),
 ("Nariz", "FACE-NARIZ", "Ajuste de perfil sem cirurgia.", ["Rinomodelação"]),
 ("Firmeza e flacidez", "FACE-FIRMEZA", "Sustentação e estímulo de colágeno.", ["Bioestimuladores de colágeno", "Fios de sustentação", "Endolaser facial", "Skinbooster"]),
 ("Manchas e pele", "FACE-PELE", "Melasma, cicatriz de acne, textura.", ["Peelings", "Microagulhamento", "Revitalli"]),
 ("Cirurgias do rosto", "FACE-CIRURGIA", "Consulta pré-cirúrgica com monitorização completa na cirurgia.", ["Enxerto de gordura", "Revisão de cicatriz e queloide", "Mentoplastia"]),
]
def quadro(t, ch, resumo, itens):
    if resumo is None or True:
        resumo = desc[itens[0]].split(". ")[0].rstrip(".") + "."  # frase literal do site (1ª do primeiro item)
    lis = "".join(f"<li><strong>{i}</strong>{(' — ' + desc[i]) if i in desc else ''}</li>" for i in itens)
    link = zap(ch, f"Quero saber sobre {t.lower()}.")
    return (f'<article class="proc"><h3>{t}</h3><p>{resumo}</p>'
            f'<details style="margin-top:.8rem"><summary style="cursor:pointer;color:var(--ouro)">O que pode ser indicado</summary>'
            f'<ul style="margin:.6rem 0 0 1rem;font-size:.86rem;color:var(--suave)">{lis}</ul></details>'
            f'<p style="margin-top:1rem"><a class="btn btn-linha" href="{link}" target="_blank" rel="noopener">Falar sobre isto</a>'
            + (' <a href="papada-e-rosto.html" style="margin-left:.8rem;color:var(--ouro)">Ver a página completa</a>' if ch == "FACE-PAPADA" else "") + '</p></article>')
f = dict(FRENTES[0]); f["arq"] = "face-previa.html"; f["titulo"] = "Face"; f["chave"] = "FACE-GERAL"; f["botao"] = "Quero avaliar meu rosto"; f["texto"] = "Quero uma avaliação do meu rosto com o Dr. Glautium."; f["foto"] = "img/ihfc-rosto-fino.webp"
f["h1"] = "O que no seu rosto <em>incomoda você</em>?"
f["dor"] = "Escolha o assunto. A indicação é individual e só é feita na avaliação com o Dr. Glautium."
h = pagina(f)
tiles = '<div class="procs" style="margin-top:2.2rem">' + "".join(quadro(*q) for q in QUADROS) + "</div>"
h = re.sub(r'<div class="procs".*?</div>\s*(?=<p class="aviso-cfo">)', tiles + "\n    ", h, count=1, flags=re.S)
h = h.replace('<h2>Caminhos que a avaliação <em>pode indicar</em>.</h2>', '<h2>Escolha o <em>assunto</em>.</h2>')
h = h.replace('<link rel="canonical" href="https://www.ihfc.com.br/face-previa.html">', '<meta name="robots" content="noindex,nofollow">')
h = re.sub(r'<meta property="og:url"[^>]*>\n', '', h)
h = h.replace('<li><a href="papada-e-rosto.html">Papada e rosto</a></li>', '<li><a class="ativo" href="face-previa.html">Face</a></li>')
h = h.replace("<!-- gerado por _trabalho/gerar_frentes.py: editar lá, não aqui -->", "<!-- PRÉVIA gerada por _trabalho/gerar_face_previa.py: editar lá. Fora do ar, sem link no site. -->")
open(r"G:/VIDEOS IA/_conhecimento/marketing-clinica/previas/face-previa.html", "w", encoding="utf-8").write(h)
print("ok face-previa.html", h.count('<article class="proc">'), "quadros")
