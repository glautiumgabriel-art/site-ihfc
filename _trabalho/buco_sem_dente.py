"""Correção do Dr. (27/10/2026): "só trabalho como buco nas cirurgias estéticas da face / câncer /
disfunção ATM / DTM, não faço nada relacionado a dente; queiloplastia eu faço".
Tira do site tudo que ligava o Dr. Glautium a tratamento dentário (siso, implante, trauma dental, ortognática)."""
import os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def trocar(arq, velho, novo, regex=False):
    s = open(arq, encoding='utf-8').read()
    n = re.subn(velho, novo, s, flags=re.S) if regex else (s.replace(velho, novo), s.count(velho))
    assert n[1] or novo in s, f'{arq}: trecho não achado: {velho[:60]}'  # L-328
    open(arq, 'w', encoding='utf-8').write(n[0])

# 1) procedimentos: a seção de bucomaxilo só com o que é dele
trocar('procedimentos.html',
       '<p class="lead">O cirurgião bucomaxilofacial cuida dos ossos, dos dentes e dos tecidos da boca e da face. É a formação que trata dente do siso, fraturas do rosto, a articulação da mandíbula e lesões da boca.</p>',
       '<p class="lead">O cirurgião bucomaxilofacial conhece a fundo os ossos, os músculos e os tecidos da face. No IHFC, o Dr. Glautium atua nas cirurgias estéticas da face, na articulação da mandíbula e nas lesões da boca. Ele não faz tratamentos dentários: siso, implantes e cuidados com os dentes ficam com a <a href="sorriso.html">equipe de odontologia</a>.</p>')
trocar('procedimentos.html', r'(<div class="procs">)\s*<div class="proc"><h3>Dente do siso e inclusos</h3>.*?<h3>Cirurgia ortognática</h3><p>[^<]*</p></div>',
       r'''\1
      <div class="proc"><h3>Cirurgias estéticas da face</h3><p>Lipo de papada, cervicoplastia, platismoplastia, bichectomia, lip lift e mentoplastia, com anestesia local na maioria das vezes. <a href="#cirurgias-face">Ver todas</a>.</p></div>
      <div class="proc"><h3>Queiloplastia</h3><p>Corrige o lábio duplo e o excesso de tecido no lábio que aparece ao sorrir ou ao falar.</p></div>
      <div class="proc"><h3>DTM e disfunção da ATM</h3><p>Mandíbula que estala, trava, sai do lugar ou dói ao mastigar, além da dor no rosto e da enxaqueca ligadas à articulação.</p></div>
      <div class="proc"><h3>Lesões da boca e câncer bucal</h3><p>Investigação de feridas, caroços e manchas na boca, no lábio e na língua, com biópsia quando indicado. O diagnóstico cedo do câncer bucal faz diferença.</p></div>
      <div class="proc"><h3>Bruxismo</h3><p>Ranger e apertar os dentes cansa o músculo e dói. A toxina botulínica no masseter relaxa o músculo e alivia a dor.</p></div>''', regex=True)
trocar('procedimentos.html', 'Urgência de trauma ou dor forte? Chame no WhatsApp para orientação.', 'Dor forte na mandíbula ou no rosto? Chame no WhatsApp para orientação.')

# 2) página de implante (gerada): o Dr. sai; extração/siso fica com a odontologia
trocar('_trabalho/gerar_frentes.py', '("Extrações e siso", "Com o cirurgião bucomaxilofacial.")', '("Extrações e siso", "Com a equipe de odontologia.")')
trocar('_trabalho/gerar_frentes.py', r'quem=\[\("img/ihfc-equipe-glautium-gabriel\.webp", "Dr\. Glautium Gabriel", "Cirurgia bucomaxilofacial, enxertos e implantes", "CRO-BA 16384"\),\s*', 'quem=[', regex=True)
print('ok')
