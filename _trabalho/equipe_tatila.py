"""29/10/2026: Tátila Argolo (massoterapeuta) entra na equipe do site. Foto profissional e função enviadas pela clínica
(Jaiane, via ROBÔ WHATSAPP). Sem --publicar gera só equipe-tatila-previa.html (noindex) para o OK do Dr.;
com --publicar aplica no novo.html e roda o montar_v5 (home oficial)."""
import os, sys, shutil, subprocess
from PIL import Image
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUBLICAR = '--publicar' in sys.argv
FOTO = '../revista-essencia/fontes/equipe/tatila_retrato_2026-10-29.jpg'
IMG = 'img/ihfc-equipe-tatila-argolo.webp'
im = Image.open(FOTO).convert('RGB')  # 961x1440: recorte 4:5 com o rosto no terço de cima (card 140x175)
im.crop((225, 600, 705, 1200)).resize((720, 900), Image.LANCZOS).save(IMG, quality=88)
CARD = '      <div class="pessoa surge"><img src="img/ihfc-equipe-tatila-argolo.webp" alt="Tátila Argolo" loading="lazy"><h3>Tátila Argolo</h3><p>Massoterapeuta</p></div>\n'
ANCORA = '<h3>Natieli Batista</h3>'
TROCAS = [('<small>Gisele · Natieli · Neuza</small>', '<small>Gisele · Natieli · Tátila · Neuza</small>'),
          ('<div class="quem">Sabrina · Gisele · Natieli · Neuza</div>', '<div class="quem">Sabrina · Gisele · Natieli · Tátila · Neuza</div>')]

def aplicar(s):
    if 'Tátila Argolo' in s: return s
    i = s.index(ANCORA); fim = s.index('\n', i) + 1  # card entra logo depois do da Natieli
    s = s[:fim] + CARD + s[fim:]
    for a, b in TROCAS:
        assert a in s, 'trecho não achado: ' + a  # L-328
        s = s.replace(a, b)
    return s

if PUBLICAR:
    novo = aplicar(open('novo.html', encoding='utf-8').read())  # ler antes de abrir para escrita
    open('novo.html', 'w', encoding='utf-8').write(novo)
    subprocess.run([sys.executable, '_trabalho/montar_v5.py'], check=True)
    assert 'Tátila Argolo' in open('index.html', encoding='utf-8').read()
    print('publicado na home')
else:
    shutil.copy('novo.html', '_trabalho/novo.bak'); shutil.copy('index.html', '_trabalho/index.bak')
    try:
        novo = aplicar(open('novo.html', encoding='utf-8').read())  # ler antes de abrir para escrita
        open('novo.html', 'w', encoding='utf-8').write(novo)
        subprocess.run([sys.executable, '_trabalho/montar_v5.py'], check=True)
        h = open('index.html', encoding='utf-8').read()
    finally:
        shutil.move('_trabalho/novo.bak', 'novo.html'); shutil.move('_trabalho/index.bak', 'index.html')
    h = h.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    open('equipe-tatila-previa.html', 'w', encoding='utf-8').write(h)
    print('prévia: equipe-tatila-previa.html')
