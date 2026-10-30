"""Página "Sobre o Dr. Glautium" com schema.org Person (pedido 221, 27/10/2026).
Texto-base: _conhecimento/marketing-clinica/autoridade-google/sobre-o-dr_texto-e-schema_v1.md
Mantém a URL dr-glautium.html (já está no menu, nos links e no sitemap). Person, nunca Physician (ele é dentista).
Gera dr-glautium-previa.html (noindex) para aprovação; ao aprovar, rodar com --publicar."""
import os, sys, json, re
PUBLICAR = '--publicar' in sys.argv  # na publicação só entra o que o Dr. já aprovou
from PIL import Image
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
URL = 'https://www.ihfc.com.br/dr-glautium.html'
Image.open('img/ihfc-equipe-glautium-gabriel.webp').convert('RGB').save('img/ihfc-dr-glautium-gabriel_retrato.jpg', quality=88)

FORMACAO = []  # (curso, instituição, ano): só o que o Dr. confirmar
V5 = '--v5' in sys.argv  # na publicação, só com o OK do Dr. na v5
# v5 (28/10 19h): o Dr. reprovou a v4 ("não faz tratamento dentário" sem necessidade; frase sem sentido).
# Nunca dizer o que ele NÃO faz; revisão cruzada ChatGPT + Gemini em _trabalho/revisao-sobre-dr_v5_*.txt (L-nova)
BIO = ("Dr. Glautium Gabriel é Cirurgião e Traumatologista Bucomaxilofacial, Especialista em Harmonização Orofacial "
       "(CRO-BA 16384) e fundador do IHFC, em Jequié-BA. Atua em cirurgias estéticas da face, queiloplastia (correção do "
       "lábio duplo), disfunção temporomandibular (DTM, da articulação da mandíbula), dor na face e na boca (dor orofacial), lesões da boca "
       "e câncer bucal.")
SEGURANCA = ("Consulta pré-cirúrgica e, durante a cirurgia, monitorização completa (eletrocardiograma, pulso e respiração), "
             "com óxido nitroso na indução e medicação sedativa.")
TROCAS_V5 = [
    ('Indicação certa, <em>no paciente certo</em>.', 'Do primeiro contato <em>ao retorno</em>.'),
    ('ele olha o rosto pela estrutura: osso, músculo, gordura e pele. É esse olhar que decide o que fazer, quanto fazer e, às vezes, o que não fazer.', 'ele avalia o rosto pela estrutura: osso, músculo, gordura e pele, e planeja cada caso a partir dela.'),
    (' Sem essa conversa, nada é marcado.', ''),
    ('<div class="proc"><h3>Às vezes a resposta é “não”</h3><p>Se o procedimento não vai entregar o que você procura, ou se outro caminho é melhor, ele diz. Indicar bem vale mais que fazer mais.</p></div>',
     f'<div class="proc"><h3>Nas cirurgias</h3><p>{SEGURANCA}</p></div>'),
    ('O cirurgião bucomaxilofacial estuda a face por dentro. Conhecer onde passam vasos, nervos e camadas é o que dá precisão à harmonização.',
     'O cirurgião bucomaxilofacial estuda a anatomia da face: onde passam vasos, nervos e as camadas do rosto.'),
    ('\n      <div class="proc"><h3>Por etapas</h3><p>Começa com quantidades pequenas, observa como o seu rosto responde e reavalia. Se uma etapa já resolver, não é preciso completar o volume planejado.</p></div>', ''),
    ('<li><b>Lábio duplo</b> ou excesso no lábio que incomoda ao sorrir: a queiloplastia corrige.</li>',
     '<li><b>Lábio duplo</b> que incomoda ao sorrir ou ao falar.</li>'),
    ('<li><b>Dor no rosto ou enxaqueca</b> que piora ao mastigar, ao acordar ou com o ranger dos dentes.</li>',
     '<li><b>Dor no rosto, na mandíbula ou dor de cabeça</b> que piora ao mastigar, ao acordar ou com o ranger dos dentes.</li>'),
    ('que não some em duas semanas: o diagnóstico precoce do câncer bucal faz diferença.</li>', 'que não some em duas semanas.</li>'),
    ('<li><b>Contorno do rosto e do pescoço</b> que pede cirurgia estética da face, como a lipo de papada.</li>',
     '<li><b>Papada e contorno do rosto e do pescoço</b> que incomodam.</li>'),
    ('queiloplastia, DTM e ATM, dor orofacial, bruxismo, biópsias e câncer bucal.', 'queiloplastia, DTM (disfunção da articulação da mandíbula), dor orofacial, bruxismo, biópsias e câncer bucal.'),
]
# v3 (27/10 noite): bio curta da IMAGEM E AUTORIDADE com as palavras do Dr. ("não faço nada relacionado a dente")
# v4 (28/10 00h25): segurança só com as palavras do Dr.; nada de anestesia, tempo ou frequência inventados (L-362)
# bio v2: base da IMAGEM E AUTORIDADE + áreas ditas pelo Dr. em 27/10 ("sou BUCO apenas para cirurgias estéticas da face,
# queiloplastia, lábio duplo, DTM/ATM, câncer bucal, dor/enxaqueca"); aguarda o OK dele junto com esta prévia
AREAS_BUCO = ["Cirurgias estéticas da face", "Queiloplastia (lábio duplo)", "DTM e disfunção da ATM",
              "Dor orofacial", "Câncer bucal"]
# só na prévia: listas da página que contradiziam o que ele disse (siso, trauma, enxerto e ortognática não são com ele)
TROCAS_PREVIA = [
    ('''        <li><b>Dente do siso</b> que dói, inflama ou não tem espaço para nascer.</li>
        <li><b>Batida no rosto</b> (queda, acidente de moto, esporte) com dente mole, sangramento ou dor ao mastigar.</li>
        <li><b>Mandíbula que estala, trava ou sai do lugar</b> ao abrir a boca.</li>
        <li><b>Ferida, caroço ou mancha na boca</b> que não some em duas semanas.</li>
        <li><b>Falta de osso para implante</b>, que pede enxerto ou levantamento de seio.</li>
        <li><b>Mordida e perfil desencaixados</b>, que podem precisar de cirurgia ortognática.</li>''',
     '''        <li><b>Lábio duplo</b> ou excesso no lábio que incomoda ao sorrir: a queiloplastia corrige.</li>
        <li><b>Mandíbula que estala, trava ou dói</b> ao abrir a boca ou mastigar (DTM).</li>
        <li><b>Dor no rosto ou enxaqueca</b> que piora ao mastigar, ao acordar ou com o ranger dos dentes.</li>
        <li><b>Ferida, caroço ou mancha na boca</b> que não some em duas semanas: o diagnóstico precoce do câncer bucal faz diferença.</li>
        <li><b>Contorno do rosto e do pescoço</b> que pede cirurgia estética da face, como a lipo de papada.</li>'''),
    ('<li><b>Boca e face:</b> siso, implantes, enxertos, trauma, ATM, biópsias e bruxismo.</li>',
     '<li><b>Boca e face:</b> queiloplastia, DTM e ATM, dor orofacial, bruxismo, biópsias e câncer bucal.</li>'),
]
SAMEAS = ['https://www.instagram.com/dr.glautiumgabriel/', 'https://www.threads.com/@dr.glautiumgabriel',
          'https://www.doctoralia.com.br/glautium-gabriel/especialista-em-harmonizacao-orofacial/jequie']  # confirmados no rastreamento de 27/10  # outros perfis entram quando confirmados

pessoa = {
    "@context": "https://schema.org", "@type": "Person", "@id": URL + "#pessoa",
    "name": "Glautium Gabriel", "honorificPrefix": "Dr.",
    "jobTitle": "Cirurgião e Traumatologista Bucomaxilofacial e Especialista em Harmonização Orofacial",
    "url": URL, "image": "https://www.ihfc.com.br/img/ihfc-dr-glautium-gabriel_retrato.jpg",
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Registro profissional",
                      "name": "CRO-BA 16384", "recognizedBy": {"@type": "Organization", "name": "Conselho Regional de Odontologia da Bahia"}},
    "knowsAbout": ["Cirurgia Bucomaxilofacial", "Cirurgia estética da face", "Queiloplastia",
                   "Disfunção temporomandibular (ATM/DTM)", "Câncer bucal", "Harmonização Orofacial", "Endolaser facial"],  # sem dente (Dr., 27/10)
    "worksFor": {"@type": ["Dentist", "MedicalClinic"], "@id": "https://www.ihfc.com.br/#clinica",
                 "name": "IHFC · Instituto de Harmonização Facial e Corporal", "url": "https://www.ihfc.com.br/",
                 "telephone": "+55-73-98150-7715",
                 "address": {"@type": "PostalAddress", "streetAddress": "R. Dr. João Braga, 640, Jequiezinho", "postalCode": "45208-201",
                             "addressLocality": "Jequié", "addressRegion": "BA", "addressCountry": "BR"}},
    "sameAs": SAMEAS,
}
if not PUBLICAR or V5:  # bio e áreas: aprovadas pelo Dr. na v5 (29/10 00h)
    pessoa["description"] = BIO
    pessoa["knowsAbout"] = ["Cirurgia Bucomaxilofacial", "Cirurgia estética da face", "Queiloplastia",
                            "Disfunção temporomandibular (ATM/DTM)", "Dor orofacial", "Câncer bucal",
                            "Harmonização Orofacial", "Endolaser facial"]  # lista da IMAGEM + câncer e dor, ditos pelo Dr.
if FORMACAO:
    pessoa["alumniOf"] = [{"@type": "CollegeOrUniversity", "name": i} for _, i, _ in FORMACAO]

h = open('dr-glautium.html', encoding='utf-8').read()
h = h.replace('<title>Dr. Glautium Gabriel · IHFC Jequié</title>',
              '<title>Dr. Glautium Gabriel | Bucomaxilofacial e Harmonização Orofacial em Jequié-BA</title>')
h = h.replace('diretor e responsável técnico do IHFC em Jequié/BA.">', 'fundador, diretor e responsável técnico do IHFC em Jequié/BA.">')
h = h.replace('"https://www.ihfc.com.br/img/ihfc-compartilhar-1200x630.jpg">', '"https://www.ihfc.com.br/img/ihfc-dr-glautium-gabriel_retrato.jpg">', 1)
h = h.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="profile">')
h = h.replace('<span class="eyebrow">Diretor e responsável técnico do IHFC</span>', '<span class="eyebrow">Fundador, diretor e responsável técnico do IHFC</span>')
h = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', h, flags=re.S)  # sempre a versão atual do schema
h = h.replace('</head>', '<script type="application/ld+json">\n' + json.dumps(pessoa, ensure_ascii=False, indent=1) + '\n</script>\n</head>', 1)
if True:  # correção do Dr. ("não faço nada relacionado a dente"): vale também na página publicada
    for velho, novo in TROCAS_PREVIA:
        assert velho in h or novo in h, 'trecho não achado: ' + velho[:60]  # L-328: nunca seguir calado
        h = h.replace(velho, novo)
if not PUBLICAR or V5:
    for velho, novo in TROCAS_V5:
        assert velho in h or (novo and novo in h), 'v5: trecho não achado: ' + velho[:60]  # L-328
        h = h.replace(velho, novo)
    assert 'não faz' not in h and 'às vezes' not in h.lower(), 'v5: ainda diz o que ele não faz'
if (not PUBLICAR or V5) and 'class="bio-dr"' not in h:
    h = h.replace('<section class="seguranca">', f'<section class="bio-dr" style="padding-bottom:0"><div class="wrap"><span class="eyebrow surge">Sobre</span><p class="lead surge" style="max-width:44rem">{BIO}</p></div></section>\n\n<section class="seguranca">', 1)
if FORMACAO and 'id="formacao"' not in h:
    itens = ''.join(f'<li><b>{c}</b>{i}, {a}</li>' for c, i, a in FORMACAO)
    h = h.replace('<section class="seguranca">', f'<section id="formacao"><div class="wrap"><span class="eyebrow surge">Formação</span><h2 class="surge">Onde ele <em>se formou</em>.</h2><ul class="lista-espaco surge">{itens}</ul></div></section>\n\n<section class="seguranca">', 1)

if '--publicar' in sys.argv:
    open('dr-glautium.html', 'w', encoding='utf-8').write(h.replace('<meta name="robots" content="noindex">\n', ''))
    print('publicada: dr-glautium.html sem noindex')
else:
    if 'noindex' not in h:  # prévia tem a bio ainda não aprovada: fora do Google
        h = h.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    open('dr-glautium-previa.html', 'w', encoding='utf-8').write(h)
    print('prévia: dr-glautium-previa.html')
