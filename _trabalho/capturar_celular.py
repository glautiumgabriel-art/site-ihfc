"""Fotografa uma página do site inteira, em tamanho de iPhone, para a página de aprovações do Dr."""
import sys, os
from playwright.sync_api import sync_playwright
pagina, saida = sys.argv[1], sys.argv[2]
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg.goto(__import__('pathlib').Path(raiz, pagina).as_uri())
    pg.add_style_tag(content='.zap{display:none!important}')
    pg.wait_for_timeout(2500)
    larg = pg.evaluate('document.documentElement.scrollWidth')
    pg.screenshot(path=saida, full_page=True, type='jpeg', quality=86)
    print('largura', larg, 'ok', saida)
    b.close()
