"""Fotografa uma página do site inteira, em tamanho de iPhone, para a página de aprovações do Dr."""
import sys, os
from playwright.sync_api import sync_playwright
pagina, saida = sys.argv[1], sys.argv[2]
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg.goto(pagina if pagina.startswith('http') else __import__('pathlib').Path(raiz, pagina).as_uri(), wait_until='domcontentloaded', timeout=60000)
    pg.evaluate('Promise.race([document.fonts.ready, new Promise(r=>setTimeout(r,8000))])')
    pg.add_style_tag(content='.zap{display:none!important}.surge{opacity:1!important;transform:none!important}html{scroll-behavior:auto!important}')
    pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}scrollTo(0,0)}')  # carrega as fotos lazy
    pg.wait_for_timeout(2500)
    larg = pg.evaluate('document.documentElement.scrollWidth')
    pg.screenshot(path=saida, full_page=True, type='jpeg', quality=86)
    print('largura', larg, 'ok', saida)
    b.close()
