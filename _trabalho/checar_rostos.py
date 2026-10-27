"""Trava L-325: em todas as páginas, no celular, nenhuma foto de pessoa pode ter algo por cima do rosto.
Para cada foto de pessoa, rola até ela e confere se o ponto do rosto (centro, 30% da altura) é a própria foto."""
import os, sys, pathlib
from playwright.sync_api import sync_playwright
raiz = pathlib.Path(__file__).resolve().parent.parent
paginas = sorted(p.name for p in raiz.glob('*.html'))
SEL = 'img[src*="ihfc-equipe-"], img[src*="glautium"]'
erros = 0
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=1, is_mobile=True, has_touch=True)
    for nome in paginas:
        pg.goto((raiz / nome).as_uri(), wait_until='domcontentloaded', timeout=60000)
        pg.add_style_tag(content='.surge{opacity:1!important;transform:none!important}#topo,.zap{display:none!important}html{scroll-behavior:auto!important}')
        pg.wait_for_timeout(400)
        res = pg.evaluate('''sel => [...document.querySelectorAll(sel)].map(img => {
            if (!img.offsetParent) return null;
            img.scrollIntoView({block: 'center', inline: 'nearest', behavior: 'instant'});
            const r = img.getBoundingClientRect();
            const redonda = getComputedStyle(img).borderRadius.includes('50%');
            // grade de pontos na área do rosto (20–80% da largura, 8–65% da altura)
            for (const fy of [.08, .2, .32, .44, .56, .65]) for (const fx of [.2, .35, .5, .65, .8]) {
                if (redonda && (fx - .5) ** 2 + (fy - .5) ** 2 > .16) continue;  // fora do círculo
                const x = r.left + r.width * fx, y = r.top + r.height * fy;
                if (x < 0 || x > innerWidth || y < 0 || y > innerHeight) continue;  // fora da tela (faixa que arrasta)
                const el = document.elementFromPoint(x, y);
                if (el && el !== img) return img.getAttribute('src') + ' coberto por <' + el.tagName.toLowerCase() + ' ' + (el.className || el.getAttribute('src') || '') + '> em ' + Math.round(fx*100) + '%x' + Math.round(fy*100) + '%';
            }
            return null;
        }).filter(Boolean)''', SEL)
        for r in res:
            print(f'ROSTO COBERTO  {nome}: {r}'); erros += 1
    b.close()
print('ok, nenhum rosto coberto' if not erros else f'{erros} problema(s)')
sys.exit(1 if erros else 0)
