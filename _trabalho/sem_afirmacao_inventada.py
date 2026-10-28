"""Correção grave do Dr. (28/10/2026 00h25, L-362): nenhuma afirmação clínica (anestesia, medicação,
técnica, frequência, tempo) sem fonte da clínica ou palavra dele. "Com anestesia local, na maioria das
vezes" era invenção. Segurança cirúrgica = só o que ele disse: consulta pré-cirúrgica, monitorização
completa (eletrocardiograma, pulso, respiração), óxido nitroso na indução e medicação sedativa (sem nomes)."""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SEGURANCA = ('Toda cirurgia segue um protocolo rígido de segurança: consulta pré-cirúrgica antes e, durante o procedimento, '
             'monitorização completa (eletrocardiograma, pulso e respiração), com óxido nitroso na indução e medicação sedativa.')

TROCAS = {
    'procedimentos.html': [
        ('<p class="lead">Feitas com anestesia local, na maioria das vezes, e sempre depois de uma consulta cirúrgica com exames, monitorização e teste alérgico. Cada causa pede uma técnica, por isso a avaliação vem primeiro.',
         f'<p class="lead">{SEGURANCA} Cada caso pede uma técnica, por isso a avaliação vem primeiro.'),
        (', com anestesia local na maioria das vezes.', '.'),
        ('Toda cirurgia começa com uma consulta cirúrgica de cerca de 20 minutos (histórico, medicações, alergias e exames).',
         'Toda cirurgia começa com uma consulta pré-cirúrgica e segue um protocolo rígido de segurança, com monitorização completa durante o procedimento.'),
    ],
    '_trabalho/gerar_frentes.py': [
        ('Toda cirurgia começa com exames, monitorização e teste alérgico.',
         'Consulta pré-cirúrgica antes e, durante a cirurgia, monitorização completa: eletrocardiograma, pulso e respiração.'),
        ('Retira a gordura sob o queixo por microincisões, com anestesia local.', 'Retira a gordura sob o queixo por microincisões.'),
    ],
    'queixas.js': [
        ('"Pequena lipoaspiração sob o queixo, por microincisões e com anestesia local."', '"Pequena lipoaspiração sob o queixo, por microincisões."'),
        ('O plano costuma combinar sustentação imediata e estímulo de colágeno.', 'O plano pode combinar sustentação e estímulo de colágeno, conforme a avaliação.'),
        ('Efeito em poucos dias, com retorno para ajuste.', 'Com retorno para ajuste.'),
        ('"Remove parte das bolas de Bichat por dentro da boca, com anestesia local e sem cicatriz aparente."', '"Remove parte das bolas de Bichat por dentro da boca."'),
        ('"Escultura direta sobre os dentes, em poucas sessões."', '"Escultura direta sobre os dentes."'),
        ('"Cânulas finas por microincisões, com anestesia local, para pequenas áreas de gordura."', '"Cânulas finas por microincisões, para pequenas áreas de gordura."'),
        ('"Retrai os tecidos e estimula colágeno, com recuperação rápida."', '"Retrai os tecidos e estimula colágeno."'),
        ('"Fios da nuca levados para as áreas com falhas, com anestesia local."', '"Fios da nuca levados para as áreas com falhas."'),
        ('com instrumentos esterilizados e, quando preciso, anestesia.', 'com instrumentos esterilizados.'),
        ('"Reduz o inchaço e acelera a recuperação depois de procedimentos."', '"Drenagem no pós-operatório, conforme a orientação de quem fez o procedimento."'),
    ],
}
for arq, lista in TROCAS.items():
    s = open(arq, encoding='utf-8').read()
    for velho, novo in lista:
        assert velho in s or novo in s, f'{arq}: trecho não achado: {velho[:70]}'  # L-328
        s = s.replace(velho, novo)
    open(arq, 'w', encoding='utf-8').write(s); print('ok', arq)
