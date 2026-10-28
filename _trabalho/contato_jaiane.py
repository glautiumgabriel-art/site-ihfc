"""Pedido do Dr. (28/10/2026, L-456): Jaiane como contato para dúvidas, sugestões, críticas e renegociação, no bloco de contato.
Texto igual ao da revista. Sem --publicar gera só contato-jaiane-previa.html (noindex) para o OK do Dr.;
com --publicar aplica no novo.html e roda o montar_v5 (home oficial)."""
import os, sys, subprocess
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUBLICAR = '--publicar' in sys.argv
WA = 'https://wa.me/5573988077281?text=Ol%C3%A1%2C%20Jaiane!%20Vim%20pelo%20site%20do%20IHFC.'
BLOCO = f'''
    <div class="fale-jaiane">
      <img src="img/ihfc-equipe-jaiane-santos-v2.webp" alt="Jaiane Santos" loading="lazy">
      <div><p>Dúvidas, sugestões, críticas construtivas ou renegociação? <b>Fale com a Jaiane</b></p>
      <a href="{WA}" target="_blank" rel="noopener">WhatsApp · (73) 98807-7281</a></div>
    </div>'''
CSS = '''<style>
.fale-jaiane{display:flex;gap:16px;align-items:center;margin-top:2rem;padding:18px 20px;border:1px solid var(--linha);border-radius:18px;max-width:36rem}
.fale-jaiane img{width:72px;height:72px;border-radius:50%;object-fit:cover;object-position:center 20%;flex:0 0 72px}
.fale-jaiane p{margin:0 0 .4rem;color:var(--creme2);font-size:.95rem}
.fale-jaiane b{color:var(--creme);font-weight:500}
.fale-jaiane a{color:var(--ouro);text-decoration:none;font-size:.92rem}
</style>
'''
ANCORA = '    <div class="infos">'
arq = 'novo.html' if PUBLICAR else 'index.html'
h = open(arq, encoding='utf-8').read()
if 'fale-jaiane' not in h:
    assert h.count(ANCORA) == 1, 'âncora do contato não achada'  # L-328
    h = h.replace(ANCORA, BLOCO.lstrip('\n') + '\n' + ANCORA).replace('</head>', CSS + '</head>', 1)
if PUBLICAR:
    open('novo.html', 'w', encoding='utf-8').write(h)
    subprocess.run([sys.executable, '_trabalho/montar_v5.py'], check=True)
    assert 'fale-jaiane' in open('index.html', encoding='utf-8').read()
    print('publicado na home')
else:
    h = h.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    open('contato-jaiane-previa.html', 'w', encoding='utf-8').write(h)
    print('prévia: contato-jaiane-previa.html')
