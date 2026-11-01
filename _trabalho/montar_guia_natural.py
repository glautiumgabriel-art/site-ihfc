"""Página "Guia da harmonização natural" (isca do Reel "Comenta NATURAL", 04/11 19h; pedido do MARKETING em 01/11/2026).
Texto e PDF do MARKETING (_conhecimento/marketing-clinica/iscas/natural/), já conferidos com o CFO; aqui só entra no visual do site.
Base: cabeçalho, contato e rodapé do novo.html. Grava guia-natural.html (servido também em /guia-natural)."""
import os, re, shutil
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORIGEM = '../../_conhecimento/marketing-clinica/iscas/natural/'
PDF = 'ihfc_guia-harmonizacao-natural_v1.pdf'
shutil.copy(ORIGEM + PDF, PDF)
g = open(ORIGEM + 'guia-natural.html', encoding='utf-8').read()
corpo = g[g.index('<h2>Os 3 erros'):g.index('<div class="cta">')]
corpo = corpo.replace('</div>\n<div class="pg">', '').replace(' style="margin-top:0"', '')
corpo = corpo.replace('<div class="card"><b class="n">', '<div class="erro surge"><b class="n">')
WA = 'https://wa.me/5573981507715?text=Ol%C3%A1!%20Li%20o%20Guia%20da%20harmoniza%C3%A7%C3%A3o%20natural%20e%20quero%20agendar%20uma%20avalia%C3%A7%C3%A3o.'
secao = f'''<section class="guia"><div class="wrap">
<span class="eyebrow surge">Guia gratuito</span>
<h1 class="surge" style="font-size:clamp(2.2rem,6vw,3.6rem)">Guia da harmonização <em>natural</em>.</h1>
<p class="lead surge" style="max-width:40rem">O que saber antes de fazer, para ficar com o seu rosto, só que mais descansado. Dr. Glautium Gabriel · CRO-BA 16384</p>
<p class="botoes surge"><a class="btn btn-ouro" href="{PDF}" download>Baixar o guia em PDF</a> <a class="btn btn-linha" href="{WA}" target="_blank" rel="noopener">Agendar pelo WhatsApp</a></p>
<div class="guia-texto">
{corpo}</div>
<p class="botoes surge"><a class="btn btn-ouro" href="{WA}" target="_blank" rel="noopener">Agendar a sua avaliação pelo WhatsApp</a> <a class="btn btn-linha" href="{PDF}" download>Baixar o PDF</a></p>
<p class="aviso">Este guia é informativo e não substitui a avaliação individual. Cada rosto tem a sua indicação, e os resultados variam de pessoa para pessoa.</p>
</div></section>

'''
CSS = ('<style>.guia{padding-top:8.5rem}.guia .botoes{display:flex;flex-wrap:wrap;gap:12px;margin:1.6rem 0}'
       '.guia-texto{max-width:46rem}.guia-texto h2{font-size:clamp(1.5rem,4vw,2.1rem);margin:2.6rem 0 1rem}'
       '.guia .erro{border:1px solid var(--linha);border-radius:16px;padding:16px 18px;margin:12px 0;color:var(--creme2);line-height:1.6}'
       '.guia .erro b{color:var(--creme);font-weight:500}.guia .erro .n{color:var(--ouro);font-size:1.4rem;margin-right:10px;font-family:inherit}'
       '.guia-texto ul,.guia-texto ol{padding-left:1.4rem}.guia-texto li{color:var(--creme2);line-height:1.6;margin:.45rem 0}.guia-texto li b{color:var(--creme)}'
       '.guia .aviso{font-size:.8rem;color:var(--suave);max-width:46rem}</style>\n')
n = open('novo.html', encoding='utf-8').read()
cab = n[:n.index('<section class="hero"')]
contato = n[n.index('<section class="contato"'):]
cab = re.sub(r'<title>.*?</title>', '<title>Guia da harmonização natural | IHFC Jequié-BA</title>', cab, count=1, flags=re.S)
cab = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\1https://www.ihfc.com.br/guia-natural.html', cab)
cab = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', cab, flags=re.S)
DESC = 'Guia gratuito do IHFC: os 3 erros que dão "cara de harmonizada", sinais de um planejamento natural e 5 perguntas para fazer na sua avaliação.'
cab = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + DESC, cab)
cab = cab.replace('<meta property="og:title" content="IHFC · Instituto de Harmonização Facial e Corporal">', '<meta property="og:title" content="Guia da harmonização natural · IHFC">')
cab = cab.replace('<meta property="og:url" content="https://www.ihfc.com.br/">', '<meta property="og:url" content="https://www.ihfc.com.br/guia-natural.html">')
cab = re.sub(r'<meta name="robots" content="noindex[^"]*">\n?', '', cab)
cab = cab.replace('</head>', CSS + '</head>', 1)
h = cab + secao + contato
h = re.sub(r'href="#(dores|portas|areas|seguranca|instituto|inicio|equipe|assessores)"', r'href="./#\1"', h)
assert h.count('class="erro') == 3 and '5 perguntas' in h and PDF in h and 'noindex' not in h
open('guia-natural.html', 'w', encoding='utf-8').write(h); print('ok guia-natural.html')
