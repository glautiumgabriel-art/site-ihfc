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
BIO = ("Dr. Glautium Gabriel é Cirurgião e Traumatologista Bucomaxilofacial e Especialista em Harmonização Orofacial "
       "(CRO-BA 16384) e fundador do IHFC, em Jequié-BA. Atende com avaliação antes de qualquer procedimento: examina a face "
       "como um todo, explica o que faz sentido para cada caso, o que não faz e os riscos, e acompanha o paciente depois.")
# bio: IMAGEM E AUTORIDADE, 27/10 (dados confirmados; texto aguarda o OK do Dr. junto com esta prévia)
SAMEAS = ['https://www.instagram.com/dr.glautiumgabriel/', 'https://www.threads.com/@dr.glautiumgabriel',
          'https://www.doctoralia.com.br/glautium-gabriel/especialista-em-harmonizacao-orofacial/jequie']  # confirmados no rastreamento de 27/10  # outros perfis entram quando confirmados

pessoa = {
    "@context": "https://schema.org", "@type": "Person", "@id": URL + "#pessoa",
    "name": "Glautium Gabriel", "honorificPrefix": "Dr.",
    "jobTitle": "Cirurgião e Traumatologista Bucomaxilofacial e Especialista em Harmonização Orofacial",
    "url": URL, "image": "https://www.ihfc.com.br/img/ihfc-dr-glautium-gabriel_retrato.jpg",
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Registro profissional",
                      "name": "CRO-BA 16384", "recognizedBy": {"@type": "Organization", "name": "Conselho Regional de Odontologia da Bahia"}},
    "knowsAbout": ["Cirurgia e Traumatologia Bucomaxilofacial", "Harmonização Orofacial", "Endolaser facial", "Lipo de papada", "Implantes dentários"],
    "worksFor": {"@type": ["Dentist", "MedicalClinic"], "@id": "https://www.ihfc.com.br/#clinica",
                 "name": "IHFC · Instituto de Harmonização Facial e Corporal", "url": "https://www.ihfc.com.br/",
                 "telephone": "+55-73-98150-7715",
                 "address": {"@type": "PostalAddress", "streetAddress": "R. Dr. João Braga, 640, Jequiezinho",
                             "addressLocality": "Jequié", "addressRegion": "BA", "addressCountry": "BR"}},
    "sameAs": SAMEAS,
}
if not PUBLICAR:  # bio ainda aguarda o OK do Dr.
    pessoa["description"] = BIO
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
if not PUBLICAR and 'class="bio-dr"' not in h:
    h = h.replace('<section class="seguranca">', f'<section class="bio-dr" style="padding-bottom:0"><div class="wrap"><span class="eyebrow surge">Sobre</span><p class="lead surge" style="max-width:44rem">{BIO}</p></div></section>\n\n<section class="seguranca">', 1)
if FORMACAO and 'id="formacao"' not in h:
    itens = ''.join(f'<li><b>{c}</b>{i}, {a}</li>' for c, i, a in FORMACAO)
    h = h.replace('<section class="seguranca">', f'<section id="formacao"><div class="wrap"><span class="eyebrow surge">Formação</span><h2 class="surge">Onde ele <em>se formou</em>.</h2><ul class="lista-espaco surge">{itens}</ul></div></section>\n\n<section class="seguranca">', 1)

if '--publicar' in sys.argv:
    open('dr-glautium.html', 'w', encoding='utf-8').write(h.replace('<meta name="robots" content="noindex">\n', ''))
    print('publicada: dr-glautium.html sem noindex')
else:
    open('dr-glautium-previa.html', 'w', encoding='utf-8').write(h)
    print('prévia: dr-glautium-previa.html')
