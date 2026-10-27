"""Ajuste do Dr. (27/10/2026): a página inicial apresenta a CLÍNICA e todas as
áreas primeiro; o Dr. Glautium entra como fundador e uma das áreas."""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
h = open('novo.html', encoding='utf-8').read()


def rep(a, b):
    global h
    assert a in h, a[:70]
    h = h.replace(a, b, 1)


# menu: áreas e equipe no lugar do destaque do Dr.
rep('''      <li><a href="procedimentos.html">Procedimentos</a></li>
      <li><a href="dr-glautium.html">Dr. Glautium</a></li>''', '''      <li><a href="#portas">Áreas</a></li>
      <li><a href="#equipe">Equipe</a></li>
      <li><a href="procedimentos.html">Procedimentos</a></li>''')

# topo: a policlínica, sem credencial individual
rep('<span class="eyebrow">Instituto de Harmonização Facial e Corporal · Jequié/BA</span>',
    '<span class="eyebrow">Policlínica · Instituto de Harmonização Facial e Corporal · Jequié/BA</span>')
rep('<p>Rosto, pele, sorriso e corpo cuidados por uma equipe que conversa entre si. Você conta o que te incomoda; a gente monta o caminho junto com você.</p>',
    '<p>Rosto, sorriso, corpo, cabelo, pele e nutrição em um só lugar, com médicos, dentistas e uma equipe que conversa entre si. Você conta o que te incomoda; a gente monta o caminho junto com você.</p>')
rep('<a class="btn btn-linha" href="#dores">Descobrir o que é ideal pra mim</a>',
    '<a class="btn btn-linha" href="#portas">Conhecer as áreas</a>')
rep('''      <div class="credencial"><b>Dr. Glautium Gabriel</b><span>Cirurgião e Traumatologista Bucomaxilofacial · Especialista em Harmonização Orofacial</span><span>CRO-BA 16384</span></div>
''', '''      <nav class="sumario-areas" aria-label="Áreas da clínica"><a href="papada-e-rosto.html">Face</a><a href="corpo.html">Corpo</a><a href="sorriso.html">Sorriso</a><a href="tricologia.html">Cabelo</a><a href="nutricao.html">Nutrição</a><a href="pele.html">Estética</a></nav>
''')

# portas de entrada: uma por área, logo depois do topo
portas = [
    ("papada-e-rosto.html", "img/ihfc-rosto-fino.webp", "Face", "Papada, contorno, rugas, lábios e cirurgias do rosto e do pescoço.", "Dr. Glautium · Dra. Jéssica"),
    ("corpo.html", "img/ihfc-corpo-barriga.webp", "Corpo", "Gordura localizada, flacidez, celulite, vasinhos e emagrecimento acompanhado.", "Dra. Ionara · Dra. Jéssica"),
    ("sorriso.html", "img/ihfc-sorriso.webp", "Sorriso", "Clareamento, lentes, alinhadores, implantes e odontologia para a família.", "Dr. Hudson · Dra. Juliana"),
    ("tricologia.html", "img/ihfc-cabelo.webp", "Cabelo", "Queda de cabelo investigada pela causa e implante capilar.", "Dr. Mateus Brito"),
    ("nutricao.html", "img/ihfc-nutricao.webp", "Nutrição", "Plano alimentar possível para a sua rotina, com bioimpedância.", "Sabrina Amparo"),
    ("pele.html", "img/ihfc-pele-manchas.webp", "Estética", "Limpeza de pele, peelings, manchas, acne e o protocolo Revitalli.", "Maria Eduarda · equipe"),
    ("procedimentos.html#bem-estar", "img/ihfc-bem-estar.webp", "Bem-estar", "Fisioterapia, drenagem, massoterapia e podologia.", "Gisele · Natielli · Neuza"),
]
cards = "".join(f'''      <a class="dor" href="{href}"><img src="{img}" alt="" loading="lazy"><div class="dor-txt"><q>{t}</q><p>{d}</p><small>{q}</small><span class="dor-ver">Conhecer {t.lower()}</span></div></a>
''' for href, img, t, d, q in portas)
rep('<section class="dores" id="dores">', f'''<section id="portas">
  <div class="wrap">
    <span class="eyebrow surge">As áreas do IHFC</span>
    <h2 class="surge">Uma clínica, <em>cuidado completo</em>.</h2>
    <p class="lead surge">Cada área tem os seus profissionais, com registro no conselho de cada profissão. Escolha por onde começar.</p>
    <div class="grade-dores">
{cards}    </div>
  </div>
</section>

<section class="dores" id="dores">''')

# o Dr. como fundador, não como destaque
rep('<span class="eyebrow">O instituto</span>', '<span class="eyebrow">O instituto · fundado pelo Dr. Glautium Gabriel</span>')
rep('<small>Diretor e responsável técnico · ', '<small>Fundador, diretor e responsável técnico · ')

# especialidades: cirurgia buco depois da harmonização
buco = '<div class="area"><h3>Cirurgia bucomaxilofacial</h3><p>Siso e dentes inclusos, implantes e enxertos, trauma de face, ATM, lesões da boca e cirurgias da papada e do pescoço.</p><div class="quem">Dr. Glautium Gabriel</div></div>\n      '
rep(buco, '')
rep('<div class="area"><h3>Pele</h3>', buco + '<div class="area"><h3>Pele</h3>')

open('novo.html', 'w', encoding='utf-8').write(h)
print('ok')
