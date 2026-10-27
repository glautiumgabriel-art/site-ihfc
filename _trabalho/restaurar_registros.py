"""27/10/2026 19h: registros confirmados pelo Dr. voltam ao site (Mateus segue sem número)."""
import os, re, glob
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = {'Dra. Ionara Caroso': 'CRM-BA 16679', 'Dra. Juliana Coelho Moreno': 'CRO-BA 27601',
       'Dr. Hudson D. Soares': 'CRO-BA 23283', 'Sabrina Amparo': 'CRN-5 20406', 'Dra. Jéssica Lopes': 'CRBM 42499'}
for a in glob.glob('*.html') + ['queixas.js', '_trabalho/gerar_frentes.py']:
    s = open(a, encoding='utf-8').read(); o = s
    for nome, r in REG.items():
        s = re.sub(rf'(<h3>{re.escape(nome)}</h3><p>[^<]*</p>)(?!<span>)', rf'\1<span>{r}</span>', s)
        s = re.sub(rf'("{re.escape(nome)}", "[^"]*", )""\)', rf'\1"{r}")', s)
    s = s.replace('<h3>Natieli Batista</h3><p>Enfermeira</p>', '<h3>Natieli Batista</h3><p>Enfermagem, feridas e massoterapia terapêutica</p>')
    s = s.replace('Natieli Batista (massoterapia)', 'Natieli Batista (enfermagem e massoterapia terapêutica)')
    if s != o: open(a, 'w', encoding='utf-8').write(s); print('ok', a)
