"""29/10/2026, pedido do Dr. (via IMAGEM E AUTORIDADE; fonte _conhecimento/clinica/EQUIPE-IHFC.md): descrição da Natieli."""
import os, sys, subprocess
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOVO = ('Enfermeira e massoterapeuta · feridas (ozonioterapia, laserterapia, PRP e PRF), reposição de vitaminas injetável com a Dra. Ionara, '
        'e cuidado com inflamação e dores')
TROCAS = [('novo.html', '<h3>Natieli Batista</h3><p>Enfermagem, feridas e massoterapia terapêutica</p>', f'<h3>Natieli Batista</h3><p>{NOVO}</p>'),
          ('queixas.js', '"Natieli Batista (enfermagem e massoterapia terapêutica)"', '"Natieli Batista (enfermagem e massoterapia)",\n  tatila: "Tátila Argolo (massoterapia)"'),
          ('queixas.js', '"Massagem modeladora", "Contorno e menos inchaço, como complemento.", [P.natielli]]', '"Massagem modeladora", "Contorno e menos inchaço, como complemento.", [P.natielli, P.tatila]]'),
          ('queixas.js', '"Massagem relaxante", "Velas, pedras quentes e bambu para desacelerar.", [P.natielli]]', '"Massagem relaxante", "Velas, pedras quentes e bambu para desacelerar.", [P.natielli, P.tatila]]'),
          ('queixas.js', '"Massagem modeladora", "Ajuda no contorno e na retenção de líquidos.", [P.natielli]]', '"Massagem modeladora", "Ajuda no contorno e na retenção de líquidos.", [P.natielli, P.tatila]]')]
for arq, a, b in TROCAS:
    s = open(arq, encoding='utf-8').read()  # ler antes de abrir para escrita (L-653)
    if b in s: continue
    assert a in s, 'trecho não achado em ' + arq  # L-328
    open(arq, 'w', encoding='utf-8').write(s.replace(a, b))
subprocess.run([sys.executable, '_trabalho/montar_v5.py'], check=True)
assert '<b>Natieli Batista</b>Enfermeira e massoterapeuta' in open('index.html', encoding='utf-8').read()
print('ok')
