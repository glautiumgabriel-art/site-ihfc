"""Gera uma página por frente do IHFC (pedido do Marketing, 27/10/2026).
Cada página: dor, o que é feito, quem faz, WhatsApp com PALAVRA-CHAVE (o robô
sabe de onde veio a paciente) e ponte para outra frente. Sem preço; CFO/CFM.
Rodar: python _trabalho/gerar_frentes.py (de dentro de _clinica/site-ihfc)."""
import os
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZAP = "5573981507715"


def zap(chave, texto):
    return f"https://wa.me/{ZAP}?text=" + quote(f"{chave} - Olá! Vim pelo site. {texto}")


FRENTES = [
    dict(arq="papada-e-rosto.html", chave="PAPADA", menu="Papada e rosto",
         titulo="Papada e rosto", h1="Papada, contorno e rosto caindo: <em>cada causa tem uma técnica</em>.",
         dor="Papada que não sai com dieta, rosto que parece mais pesado, olhar cansado. Antes de escolher o procedimento, o Dr. Glautium descobre se o problema é gordura, pele, músculo ou osso.",
         foto="img/ihfc-papada-contorno.webp",
         itens=[("Lipo de papada", "Retira a gordura sob o queixo por microincisões, com anestesia local."),
                ("Platismoplastia e cervicoplastia", "Tratam as bandas do músculo e o excesso de pele do pescoço."),
                ("Enzimas e Endolaser", "Caminhos sem cirurgia para gordura e flacidez leves, conforme a avaliação."),
                ("Bichectomia e lip lift", "Contorno das bochechas e elevação do lábio superior, com cicatriz escondida."),
                ("Harmonização natural", "Toxina, ácido hialurônico, bioestimuladores e fios, por etapas, sem exagero."),
                ("Consulta cirúrgica", "Toda cirurgia começa com exames, monitorização e teste alérgico.")],
         quem=[("img/ihfc-equipe-glautium-gabriel.webp", "Dr. Glautium Gabriel", "Cirurgião e Traumatologista Bucomaxilofacial - Especialista em Harmonização Orofacial", "CRO-BA 16384")],
         botao="Quero avaliar minha papada ou rosto", texto="Quero uma avaliação de papada/rosto com o Dr. Glautium.",
         ponte=[("pele.html", "Pele"), ("sorriso.html", "Sorriso"), ("nutricao.html", "Nutrição")]),
    dict(arq="sorriso.html", chave="SORRISO", menu="Sorriso",
         titulo="Sorriso", h1="Vergonha de sorrir <em>tem solução</em>.",
         dor="Dentes amarelados, desalinhados, com espaços ou gengiva aparecendo demais. A odontologia do IHFC planeja o sorriso junto com o rosto.",
         foto="img/ihfc-sorriso.webp",
         itens=[("Clareamento", "No consultório ou em casa, com acompanhamento."),
                ("Lentes e facetas", "Em resina ou cerâmica, e fechamento de espaços entre os dentes."),
                ("Alinhadores e aparelhos", "Para alinhar os dentes e a mordida."),
                ("Gengivas", "Correção do sorriso gengival."),
                ("Tratamentos do dia a dia", "Limpeza, restaurações e canal."),
                ("Crianças", "Odontopediatria com calma e no tempo delas.")],
         quem=[("img/ihfc-equipe-hudson-soares.webp", "Dr. Hudson D. Soares", "Implantes, estética e reabilitação oral", ""),
               ("img/ihfc-equipe-juliana.webp", "Dra. Juliana Coelho Moreno", "Implantes, estética dental e atendimento infantil", "")],
         botao="Quero avaliar meu sorriso", texto="Quero uma avaliação do sorriso.",
         ponte=[("implante.html", "Implante"), ("papada-e-rosto.html", "Harmonização"), ("pele.html", "Pele")]),
    dict(arq="implante.html", chave="IMPLANTE", menu="Implante",
         titulo="Implantes dentários", h1="Voltar a mastigar e a sorrir <em>com segurança</em>.",
         dor="Falta de dente, prótese que machuca ou solta, osso que diminuiu depois de uma extração. O implante começa pelo planejamento por imagem e pela avaliação cirúrgica.",
         foto="img/ihfc-planejamento.webp",
         itens=[("Implantes", "Planejados por imagem, com guia cirúrgico quando indicado."),
                ("Enxerto ósseo", "Quando falta osso para o implante."),
                ("Levantamento de seio", "Ganho de osso na região de cima, atrás."),
                ("Prótese sobre implante", "Unitária ou protocolo, fixa no implante."),
                ("Próteses", "Fixas, removíveis e totais."),
                ("Extrações e siso", "Com o cirurgião bucomaxilofacial.")],
         quem=[("img/ihfc-equipe-glautium-gabriel.webp", "Dr. Glautium Gabriel", "Cirurgia bucomaxilofacial, enxertos e implantes", "CRO-BA 16384"),
               ("img/ihfc-equipe-hudson-soares.webp", "Dr. Hudson D. Soares", "Implantes e reabilitação oral", ""),
               ("img/ihfc-equipe-juliana.webp", "Dra. Juliana Coelho Moreno", "Implantes e estética dental", "")],
         botao="Quero avaliar um implante", texto="Quero uma avaliação de implante.",
         ponte=[("sorriso.html", "Sorriso"), ("papada-e-rosto.html", "Rosto")]),
    dict(arq="corpo.html", chave="CORPO", menu="Corpo",
         titulo="Corpo", h1="Barriga que não sai com dieta <em>tem causa</em>.",
         dor="Gordura localizada, flacidez, celulite, vasinhos. Cada queixa tem o seu caminho, do tratamento sem cortes ao procedimento médico, com avaliação e bioimpedância.",
         foto="img/ihfc-corpo-barriga.webp",
         itens=[("Gordura localizada", "Enzimas, criolipólise, Endolaser corporal, hidrolipo e ultracavitação."),
                ("Bumbum e celulite", "Subcisão, bioestimuladores e protocolos de firmeza."),
                ("Vasinhos", "Escleroterapia (PEIM) com avaliação antes."),
                ("Emagrecimento acompanhado", "Plano com médica e nutricionista; medicação só com prescrição."),
                ("Suor excessivo", "Toxina para axilas e mãos."),
                ("Drenagem e fisioterapia", "Para recuperar melhor e potencializar o tratamento.")],
         quem=[("img/ihfc-equipe-ionara-caroso.webp", "Dra. Ionara Caroso", "Médica · estética, corpo e dermatologia", ""),
               ("img/ihfc-equipe-jessica-lopes.webp", "Dra. Jéssica Lopes", "Biomédica esteta · bioestimuladores e microvasos", ""),
               ("img/ihfc-equipe-gisele.webp", "Gisele Gomes", "Fisioterapeuta", "CREFITO-7 441870-F")],
         botao="Quero uma avaliação corporal", texto="Quero uma avaliação corporal.",
         ponte=[("nutricao.html", "Nutrição"), ("pele.html", "Pele")]),
    dict(arq="tricologia.html", chave="CABELO", menu="Cabelo",
         titulo="Tricologia · queda de cabelo", h1="Queda de cabelo tem causa. <em>E tem tratamento.</em>",
         dor="Fios caindo no travesseiro, entradas, couro cabeludo aparecendo. A tricologia é a área da medicina que investiga o porquê da queda (hormônios, vitaminas, estresse, couro cabeludo) antes de tratar.",
         foto="img/ihfc-cabelo-implante.webp",
         itens=[("Consulta tricológica", "Conversa, exame do couro cabeludo e, quando preciso, exames de sangue para achar a causa."),
                ("Tratamento clínico", "Plano conforme o diagnóstico, com acompanhamento."),
                ("PRP e microagulhamento capilar", "Estimulam os fios a partir do couro cabeludo, em sessões."),
                ("Laser e LED capilar", "Protocolos de apoio para fortalecer o fio."),
                ("Implante capilar", "Para áreas sem fio, depois da avaliação da área doadora."),
                ("Acompanhamento", "Retornos para medir a resposta e ajustar o plano.")],
         quem=[("img/ihfc-equipe-dr-mateus.webp", "Dr. Mateus", "Tricologia e implante capilar", "")],
         botao="Entrar na lista de espera", texto="Quero entrar na lista de espera da Tricologia com o Dr. Mateus.",
         extra="As vagas da Tricologia estão abrindo agora. Entre na lista de espera e a equipe te chama assim que houver horário.",
         ponte=[("nutricao.html", "Nutrição"), ("papada-e-rosto.html", "Rosto")]),
    dict(arq="nutricao.html", chave="NUTRI", menu="Nutrição",
         titulo="Nutrição", h1="Comer bem <em>sem sofrer</em>.",
         dor="Dieta que não se sustenta, inchaço, cansaço, preparo para cirurgia ou recuperação. A nutrição monta um plano possível para a sua rotina, com bioimpedância.",
         foto="img/ihfc-nutricao.webp",
         itens=[("Consulta e plano alimentar", "Feito para a sua rotina, sem promessa de número na balança."),
                ("Bioimpedância", "Mede gordura, músculo e água para acompanhar a evolução."),
                ("Preparo para cirurgia", "Chegar bem e recuperar melhor."),
                ("Apoio a outros tratamentos", "Corpo, pele e queda de cabelo também dependem da alimentação.")],
         quem=[("img/ihfc-equipe-sabrina-amparo.webp", "Sabrina Amparo", "Nutricionista", "")],
         botao="Quero agendar com a nutricionista", texto="Quero agendar uma consulta de nutrição.",
         ponte=[("corpo.html", "Corpo"), ("tricologia.html", "Cabelo")]),
    dict(arq="pele.html", chave="PELE", menu="Pele",
         titulo="Pele", h1="Manchas, acne e pele sem viço: <em>começa pela causa</em>.",
         dor="Melasma que volta, cicatriz de acne, cravos, pele opaca. O cuidado da pele combina tratamento no consultório e rotina em casa.",
         foto="img/ihfc-pele-manchas.webp",
         itens=[("Limpeza de pele", "Remove impurezas e prepara a pele para os outros tratamentos."),
                ("Peelings", "Do suave ao profundo, para manchas, textura e acne."),
                ("Microagulhamento", "Estimula colágeno e melhora cicatrizes."),
                ("Revitalli", "Protocolo próprio do IHFC para melasma, manchas e cicatrizes de acne."),
                ("Skinbooster", "Hidratação profunda do rosto, do pescoço e das mãos."),
                ("Tecnologias", "Ultrassom microfocado, radiofrequência e laser, conforme a avaliação.")],
         quem=[("img/ihfc-equipe-maria-eduarda-brisola.webp", "Maria Eduarda Brisola", "Esteticista · limpeza de pele, peeling e microagulhamento", ""),
               ("img/ihfc-equipe-glautium-gabriel.webp", "Dr. Glautium Gabriel", "Protocolo Revitalli e harmonização", "CRO-BA 16384"),
               ("img/ihfc-equipe-ionara-caroso.webp", "Dra. Ionara Caroso", "Dermatologia", "")],
         botao="Quero cuidar da minha pele", texto="Quero uma avaliação da pele.",
         ponte=[("papada-e-rosto.html", "Rosto"), ("nutricao.html", "Nutrição")]),
]

ICONE_ZAP = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.4 14.1c-.2.6-1.3 1.2-1.8 1.3-.5 0-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8 0-1.4.7-2 1-2.3.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.4.6-.3.4c-.1.1-.3.3-.1.5.2.3.7 1.2 1.6 2 1.1.9 2 1.2 2.3 1.4.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/></svg>'


def menu(ativo):
    lis = "".join(f'<li><a{" class=\"ativo\"" if f["arq"] == ativo else ""} href="{f["arq"]}">{f["menu"]}</a></li>' for f in FRENTES)
    return lis + '<li><a href="procedimentos.html">Todos</a></li><li class="sempre"><a href="cursos.html">Cursos</a></li>'


def pagina(f):
    link = zap(f["chave"], f["texto"])
    itens = "".join(f'<div class="proc"><h3>{t}</h3><p>{d}</p></div>' for t, d in f["itens"])
    quem = "".join(f'<div class="pessoa"><img src="{i}" alt="{n}" loading="lazy"><h3>{n}</h3><p>{p}</p>{f"<span>{r}</span>" if r else ""}</div>' for i, n, p, r in f["quem"])
    ponte = "".join(f'<a class="btn btn-linha" href="{a}">{t}</a>' for a, t in f["ponte"])
    extra = f'<p class="aviso-cfo" style="margin-top:1.4rem">{f["extra"]}</p>' if f.get("extra") else ""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{f["titulo"]} · IHFC Jequié</title>
<meta name="description" content="{f["dor"]}">
<meta property="og:title" content="{f["titulo"]} · IHFC Jequié">
<meta property="og:url" content="https://www.ihfc.com.br/{f["arq"]}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:image" content="https://www.ihfc.com.br/img/ihfc-compartilhar-1200x630.jpg">
<link rel="canonical" href="https://www.ihfc.com.br/{f["arq"]}">
<link rel="icon" href="img/ihfc-favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="img/ihfc-icone-180.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#0e0c0a">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="estilo.css">
</head>
<body class="tem-menu">
<!-- gerado por _trabalho/gerar_frentes.py: editar lá, não aqui -->
<header id="topo">
  <div class="wrap nav">
    <a href="novo.html" aria-label="IHFC, página inicial"><img src="img/ihfc-logo-branco.png" alt="IHFC"></a>
    <ul>{menu(f["arq"])}</ul>
    <a class="btn btn-ouro" href="{link}" target="_blank" rel="noopener">Agendar</a>
  </div>
</header>

<main>
<section class="hero-interna">
  <div class="wrap duas-col" style="align-items:center">
    <div>
      <span class="eyebrow">{f["titulo"]}</span>
      <h1>{f["h1"]}</h1>
      <p>{f["dor"]}</p>
      {extra}
      <p style="margin-top:2rem"><a class="btn btn-ouro" href="{link}" target="_blank" rel="noopener">{ICONE_ZAP}{f["botao"]}</a></p>
    </div>
    <img class="foto-alta" src="{f["foto"]}" alt="" style="aspect-ratio:4/4.4">
  </div>
</section>

<section class="seguranca" style="padding-top:40px">
  <div class="wrap">
    <span class="eyebrow">O que é feito</span>
    <h2>Caminhos que a avaliação <em>pode indicar</em>.</h2>
    <div class="procs" style="margin-top:2.2rem">{itens}</div>
    <p class="aviso-cfo">A indicação é individual e só é feita na avaliação presencial. O número de sessões e o resultado variam de pessoa para pessoa. Imagens ilustrativas.</p>
  </div>
</section>

<section class="equipe">
  <div class="wrap">
    <span class="eyebrow">Quem faz</span>
    <h2>Quem cuida <em>de você</em>.</h2>
    <div class="grade-equipe">{quem}</div>
  </div>
</section>

<section class="contato">
  <div class="wrap">
    <span class="eyebrow">Próximo passo</span>
    <h2>Comece por <em>uma conversa</em>.</h2>
    <p class="lead">Toque no botão: a mensagem já vai pronta e a equipe te responde no WhatsApp.</p>
    <a class="btn btn-ouro" href="{link}" target="_blank" rel="noopener">{ICONE_ZAP}{f["botao"]}</a>
    <p style="margin-top:3rem;color:var(--suave);font-size:.86rem">Conheça também</p>
    <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:1rem">{ponte}</div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <img src="img/ihfc-logo-branco.png" alt="IHFC">
    <span>IHFC · Instituto de Harmonização Facial e Corporal · Responsável técnico: Dr. Glautium Gabriel, CRO-BA 16384 · EPAO 5145 · CNES 4327152</span>
    <span class="rodape-links"><a href="procedimentos.html">Procedimentos</a><a href="dr-glautium.html">Dr. Glautium</a><a href="essencia.html">Revista ESSÊNCIA</a><a href="privacidade.html">Privacidade</a></span>
  </div>
</footer>

<a class="zap btn btn-ouro" href="{link}" target="_blank" rel="noopener">{ICONE_ZAP}{f["botao"]}</a>
<script>
const topo=document.getElementById('topo');
addEventListener('scroll',()=>topo.classList.toggle('sol',scrollY>40),{{passive:true}});
</script>
<script src="menu.js"></script>
</body>
</html>
'''


if __name__ == "__main__":
    for f in FRENTES:
        open(os.path.join(RAIZ, f["arq"]), "w", encoding="utf-8").write(pagina(f))
        print(f["arq"], f["chave"], zap(f["chave"], f["texto"])[:80])
    # lista dos links por frente, para o robô do WhatsApp e o Marketing
    with open(os.path.join(RAIZ, "_trabalho", "links-whatsapp-por-frente.md"), "w", encoding="utf-8") as s:
        s.write("# Links de WhatsApp por frente (site IHFC)\n\nA mensagem começa com a PALAVRA-CHAVE; o robô usa a palavra para saber a origem e passa à Jaiane.\n\n| Frente | Palavra | Página | Link |\n|---|---|---|---|\n")
        for f in FRENTES:
            s.write(f'| {f["titulo"]} | {f["chave"]} | https://www.ihfc.com.br/{f["arq"]} | {zap(f["chave"], f["texto"])} |\n')
