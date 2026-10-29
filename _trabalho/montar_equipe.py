"""Página "Equipe" com a descrição completa de cada pessoa (Dr., 29/10/2026 19:48, item site-area-equipe).
Base: cabeçalho, equipe, assessores, contato e rodapé do novo.html; o que cada um faz vem do que o site já publica
(queixas.js) e das descrições do Dr. (_conhecimento/clinica/EQUIPE-IHFC.md). Nada inventado (L-362).
Sem --publicar gera equipe-previa.html (noindex); com --publicar grava equipe.html."""
import os, sys, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUBLICAR = '--publicar' in sys.argv
FAZ = {  # o que cada um atende no IHFC, como já publicado no site
    'Dr. Glautium Gabriel': 'Cirurgias estéticas da face, queiloplastia (lábio duplo), DTM e dor orofacial, lesões da boca e câncer bucal; harmonização facial: toxina botulínica, preenchimentos, bioestimuladores, fios, rinomodelação, lábios, papada e Endolaser.',
    'Dra. Ionara Caroso': 'Avaliação dermatológica, acne, rosácea, manchas, pintas e pequenas cirurgias, hiperidrose, laser e luz intensa pulsada; corpo: gordura localizada, flacidez, celulite, estrias, vasinhos (escleroterapia) e emagrecimento com acompanhamento médico.',
    'Dr. Hudson D. Soares': 'Avaliação odontológica, implantes dentários, lentes de contato dental e facetas, clareamento, alinhadores invisíveis e planejamento digital do sorriso.',
    'Dra. Juliana Coelho Moreno': 'Avaliação odontológica, implantes dentários, lentes de contato dental e facetas, clareamento, alinhadores invisíveis, planejamento digital do sorriso e atendimento infantil.',
    'Dr. Mateus Silva Brito': 'Avaliação tricológica, tratamento clínico da queda de cabelo e implante capilar.',
    'Dra. Jéssica Lopes': 'Toxina botulínica, bioestimuladores, microvasos (PEIM) e clareamento de áreas.',
    'Maria Eduarda Brisola': 'Limpeza de pele protocolada, peelings e microagulhamento.',
    'Sabrina Amparo': 'Avaliação nutricional, bioimpedância, plano alimentar, recomposição corporal e acompanhamento contínuo.',
    'Gisele Gomes': 'Fisioterapia para diástase, drenagem no pós-operatório, liberação miofascial e estrias.',
    'Maria Neuza': 'Unha encravada e órtese, fungos nas unhas, calos e rachaduras, cuidado com o pé diabético e spa dos pés.',
    'Natieli Batista': 'Feridas (ozonioterapia, laserterapia, PRP e PRF), reposição de vitaminas injetável com a Dra. Ionara, cuidado com inflamação e dores, drenagem e massoterapia.',
    'Tátila Argolo': 'Massagem relaxante e massagem modeladora.',
}
n = open('novo.html', encoding='utf-8').read()
cab = n[:n.index('<section class="hero"')]
i = n.index('<section class="equipe"'); f = n.index('</section>', n.index('<section class="assessores"')) + len('</section>')
equipe = n[i:f]
contato = n[n.index('<section class="contato"'):]
cards = re.findall(r'<div class="pessoa surge">.*?<h3>(.*?)</h3>.*?</div>', equipe)
assert sorted(cards) == sorted(FAZ), f'equipe diferente: {set(cards) ^ set(FAZ)}'  # L-328: ninguém sem descrição
for nome, txt in FAZ.items():
    equipe = re.sub(rf'(<h3>{re.escape(nome)}</h3><p>[^<]*</p>(?:<span>[^<]*</span>)?)', rf'\1<p class="faz">{txt}</p>', equipe, count=1)
assert equipe.count('class="faz"') == len(FAZ)
equipe = equipe.replace('<h2 class="surge">Quem cuida <em>de você</em>.</h2>',
                        '<h1 class="surge" style="font-size:clamp(2.2rem,6vw,3.6rem)">Quem cuida <em>de você</em>.</h1>'
                        '<p class="lead surge" style="max-width:40rem">Conheça cada profissional do IHFC e o que cada um atende.</p>')
CSS = ('<style>.equipe{padding-top:8.5rem}.pessoa .faz{font-size:.86rem;color:var(--creme2);margin-top:.6rem;line-height:1.5}'
       '.pessoa span{display:block;margin-top:.3rem}'
       '@media(max-width:700px){.grade-equipe{grid-template-columns:1fr!important;gap:28px!important}'  # celular: foto ao lado
       '.pessoa{display:grid;grid-template-columns:112px 1fr;column-gap:16px;align-items:start}'
       '.pessoa img{grid-row:1/span 4}.pessoa h3{margin-top:0;font-size:1.2rem}}</style>\n')
cab = re.sub(r'<title>.*?</title>', '<title>Equipe IHFC | Profissionais em Jequié-BA</title>', cab, count=1, flags=re.S)
cab = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\1https://www.ihfc.com.br/equipe.html', cab)
cab = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', cab, flags=re.S)  # schema da clínica fica na home
cab = cab.replace('</head>', CSS + '</head>', 1)
DESC = 'Equipe do IHFC em Jequié-BA: cada profissional e o que atende.'
cab = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', rf'\g<1>{DESC}', cab)
cab = cab.replace('<meta property="og:title" content="IHFC · Instituto de Harmonização Facial e Corporal">', '<meta property="og:title" content="Equipe IHFC · Jequié-BA">')
cab = cab.replace('<meta property="og:url" content="https://www.ihfc.com.br/">', '<meta property="og:url" content="https://www.ihfc.com.br/equipe.html">')
h = cab + equipe + '\n\n' + contato
if PUBLICAR:
    open('equipe.html', 'w', encoding='utf-8').write(h); print('publicada: equipe.html')
else:
    h = h.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    open('equipe-previa.html', 'w', encoding='utf-8').write(h); print('prévia: equipe-previa.html')
