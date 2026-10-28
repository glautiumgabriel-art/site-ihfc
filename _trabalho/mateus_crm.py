"""28/10/2026: Jaiane confirmou o nome completo e o registro (via ORACULO): Dr. Mateus Silva Brito, CRM-BA 49804."""
import os, re, glob
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOME, REG = 'Dr. Mateus Silva Brito', 'CRM-BA 49804'
for a in glob.glob('*.html') + ['queixas.js', '_trabalho/gerar_frentes.py']:
    s = open(a, encoding='utf-8').read(); o = s
    s = s.replace('alt="Dr. Mateus"', f'alt="{NOME}"').replace('<h3>Dr. Mateus</h3>', f'<h3>{NOME}</h3>')
    s = re.sub(rf'(<h3>{re.escape(NOME)}</h3><p>[^<]*</p>)(?!<span>)', rf'\1<span>{REG}</span>', s)
    s = s.replace('"Dr. Mateus", "Tricologia e implante capilar", ""', f'"{NOME}", "Tricologia e implante capilar", "{REG}"')
    s = s.replace('<div class="quem">Dr. Mateus</div>', f'<div class="quem">{NOME}</div>')
    s = s.replace('"Dr. Mateus (tricologia)"', f'"{NOME} (tricologia)"')
    if s != o: open(a, 'w', encoding='utf-8').write(s); print('ok', a)
