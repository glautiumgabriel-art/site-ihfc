"""Página "Dúvidas frequentes" com FAQPage (AEO/GEO; perguntas reais dos Reels e anúncios, via MARKETING, 01/11/2026).
Respostas revisadas pelo ChatGPT em 01/11 (_trabalho/faq_revisao_v1.txt; Gemini sem cota) e sem prazo, número ou promessa (L-362).
Base: cabeçalho, contato e rodapé do novo.html. Sem --publicar gera duvidas-previa.html (noindex)."""
import os, sys, re, json, html
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUBLICAR = '--publicar' in sys.argv
FDA = ('FDA: Dermal Fillers', 'https://www.fda.gov/medical-devices/aesthetic-cosmetic-devices/dermal-fillers-soft-tissue-fillers')
FAQ = [
    ('Vou ficar com cara de harmonizada?',
     'O plano parte da anatomia do seu rosto e das suas expectativas. Na avaliação, o profissional explica o que pode mudar, os limites e os riscos de cada opção, antes de qualquer procedimento.', None),
    ('A toxina botulínica vicia?',
     'O efeito da toxina botulínica é temporário: o músculo volta a se mover aos poucos. Repetir a aplicação é uma decisão sua, tomada com avaliação profissional; não existe obrigação de continuar.',
     ('MedlinePlus: OnabotulinumtoxinA', 'https://medlineplus.gov/druginfo/meds/a608013.html')),
    ('Papada só sai com cirurgia?',
     'Nem sempre. A papada pode vir de gordura, de flacidez da pele ou do formato do queixo, e cada causa tem um caminho diferente. A avaliação mostra qual é o seu caso e quais opções fazem sentido.', None),
    ('Melasma tem cura?',
     'O melasma costuma ser persistente e pode voltar. O tratamento ajuda a reduzir as manchas, e a proteção solar diária com acompanhamento ajuda a manter o resultado.',
     ('Academia Americana de Dermatologia: Melasma', 'https://www.aad.org/public/diseases/a-z/melasma-treatment')),
    ('Quanto tempo dura o preenchimento labial?',
     'A duração varia conforme o produto e a região tratada. O ácido hialurônico é absorvido pelo corpo aos poucos, e a necessidade de reaplicar é avaliada caso a caso.', FDA),
    ('Quando o bioestimulador começa a fazer efeito?',
     'O bioestimulador estimula o próprio corpo a produzir colágeno, um processo gradual. A evolução varia conforme o produto e a resposta de cada pessoa, e é acompanhada nos retornos.', FDA),
]
n = open('novo.html', encoding='utf-8').read()
cab = n[:n.index('<section class="hero"')]
contato = n[n.index('<section class="contato"'):]
itens = ''.join(
    f'<details class="faq surge"><summary>{html.escape(p)}</summary><p>{html.escape(r)}</p>'
    + (f'<p class="fonte">Fonte: <a href="{f[1]}" target="_blank" rel="noopener">{html.escape(f[0])}</a></p>' if f else '')
    + '</details>\n' for p, r, f in FAQ)
corpo = (f'<section class="duvidas"><div class="wrap"><span class="eyebrow surge">Dúvidas frequentes</span>'
         f'<h1 class="surge" style="font-size:clamp(2.2rem,6vw,3.6rem)">O que as pacientes <em>mais perguntam</em>.</h1>'
         f'<p class="lead surge" style="max-width:40rem">Respostas curtas. A resposta para o seu caso vem da avaliação presencial.</p>\n{itens}</div></section>\n\n')
schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r, _ in FAQ]}
CSS = ('<style>.duvidas{padding-top:8.5rem}.faq{border-top:1px solid var(--linha);padding:1.1rem 0;max-width:46rem}'
       '.faq summary{cursor:pointer;font-size:1.12rem;color:var(--creme);list-style:none}.faq summary::after{content:" +";color:var(--ouro)}'
       '.faq[open] summary::after{content:" −"}.faq p{margin:.7rem 0 0;color:var(--creme2);line-height:1.6}'
       '.faq .fonte{font-size:.8rem;color:var(--suave)}.faq .fonte a{color:var(--ouro)}</style>\n')
cab = re.sub(r'<title>.*?</title>', '<title>Dúvidas frequentes | IHFC Jequié-BA</title>', cab, count=1, flags=re.S)
cab = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\1https://www.ihfc.com.br/duvidas.html', cab)
cab = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', cab, flags=re.S)
DESC = 'Dúvidas frequentes sobre harmonização facial, toxina botulínica, papada, melasma, preenchimento e bioestimulador no IHFC, em Jequié-BA.'
cab = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + DESC, cab)
cab = cab.replace('<meta property="og:url" content="https://www.ihfc.com.br/">', '<meta property="og:url" content="https://www.ihfc.com.br/duvidas.html">')
cab = re.sub(r'<meta name="robots" content="noindex[^"]*">\n?', '', cab)
cab = cab.replace('</head>', CSS + '<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=1) + '\n</script>\n</head>', 1)
h = cab + corpo + contato
h = re.sub(r'href="#(dores|portas|areas|seguranca|instituto|inicio|equipe|assessores)"', r'href="./#\1"', h)
assert h.count('<details class="faq') == len(FAQ) and 'FAQPage' in h
if PUBLICAR:
    open('duvidas.html', 'w', encoding='utf-8').write(h); print('publicada: duvidas.html')
else:
    h = h.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    open('duvidas-previa.html', 'w', encoding='utf-8').write(h); print('prévia: duvidas-previa.html')
