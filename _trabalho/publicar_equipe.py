"""Publica a página Equipe (Dr. aprovou às 20:02 de 29/10/2026, item site-equipe-pagina) e liga ela ao site:
menu "Equipe" da home, link abaixo da faixa da equipe, rodapé de todas as páginas, menus das páginas internas e sitemap."""
import os, sys, glob, re, subprocess
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RODAPE = '<a href="equipe.html">Equipe</a>'

def trocar(arq, pares, obrigatorio=True):
    s = open(arq, encoding='utf-8').read(); o = s  # ler antes de abrir para escrita (L-653)
    for a, b in pares:
        if b in s: continue
        assert a in s or not obrigatorio, f'{arq}: trecho não achado: {a[:60]}'  # L-328
        s = s.replace(a, b, 1)
    if s != o: open(arq, 'w', encoding='utf-8').write(s); print('ok', arq)

# home (gerada pelo montar_v5): menu e link abaixo da faixa
trocar('_trabalho/montar_v5.py', [
    ('<li><a href="#equipe">Equipe</a></li>', '<li><a href="equipe.html">Equipe</a></li>'),
    ('<p class="v5-dica">Arraste para o lado →</p>', '<p class="v5-dica">Arraste para o lado → · <a href="equipe.html" style="color:var(--ouro)">Ver a equipe completa</a></p>')])
# rodapé: logo depois do Dr. Glautium; onde ele não está no rodapé (a própria página dele), depois de Procedimentos
for arq in sorted(set(glob.glob('*.html')) - {'equipe.html'}) + ['_trabalho/gerar_frentes.py']:
    if 'previa' in arq or arq.startswith('v5') or arq in ('index.html', 'novo.html'): continue
    s = open(arq, encoding='utf-8').read()
    if 'rodape-links' not in s or RODAPE in s: continue
    k = s.index('<span class="rodape-links">'); fim = s.index('</span>', k)
    dr = s.find('<a href="dr-glautium.html">Dr. Glautium</a>', k, fim)
    pos = dr + len('<a href="dr-glautium.html">Dr. Glautium</a>') if dr > 0 else s.index('</a>', k) + 4
    open(arq, 'w', encoding='utf-8').write(s[:pos] + RODAPE + s[pos:]); print('ok rodapé', arq)
# menus das páginas internas que listam o Dr. Glautium
for arq in glob.glob('*.html') + ['_trabalho/inicio_policlinica.py']:
    if 'previa' in arq: continue
    for li in ('<li><a href="dr-glautium.html">Dr. Glautium</a></li>', '<li><a class="ativo" href="dr-glautium.html">Dr. Glautium</a></li>'):
        trocar(arq, [(li, li + '\n      <li><a href="equipe.html">Equipe</a></li>')], obrigatorio=False)
trocar('novo.html', [('<span class="rodape-links"><a href="procedimentos.html">Procedimentos</a><a href="dr-glautium.html">Dr. Glautium</a>',
                      '<span class="rodape-links"><a href="procedimentos.html">Procedimentos</a><a href="dr-glautium.html">Dr. Glautium</a>' + RODAPE)])
trocar('sitemap.xml', [('<url><loc>https://www.ihfc.com.br/dr-glautium.html</loc></url>',
                        '<url><loc>https://www.ihfc.com.br/dr-glautium.html</loc></url>\n<url><loc>https://www.ihfc.com.br/equipe.html</loc></url>')])
subprocess.run([sys.executable, '_trabalho/montar_v5.py'], check=True)
subprocess.run([sys.executable, '_trabalho/montar_equipe.py', '--publicar'], check=True)
# na página Equipe, as âncoras do menu apontam para a home
e = open('equipe.html', encoding='utf-8').read()
e = re.sub(r'<meta name="robots" content="noindex[^"]*">\n?', '', e)  # o novo.html é rascunho, a Equipe vai para o Google
e = re.sub(r'href="#(dores|portas|areas|seguranca|instituto|inicio)"', r'href="./#\1"', e)
e = e.replace('<li><a href="#equipe">Equipe</a></li>', '<li><a class="ativo" href="equipe.html">Equipe</a></li>')
open('equipe.html', 'w', encoding='utf-8').write(e)
h = open('index.html', encoding='utf-8').read()
assert 'href="equipe.html"' in h and 'noindex' not in e and e.count('class="faz"') == 12
print('equipe publicada')
