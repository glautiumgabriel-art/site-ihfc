"""Correção 27/10/2026 (L-318): nome, registro e foto de profissional só valem se vieram
do Dr., da própria pessoa ou do Simples Dental. O que veio de busca na web sai do site.
Origem de cada dado: _trabalho/equipe-origem-dos-dados_2026-10-27.md"""
import os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# registros sem fonte válida (web ou sem origem anotada) e o do "Dr. Mateus" errado
TIRAR = ['CRM-BA 49804', 'CRM-BA 16679', 'CRO-BA 23283', 'CRO-BA 27601', 'CRN-5 20406', 'CRBM 15493']

arqs = [f for f in os.listdir('.') if f.endswith(('.html', '.js'))]
arqs += ['_trabalho/gerar_frentes.py', '_trabalho/inicio_policlinica.py']
for a in arqs:
    s = open(a, encoding='utf-8').read(); o = s
    for r in TIRAR:
        s = s.replace(f'<span>{r}</span>', '').replace(f' · {r}', '').replace(f', "{r}")', ', "")').replace(f'"{r}"', '""')
    s = s.replace('img/ihfc-equipe-mateus-brito.webp', 'img/ihfc-equipe-dr-mateus.webp')
    s = re.sub(r'Dr\. Mateus (Silva )?Brito', 'Dr. Mateus', s)
    s = s.replace('Natielli', 'Natieli')  # grafia do Simples Dental
    if s != o:
        open(a, 'w', encoding='utf-8').write(s); print('ok', a)
