"""Auditoria 27/10/2026: prévias (jpg) das melhorias premium propostas para o site.
Gera um html por melhoria em _trabalho/previas-premium/ e fotografa com o Chrome."""
import os, subprocess
from PIL import Image
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, '_trabalho', 'previas-premium')
os.makedirs(OUT, exist_ok=True)
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
I = '../../img/'
CSS = '''
:root{--preto:#0e0c0a;--preto2:#171411;--preto3:#221d18;--ouro:#c9a45c;--ouro-claro:#e2c88f;--creme:#f3ebdd;--creme2:#d9cfbf;--suave:#a89d8c;--linha:rgba(201,164,92,.22)}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1280px;height:800px;overflow:hidden;background:var(--preto);color:var(--creme2);font:15px/1.6 Inter,sans-serif;position:relative}
h1,h2,h3{font-family:'Cormorant Garamond',serif;font-weight:500;color:var(--creme);line-height:1.05}
em{color:var(--ouro-claro)}
.tag{position:absolute;top:18px;right:18px;z-index:9;background:var(--ouro);color:#14100b;font:600 12px Inter;letter-spacing:.12em;padding:7px 14px;border-radius:99px;text-transform:uppercase}
.eb{font:500 12px Inter;letter-spacing:.22em;text-transform:uppercase;color:var(--ouro)}
.btn{display:inline-block;padding:14px 26px;border-radius:99px;font:500 14px Inter;text-decoration:none}
.ouro{background:linear-gradient(135deg,var(--ouro-claro),var(--ouro));color:#14100b}
.linha{border:1px solid var(--ouro);color:var(--creme)}
.wrap{padding:70px 80px}
'''
FONT = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,400;1,500'
        '&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">')

P = {}
P['01-hero-video-bastidor'] = ('Hero com vídeo de bastidor', f'''
<style>.hero{{position:absolute;inset:0;background:url({I}ihfc-consultorio.webp) center/cover;filter:saturate(.85) contrast(1.05)}}
.hero:after{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,12,10,.94) 30%,rgba(14,12,10,.35))}}
.txt{{position:absolute;left:80px;top:190px;width:580px}} h1{{font-size:78px;margin:18px 0}} p{{font-size:17px;max-width:480px;margin-bottom:30px}}
.play{{position:absolute;right:90px;bottom:70px;display:flex;align-items:center;gap:14px;color:var(--creme);font-size:13px;letter-spacing:.1em}}
.play b{{width:54px;height:54px;border:1px solid var(--ouro);border-radius:50%;display:grid;place-items:center;color:var(--ouro)}}
.grao{{position:absolute;inset:0;opacity:.07;background-image:radial-gradient(#fff 1px,transparent 1px);background-size:3px 3px}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:3px;background:linear-gradient(90deg,var(--ouro) 38%,rgba(201,164,92,.2) 38%)}}</style>
<div class="hero"></div><div class="grao"></div>
<div class="txt"><span class="eb">Policlínica · Jequié/BA</span><h1>Cuidado completo,<br><em>do rosto ao corpo</em>.</h1>
<p>No fundo, um vídeo curto e silencioso em loop: recepção, esterilização, consultório e equipe trabalhando, com tratamento de cor de cinema.</p>
<a class="btn ouro">Agendar avaliação</a></div>
<div class="play"><b>❚❚</b>BASTIDOR IHFC · 20 s EM LOOP</div><div class="bar"></div>''')

P['02-escolha-guiada'] = ('Escolha guiada em 3 toques', '''
<style>.c{display:grid;grid-template-columns:1fr 1.15fr;gap:60px;align-items:center;height:800px;padding:0 80px} h2{font-size:62px;margin:16px 0 18px}
.passos{display:flex;gap:8px;margin-bottom:22px} .passos i{flex:1;height:4px;border-radius:4px;background:var(--preto3)} .passos i.on{background:var(--ouro)}
.cx{background:var(--preto2);border:1px solid var(--linha);border-radius:24px;padding:38px} .cx h3{font-size:32px;margin:10px 0 22px}
.op{display:grid;grid-template-columns:1fr 1fr;gap:12px} .op div{border:1px solid var(--linha);border-radius:16px;padding:18px 20px;color:var(--creme)}
.op div.sel{border-color:var(--ouro);background:rgba(201,164,92,.1)} .op small{display:block;color:var(--suave);font-size:12px}
.fim{margin-top:24px;display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--suave)}</style>
<div class="c"><div><span class="eb">Não sabe por onde começar?</span><h2>Monte o seu <em>caminho</em>.</h2>
<p style="font-size:17px">Três perguntas rápidas: o que incomoda, há quanto tempo e o que você espera. No fim, o WhatsApp abre já com a palavra da área certa (PAPADA, SORRISO, CABELO…) e a equipe responde sabendo do que se trata.</p></div>
<div class="cx"><div class="passos"><i class="on"></i><i class="on"></i><i></i></div><span class="eb">Pergunta 2 de 3</span>
<h3>O que mais te incomoda no rosto?</h3><div class="op">
<div class="sel">Papada e contorno<small>queixo, mandíbula, pescoço</small></div><div>Rugas e linhas<small>testa, olhos, boca</small></div>
<div>Olheiras e cansaço<small>olhar abatido</small></div><div>Lábios<small>volume, contorno</small></div>
<div>Manchas e acne<small>textura da pele</small></div><div>Ainda não sei<small>quero uma avaliação</small></div></div>
<div class="fim"><span>← voltar</span><a class="btn ouro">Continuar</a></div></div></div>''')

eq = [('glautium-gabriel', 'Dr. Glautium Gabriel', 'Face · cirurgia'), ('jessica-lopes', 'Dra. Jéssica Lopes', 'Face · estética'),
      ('ionara-caroso', 'Dra. Ionara Caroso', 'Corpo'), ('mateus-brito', 'Dr. Mateus Brito', 'Cabelo')]
cards = ''.join(f'<div class="p"><img src="{I}ihfc-equipe-{a}.webp"><h3>{n}</h3><small>{r}</small></div>' for a, n, r in eq)
P['03-equipe-por-area'] = ('Equipe com filtro por área', f'''
<style>h2{{font-size:58px;margin:14px 0 24px}} .chips{{display:flex;gap:10px;margin-bottom:30px}} .chips span{{border:1px solid var(--linha);border-radius:99px;padding:9px 18px;color:var(--creme2);font-size:13px}}
.chips span.on{{background:var(--ouro);color:#14100b;border-color:var(--ouro)}} .g{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}}
.p img{{width:100%;height:330px;object-fit:cover;object-position:top;border-radius:18px;border:1px solid var(--linha)}}
.p h3{{font-size:24px;margin-top:14px}} .p small{{color:var(--ouro);font-size:12px;letter-spacing:.1em;text-transform:uppercase}}</style>
<div class="wrap"><span class="eb">Equipe</span><h2>Quem cuida <em>de você</em>, por área.</h2>
<div class="chips"><span class="on">Todas</span><span>Face</span><span>Corpo</span><span>Sorriso</span><span>Cabelo</span><span>Nutrição</span><span>Estética</span><span>Bem-estar</span></div>
<div class="g">{cards}</div></div>''')

P['04-visite-mapa'] = ('Bloco Visite o IHFC com mapa', f'''
<style>.c{{display:grid;grid-template-columns:1fr 1fr;height:800px}} .f{{background:url({I}ihfc-fachada.webp) center/cover;position:relative}}
.f:after{{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(14,12,10,.85),transparent 55%)}}
.mapa{{position:absolute;left:40px;right:40px;bottom:40px;height:250px;z-index:2;border-radius:20px;border:1px solid var(--ouro);overflow:hidden;background-color:#1b1814;
background-image:linear-gradient(28deg,transparent 46%,#3a3127 47%,#3a3127 50%,transparent 51%),linear-gradient(-60deg,transparent 30%,#2c261f 31%,#2c261f 34%,transparent 35%),linear-gradient(95deg,transparent 60%,#2c261f 61%,#2c261f 63%,transparent 64%)}}
.mapa span{{position:absolute;left:20px;top:16px;font-size:12px;letter-spacing:.15em;color:var(--suave)}}
.pin{{position:absolute;left:52%;top:40%;width:26px;height:26px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--ouro);box-shadow:0 0 0 10px rgba(201,164,92,.18)}}
.t{{padding:110px 80px}} h2{{font-size:60px;margin:16px 0 30px}} .i{{border-top:1px solid var(--linha);padding:18px 0;display:flex;justify-content:space-between}} .i b{{color:var(--creme);font-weight:500}}</style>
<div class="c"><div class="f"><div class="mapa"><span>MAPA ESCURO DO GOOGLE</span><div class="pin"></div></div></div>
<div class="t"><span class="eb">Visite</span><h2>Estamos no <em>Jequiezinho</em>.</h2>
<div class="i"><b>Endereço</b><span>R. Dr. João Braga, 640 · Jequié/BA</span></div>
<div class="i"><b>Seg. a sex.</b><span>8h–12h · 14h–18h</span></div><div class="i"><b>Sábado</b><span>8h–12h</span></div>
<div class="i"><b>Chegando</b><span>foto da fachada + rota no celular</span></div>
<div style="margin-top:30px;display:flex;gap:12px"><a class="btn ouro">Como chegar</a><a class="btn linha">Falar no WhatsApp</a></div></div></div>''')

P['05-avaliacoes-google'] = ('Avaliações do Google em destaque', '''
<style>.top{display:flex;justify-content:space-between;align-items:end;margin-bottom:40px} h2{font-size:58px;margin-top:14px}
.nota{text-align:right} .nota b{font:500 64px 'Cormorant Garamond',serif;color:var(--creme)} .nota div{color:var(--ouro);letter-spacing:4px} .nota small{color:var(--suave)}
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:22px} .r{background:var(--preto2);border:1px solid var(--linha);border-radius:20px;padding:30px}
.r div{color:var(--ouro);letter-spacing:3px} .r q{display:block;font:italic 400 23px/1.35 'Cormorant Garamond',serif;color:var(--creme);margin:16px 0 22px;quotes:none}
.r span{font-size:13px;color:var(--suave)} .ponto{display:flex;gap:8px;justify-content:center;margin-top:30px} .ponto i{width:8px;height:8px;border-radius:50%;background:var(--preto3)} .ponto i:first-child{background:var(--ouro);width:26px;border-radius:8px}</style>
<div class="wrap"><div class="top"><div><span class="eb">Avaliações reais no Google</span><h2>O que dizem <em>os pacientes</em>.</h2></div>
<div class="nota"><b>nota real</b><div>★★★★★</div><small>nota e número de avaliações puxados do Google</small></div></div>
<div class="g"><div class="r"><div>★★★★★</div><q>Iniciei meu tratamento de melasma e me sinto satisfeita pelo profissionalismo.</q><span>Paciente · Google</span></div>
<div class="r"><div>★★★★★</div><q>Os cuidados com os pacientes no pós é o que cativa a gente como cliente.</q><span>Paciente · Google</span></div>
<div class="r"><div>★★★★★</div><q>Desde a recepção à consulta, tirando todas as dúvidas.</q><span>Maria P. · Google</span></div></div>
<div class="ponto"><i></i><i></i><i></i><i></i></div></div>''')

P['06-tipografia-editorial'] = ('Tipografia editorial estilo ESSÊNCIA', '''
<style>.c{display:grid;grid-template-columns:420px 1fr;height:800px} .n{border-right:1px solid var(--linha);padding:80px 60px;display:flex;flex-direction:column;gap:6px}
.n div{display:flex;gap:18px;align-items:baseline;padding:12px 0;border-bottom:1px solid rgba(201,164,92,.1);color:var(--suave);font:400 26px 'Cormorant Garamond',serif}
.n div i{font:500 12px Inter;color:var(--ouro);letter-spacing:.15em;font-style:normal} .n div.on{color:var(--creme)}
.t{padding:110px 90px;position:relative} .num{position:absolute;right:70px;top:30px;font:italic 400 300px/1 'Cormorant Garamond',serif;color:rgba(201,164,92,.09)}
h2{font-size:96px;font-style:italic;font-weight:400;margin:20px 0 26px} .fil{width:90px;height:1px;background:var(--ouro);margin:28px 0}
p{font-size:18px;max-width:560px} .cap:first-letter{font:500 64px/0.8 'Cormorant Garamond',serif;float:left;color:var(--ouro);margin:8px 10px 0 0}</style>
<div class="c"><div class="n"><span class="eb" style="margin-bottom:14px">Índice</span><div class="on"><i>01</i>Face</div><div><i>02</i>Corpo</div><div><i>03</i>Sorriso</div><div><i>04</i>Cabelo</div><div><i>05</i>Nutrição</div><div><i>06</i>Estética</div><div><i>07</i>Bem-estar</div></div>
<div class="t"><div class="num">01</div><span class="eb">Área 01 · Face</span><h2>O rosto,<br><em>com método</em>.</h2><div class="fil"></div>
<p class="cap">Cada área abre como um capítulo da revista: número grande ao fundo, título em itálico, capitular dourada e filete fino. O mesmo idioma visual da ESSÊNCIA, para o site e a revista parecerem da mesma casa.</p></div></div>''')

P['07-tour-clinica'] = ('Tour pela clínica em tela cheia', f'''
<style>.g{{position:absolute;inset:0;display:grid;grid-template-columns:2fr 1fr;grid-template-rows:1fr 1fr;gap:6px}}
.g div{{background-size:cover;background-position:center;position:relative}} .g div:after{{content:attr(data-l);position:absolute;left:24px;bottom:20px;color:var(--creme);font:italic 400 28px 'Cormorant Garamond',serif;text-shadow:0 2px 16px #000}}
.g div:first-child{{grid-row:span 2}} .ov{{position:absolute;left:0;top:0;bottom:0;width:66.6%;background:linear-gradient(90deg,rgba(14,12,10,.88),transparent 65%)}}
.t{{position:absolute;left:70px;top:90px;width:430px}} h2{{font-size:66px;margin:16px 0 20px}} .ctrl{{position:absolute;left:70px;bottom:70px;display:flex;gap:10px;align-items:center;color:var(--suave);font-size:13px}}
.ctrl b{{width:46px;height:46px;border-radius:50%;border:1px solid var(--ouro);display:grid;place-items:center;color:var(--ouro)}}</style>
<div class="g"><div data-l="" style="background-image:url({I}ihfc-fachada.webp)"></div><div data-l="Consultório" style="background-image:url({I}ihfc-consultorio.webp)"></div><div data-l="Sala de avaliação" style="background-image:url({I}ihfc-sala-dr-glautium.webp)"></div></div>
<div class="ov"></div><div class="t"><span class="eb">Por dentro do IHFC</span><h2>Conheça a clínica <em>antes de vir</em>.</h2><p style="font-size:16px">Galeria em tela cheia, foto a foto, com legenda: recepção, Sala VIP, central de esterilização, raio-x digital e salas de procedimento. Pode incluir o tour 360° do Google.</p></div>
<div class="ctrl"><b>←</b><b>→</b>1 / 8 · toque para tela cheia</div>''')

for nome, (titulo, corpo) in P.items():
    h = os.path.join(OUT, f'ihfc-site_melhoria{nome}_previa.html')
    open(h, 'w', encoding='utf-8').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>{FONT}<style>{CSS}</style></head><body><span class="tag">Prévia · {titulo}</span>{corpo}</body></html>')
    png = h[:-5] + '.png'
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,800',
                    '--virtual-time-budget=5000', '--allow-file-access-from-files', f'--screenshot={png}',
                    'file:///' + h.replace('\\', '/')], capture_output=True, timeout=120)
    Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=88)
    os.remove(png)
    print('ok', os.path.basename(png[:-4] + '.jpg'))
