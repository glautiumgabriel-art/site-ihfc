"""Auditoria 27/10/2026: prévia de link (WhatsApp/Facebook) com imagem JPG 1200x630,
URL absoluta, og:url e canonical em todas as páginas."""
import os, re
from PIL import Image, ImageDraw, ImageFilter
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = 'https://www.ihfc.com.br/'

# imagem de compartilhamento: fachada escurecida + logo
im = Image.open('img/ihfc-fachada.webp').convert('RGB')
w, h = im.size; alvo = 1200 / 630
if w / h > alvo:
    nw = int(h * alvo); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
else:
    nh = int(w / alvo); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
im = im.resize((1200, 630), Image.LANCZOS)
sombra = Image.new('RGB', im.size, (14, 12, 10))
masc = Image.new('L', im.size)  # escuro à esquerda, foto aparecendo à direita
masc.putdata([int(235 * max(0, 1 - x / 760) ** .8) + 25 for y in range(630) for x in range(1200)])
im = Image.composite(sombra, im, masc)
logo = Image.open('img/ihfc-logo-branco.png').convert('RGBA')
logo.thumbnail((420, 200))
im.paste(logo, (70, (630 - logo.height) // 2), logo)
im.save('img/ihfc-compartilhar-1200x630.jpg', quality=86, optimize=True)

def ajustar(p, s):
    url = BASE if p in ('index.html',) else BASE + p
    s = re.sub(r'<meta property="og:image" content="(?!http)([^"]+)">',
               lambda m: f'<meta property="og:image" content="{BASE}{m.group(1) if m.group(1).endswith(".jpg") else "img/ihfc-compartilhar-1200x630.jpg"}">', s)
    if 'og:image' not in s:
        s = s.replace('<link rel="icon"', f'<meta property="og:title" content="IHFC Jequié">\n<meta property="og:image" content="{BASE}img/ihfc-compartilhar-1200x630.jpg">\n<link rel="icon"', 1)
    if 'og:url' not in s:
        s = s.replace('<meta property="og:image"', f'<meta property="og:url" content="{url}">\n<meta property="og:type" content="website">\n<meta property="og:locale" content="pt_BR">\n<meta property="og:image"', 1)
    if 'rel="canonical"' not in s:
        s = s.replace('<link rel="icon"', f'<link rel="canonical" href="{url}">\n<link rel="icon"', 1)
    return s

for p in sorted(f for f in os.listdir('.') if f.endswith('.html')):
    s = open(p, encoding='utf-8').read(); n = ajustar(p, s)
    if n != s: open(p, 'w', encoding='utf-8').write(n); print('ok', p)
