"""Seção "Assessores e Equipe" (pedido do Dr., 27/10/2026 21h50): gestão e equipe de apoio
ficam fora dos cartões de profissionais. Foto que ainda não chegou = cartão com as iniciais.
Para pôr uma foto: salvar em img/ihfc-equipe-<id>.webp e rodar de novo (depois montar_v5.py)."""
import os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EQUIPE = [  # (id da foto, nome, função)
    ('jaiane-santos', 'Jaiane Santos', 'Gestora em saúde pública e privada · MBA em sistema gerencial e organizacional'),
    ('luisa', 'Luísa', 'Recepção'),
    ('sara', 'Sara', 'Financeiro'),
    ('suely', 'Suely', 'Equipe IHFC'),
    ('poliana', 'Poliana', 'Comunicação'),
]

def cartao(i, nome, funcao):
    foto = f'img/ihfc-equipe-{i}.webp'
    if os.path.exists(foto):
        rosto = f'<img src="{foto}" alt="{nome}" loading="lazy">'
    else:
        rosto = f'<span class="inicial" aria-hidden="true">{"".join(p[0] for p in nome.split()[:2])}</span>'
    return f'<div class="apoio-pessoa">{rosto}<h3>{nome}</h3><p>{funcao}</p></div>'

secao = ('<section class="assessores" id="assessores">\n  <div class="wrap">\n'
         '    <span class="eyebrow surge">Assessores e Equipe</span>\n'
         '    <h2 class="surge">Quem faz <em>tudo funcionar</em>.</h2>\n'
         '    <div class="apoio-grade surge">' + ''.join(cartao(*e) for e in EQUIPE) + '</div>\n'
         '  </div>\n</section>\n')

for a in ['index.html', 'novo.html']:
    s = open(a, encoding='utf-8').read()
    s = re.sub(r'\s*<div class="pessoa surge"><img src="img/ihfc-equipe-jaiane-santos\.webp".*?</div>', '', s)  # sai dos profissionais
    s = re.sub(r'\s*<p class="apoio surge">.*?</p>', '', s)
    s = re.sub(r'<section class="assessores" id="assessores">.*?</section>\n', '', s, flags=re.S)
    fim_equipe = s.index('</section>', s.index('<section class="equipe" id="equipe">')) + len('</section>\n')
    s = s[:fim_equipe] + '\n' + secao + s[fim_equipe:]
    open(a, 'w', encoding='utf-8').write(s); print('ok', a)
