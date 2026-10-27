"""v5 da página inicial (27/10/2026): o Dr. achou a v4 "muito poluída e grande".
Só 5 blocos: topo curto, áreas em cartões simples, equipe compacta, "mais do IHFC" e contato.
O resto fica nas páginas internas. Gera v5.html (noindex) a partir do novo.html."""
import os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
h = open('novo.html', encoding='utf-8').read()
cab = h[:h.index('<header id="topo">')]
zap = re.search(r'<a class="zap btn btn-ouro".*?</a>', h, re.S).group(0)
pessoas = re.findall(r'<div class="pessoa surge"><img src="([^"]+)" alt="([^"]+)"[^>]*><h3>[^<]*</h3><p>([^<]*)</p>', h)
contato = re.search(r'<section class="contato" id="contato">.*?</section>', h, re.S).group(0)
apoio = re.search(r'<p class="apoio surge">(.*?)</p>', h).group(1)
rodape = re.search(r'<footer>.*?</footer>', h, re.S).group(0)
WA = 'https://wa.me/5573981507715?text=Ol%C3%A1!%20Vim%20pelo%20site%20e%20quero%20agendar%20uma%20avalia%C3%A7%C3%A3o.'

areas = [("papada-e-rosto.html", "img/ihfc-rosto-fino.webp", "Face"), ("corpo.html", "img/ihfc-corpo-barriga.webp", "Corpo"),
         ("sorriso.html", "img/ihfc-sorriso.webp", "Sorriso"), ("tricologia.html", "img/ihfc-cabelo.webp", "Cabelo"),
         ("nutricao.html", "img/ihfc-nutricao.webp", "Nutrição"), ("pele.html", "img/ihfc-pele-manchas.webp", "Estética"),
         ("procedimentos.html#bem-estar", "img/ihfc-bem-estar.webp", "Bem-estar"), ("procedimentos.html", "img/ihfc-planejamento.webp", "Todos os procedimentos")]
cards = ''.join(f'<a class="v5-area" href="{u}"><img src="{i}" alt="" loading="lazy"><span>{t}</span></a>' for u, i, t in areas)
equipe = ''.join(f'<figure><img src="{i}" alt="{n}" loading="lazy"><figcaption><b>{n}</b>{p.split(" · ")[0]}</figcaption></figure>' for i, n, p in pessoas)

css = '''<style>
.v5-hero{min-height:88svh;display:flex;align-items:flex-end;position:relative;padding:0 0 64px}
.v5-hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}
.v5-hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,12,10,.25) 0%,rgba(14,12,10,.55) 45%,var(--preto) 100%)}
.v5-hero .wrap{position:relative;z-index:1}
.v5-hero h1{font-size:clamp(2.6rem,9vw,5rem);margin:.6rem 0 1rem;max-width:12ch}
.v5-hero p{max-width:30rem;color:var(--creme2);margin-bottom:1.6rem}
.v5-bloco{padding:72px 0}
.v5-bloco h2{font-size:clamp(2rem,6vw,3rem);margin:.5rem 0 1.6rem}
.v5-areas{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
@media(min-width:900px){.v5-areas{grid-template-columns:repeat(4,1fr);gap:16px}}
.v5-area{position:relative;aspect-ratio:4/5;border-radius:18px;overflow:hidden;display:block;color:var(--creme);text-decoration:none}
.v5-area img{width:100%;height:100%;object-fit:cover;transition:transform .6s}
.v5-area:after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(14,12,10,.85),transparent 55%)}
.v5-area span{position:absolute;left:16px;bottom:14px;z-index:1;font-family:var(--serif);font-size:1.5rem}
.v5-area:hover img{transform:scale(1.05)}
.v5-equipe{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:10px;scrollbar-width:none}
.v5-equipe figure{flex:0 0 140px;scroll-snap-align:start;margin:0}
.v5-equipe img{width:140px;height:175px;object-fit:cover;object-position:center 15%;border-radius:16px}
.v5-equipe figcaption{font-size:.78rem;color:var(--suave);margin-top:8px;line-height:1.35}
.v5-equipe b{display:block;color:var(--creme);font-weight:500;font-size:.86rem}
.v5-mais{display:grid;gap:10px}
@media(min-width:900px){.v5-mais{grid-template-columns:repeat(3,1fr)}}
.v5-mais a{display:flex;justify-content:space-between;align-items:center;padding:20px 22px;border:1px solid var(--linha);border-radius:16px;color:var(--creme);text-decoration:none;font-family:var(--serif);font-size:1.3rem}
.v5-mais a:after{content:"→";color:var(--ouro);font-family:Inter,sans-serif}
.v5-mais a:hover{border-color:var(--ouro)}
.v5-apoio{margin-top:1.4rem;color:var(--creme2);font-size:.92rem;max-width:36rem}
.v5-apoio b{color:var(--creme);font-weight:500}
.v5-dica{font-size:.8rem;color:var(--suave);margin-top:.4rem}
</style>
'''
pg = f'''{cab.replace('<link rel="stylesheet" href="estilo.css">', '<link rel="stylesheet" href="estilo.css">' + chr(10) + css)}<header id="topo">
  <div class="wrap nav">
    <a href="v5.html" aria-label="IHFC, página inicial"><img src="img/ihfc-logo-branco.png" alt="IHFC"></a>
    <ul>
      <li><a href="#areas">Áreas</a></li>
      <li><a href="#equipe">Equipe</a></li>
      <li><a href="procedimentos.html">Procedimentos</a></li>
      <li><a href="#contato">Contato</a></li>
    </ul>
    <a class="btn btn-ouro" href="{WA}" target="_blank" rel="noopener">Agendar</a>
  </div>
</header>

<main>
<section class="v5-hero">
  <img src="img/ihfc-hero-rosto.webp" alt="">
  <div class="wrap">
    <span class="eyebrow">Policlínica · Jequié/BA</span>
    <h1>Cuidado completo, <em>do rosto ao corpo</em>.</h1>
    <p>Médicos, dentistas e especialistas em um só lugar.</p>
    <a class="btn btn-ouro" href="{WA}" target="_blank" rel="noopener">Agendar avaliação</a>
  </div>
</section>

<section class="v5-bloco" id="areas">
  <div class="wrap">
    <span class="eyebrow">Áreas</span>
    <h2>Por onde <em>começar</em>?</h2>
    <div class="v5-areas">{cards}</div>
  </div>
</section>

<section class="v5-bloco" id="equipe" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">Equipe</span>
    <h2>Quem cuida <em>de você</em>.</h2>
    <div class="v5-equipe">{equipe}</div>
    <p class="v5-dica">Arraste para o lado →</p>
    <p class="v5-apoio">{apoio}</p>
  </div>
</section>

<section class="v5-bloco" style="padding-top:0">
  <div class="wrap v5-mais">
    <a href="dr-glautium.html">O fundador</a>
    <a href="essencia.html">Revista ESSÊNCIA</a>
    <a href="procedimentos.html">Segurança e procedimentos</a>
  </div>
</section>

{contato}
</main>

{rodape.replace('novo.html', 'v5.html')}

{zap}
<script>
const topo=document.getElementById('topo');
addEventListener('scroll',()=>topo.classList.toggle('sol',scrollY>40),{{passive:true}});
</script>
<script src="menu.js"></script>
</body>
</html>
'''
open('v5.html', 'w', encoding='utf-8').write(pg)
print('ok', len(pessoas), 'pessoas,', len(pg) // 1024, 'KB')
