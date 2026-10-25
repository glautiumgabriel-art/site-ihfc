// Queixas da seção "Comece pelo que te incomoda": cada cartão abre uma janela com os
// procedimentos, um resumo de cada um e quem faz. Fonte: revista ESSÊNCIA nº 01 (out/2026).
const P = {
  glautium: "Dr. Glautium Gabriel",
  ionara: "Dra. Ionara Caroso",
  juliana: "Dra. Juliana Coelho Moreno",
  hudson: "Dr. Hudson D. Soares",
  jessica: "Dra. Jéssica Lopes",
  sabrina: "Sabrina Amparo (nutrição)",
  gisele: "Gisele Gomes (fisioterapia)",
  natielli: "Natielli Batista (massoterapia)",
  neuza: "Maria Neuza (podologia)",
  matheus: "Dr. Mateus Brito (tricologia)",
  duda: "Maria Eduarda Brisola (estética)",
  equipe: "Equipe IHFC",
};

const QUEIXAS = [
  // ROSTO
  { area: "rosto", img: "ihfc-pele-manchas", q: "Mancha escura no rosto que não sai", tag: "Pele · manchas e melasma",
    intro: "Pode ser melasma: uma mancha crônica ligada a hormônios, sol, calor e genética. Não tem cura definitiva, mas tem controle com método.",
    itens: [
      ["Protocolo Revitalli", "Gerenciamento de pele aplicado há 8 anos no IHFC: etapas no consultório e passo a passo em casa, com retornos programados.", [P.glautium]],
      ["Peelings", "Renovam a camada superficial da pele e ajudam a clarear manchas e uniformizar o tom.", [P.glautium, P.ionara, P.duda]],
      ["Laser e luz intensa pulsada", "Tratam manchas de sol, vasinhos do rosto e vermelhidão, com pouca interferência na rotina.", [P.ionara]],
      ["Avaliação dermatológica", "Investiga a causa da mancha e garante que o tratamento comece numa pele saudável.", [P.ionara]],
    ] },
  { area: "rosto", img: "ihfc-papada-contorno", q: "Papada mesmo sendo magra", tag: "Contorno · papada e pescoço",
    intro: "Papada nem sempre é gordura: pode ser pele flácida, queixo posicionado para trás ou as bandas do músculo do pescoço. Cada causa pede uma técnica.",
    itens: [
      ["Enzimas para papada", "Reduzem a gordura localizada sob o queixo, sem cirurgia.", [P.glautium]],
      ["Endolaser de papada", "Fibra de laser sob a pele que retrai os tecidos e reduz pequenos acúmulos de gordura, sem cortes.", [P.glautium]],
      ["Lipo de papada", "Pequena lipoaspiração sob o queixo, por microincisões e com anestesia local.", [P.glautium]],
      ["Mentoplastia", "Projeta o queixo com ácido hialurônico ou cirurgia, equilibrando o perfil.", [P.glautium]],
      ["Cervicoplastia e platismoplastia", "Tratam o excesso de pele e as bandas do músculo do pescoço.", [P.glautium]],
    ] },
  { area: "rosto", img: "ihfc-flacidez", q: "Meu rosto está caindo", tag: "Flacidez · sustentação",
    intro: "Com o tempo o corpo produz menos colágeno e os tecidos cedem. O plano costuma combinar sustentação imediata e estímulo de colágeno.",
    itens: [
      ["Fios de sustentação", "Fios absorvíveis com pequenas garras reposicionam os tecidos, com efeito lifting logo após o procedimento.", [P.glautium]],
      ["Bioestimulador de colágeno", "Estimula o seu próprio colágeno: a firmeza aparece aos poucos, de forma natural.", [P.glautium]],
      ["Endolaser", "Trata a flacidez por dentro, sem cortes, no contorno da mandíbula, bochechas e pescoço.", [P.glautium]],
      ["Ultrassom microfocado", "Energia concentrada nas camadas profundas para efeito lifting, sem agulhas.", [P.equipe]],
    ] },
  { area: "rosto", img: "ihfc-rugas", q: "Pareço cansada ou brava", tag: "Rugas · linhas de expressão",
    intro: "As linhas da testa, entre as sobrancelhas e ao redor dos olhos podem ser suavizadas sem tirar a sua expressão.",
    itens: [
      ["Toxina botulínica", "Relaxa os músculos das linhas de expressão: testa, glabela e pés de galinha. Efeito em poucos dias, com retorno para ajuste.", [P.glautium]],
      ["Elevação das sobrancelhas", "Microdoses de toxina para um olhar mais aberto e descansado.", [P.glautium]],
      ["Skinbooster", "Microinjeções de ácido hialurônico fluido que hidratam a pele por dentro e devolvem o viço.", [P.glautium]],
      ["Bioestimulador de colágeno", "Melhora a qualidade e a firmeza da pele, complementando a toxina.", [P.glautium]],
    ] },
  { area: "rosto", img: "ihfc-rosto-fino", q: "Rosto redondo, bochecha gordinha", tag: "Contorno · bochechas",
    intro: "Quando o volume está concentrado nas bochechas, há caminhos com e sem cirurgia. Em rostos finos, a avaliação é decisiva.",
    itens: [
      ["Bichectomia", "Remove parte das bolas de Bichat por dentro da boca, com anestesia local e sem cicatriz aparente.", [P.glautium]],
      ["Toxina no masseter", "Afina o ângulo da mandíbula e alivia o bruxismo.", [P.glautium]],
      ["Enzimas e lipo de papada", "Completam o contorno quando também há gordura sob o queixo.", [P.glautium]],
    ] },
  { area: "rosto", img: "ihfc-nariz-olheiras", q: "Calombo no nariz, ponta caída", tag: "Nariz · rinomodelação",
    intro: "Sem cortes, pequenas quantidades de ácido hialurônico equilibram o perfil. A rinomodelação não diminui o nariz: equilibra proporções.",
    itens: [
      ["Rinomodelação", "Disfarça a giba, eleva a ponta e alinha o perfil com ácido hialurônico.", [P.glautium, P.juliana]],
      ["Toxina na ponta do nariz", "Ajuda a deixar a ponta mais empinada ao sorrir.", [P.glautium]],
    ] },
  { area: "rosto", img: "ihfc-avaliacao-rosto", q: "Olheira funda, cara de cansada", tag: "Olhar · olheiras",
    intro: "A olheira pode ser sulco, pigmento, vasinhos ou bolsa de gordura. Entender a causa vem antes de qualquer preenchimento.",
    itens: [
      ["Preenchimento de olheira", "Suaviza o sulco entre a pálpebra e a bochecha com ácido hialurônico.", [P.glautium, P.juliana]],
      ["Olheira escura", "Peelings, laser e cuidados diários com a pele para clarear a região.", [P.glautium, P.ionara]],
      ["Jato de plasma", "Retração da pele em áreas delicadas, como as pálpebras.", [P.equipe]],
      ["Bolsa de gordura", "Pede avaliação específica para indicar o melhor caminho.", [P.glautium]],
    ] },
  { area: "rosto", img: "ihfc-hero-rosto", q: "Orelha de abano", tag: "Orelhas · otomodelação",
    intro: "Dá para suavizar a orelha de abano sem cirurgia.",
    itens: [
      ["Otomodelação", "Técnica personalizada que aproxima as orelhas da cabeça, sem cortes.", [P.glautium]],
    ] },
  { area: "rosto", img: "ihfc-mandibula-bruxismo", q: "Ranger os dentes, dor de cabeça", tag: "Bruxismo · tensão",
    intro: "A força do músculo da mastigação pode causar desgaste nos dentes, dor e alargar o rosto.",
    itens: [
      ["Toxina no masseter", "Relaxa o músculo que range os dentes, alivia a dor e afina o contorno.", [P.glautium]],
      ["Toxina para cefaleia", "Aplicação no músculo temporal para tensão e enxaqueca, conforme avaliação.", [P.glautium]],
      ["Placa e avaliação odontológica", "Protege os dentes do desgaste noturno.", [P.hudson, P.juliana]],
    ] },

  // SORRISO E LÁBIOS
  { area: "sorriso", img: "ihfc-labios", q: "Boca fina, sem contorno", tag: "Lábios · contorno e volume",
    intro: "O melhor resultado nos lábios é o que parece seu: respeita a proporção entre o lábio de cima e o de baixo e o desenho do arco do cupido.",
    itens: [
      ["Preenchimento labial", "Contorno, volume e projeção com ácido hialurônico, na medida da sua anatomia.", [P.glautium]],
      ["Hidratação labial", "Lábios macios e viçosos, sem aumento de volume.", [P.glautium]],
      ["Lip flip", "Microdoses de toxina para o lábio superior aparecer mais ao sorrir.", [P.glautium]],
      ["Código de barras", "Suaviza as linhas finas acima do lábio.", [P.glautium]],
      ["Micropigmentação labial", "Devolve cor e definição ao contorno da boca.", [P.glautium]],
      ["Lip lift", "Pequena cirurgia que encurta a distância entre nariz e lábio, com cicatriz escondida na base do nariz.", [P.glautium]],
    ] },
  { area: "sorriso", img: "ihfc-sorriso", q: "Tenho vergonha de sorrir", tag: "Sorriso · dentes e gengiva",
    intro: "Um sorriso bonito é proporção: cor, forma, alinhamento e o desenho da gengiva. Com o planejamento digital, você vê o resultado antes de começar.",
    itens: [
      ["Planejamento digital do sorriso", "Fotos, vídeos e escaneamento para desenhar o novo sorriso.", [P.hudson, P.juliana]],
      ["Lentes de contato dental", "Lâminas ultrafinas de porcelana para cor, forma e espaços.", [P.hudson, P.juliana]],
      ["Facetas em resina", "Escultura direta sobre os dentes, em poucas sessões.", [P.hudson, P.juliana]],
      ["Clareamento dental", "No consultório, caseiro ou combinado.", [P.hudson, P.juliana]],
      ["Alinhadores invisíveis", "Placas transparentes e removíveis para alinhar os dentes.", [P.hudson, P.juliana]],
      ["Gengivoplastia e toxina", "Recontorno da gengiva ou microdoses de toxina para o sorriso gengival.", [P.hudson, P.juliana, P.glautium]],
      ["Implantes dentários", "Reposição de dentes perdidos, com função e estética.", [P.hudson, P.juliana]],
    ] },

  // CORPO
  { area: "corpo", img: "ihfc-corpo-barriga", q: "Barriga que não sai com dieta", tag: "Abdome · gordura, flacidez, diástase",
    intro: "\"Barriga\" costuma reunir três questões: gordura localizada, pele flácida e diástase (afastamento dos músculos, comum após a gestação).",
    itens: [
      ["Criolipólise", "Resfriamento controlado que elimina parte das células de gordura, sem cortes.", [P.ionara]],
      ["Mini lipo", "Cânulas finas por microincisões, com anestesia local, para pequenas áreas de gordura.", [P.ionara]],
      ["Endolaser corporal", "Retrai a pele e reduz gordura localizada por dentro.", [P.ionara]],
      ["Bioestimulador e radiofrequência", "Tratam a flacidez da pele do abdome.", [P.ionara]],
      ["Fisioterapia para diástase", "Exercícios, drenagem e ultracavitação no pós-parto.", [P.gisele]],
      ["Massagem modeladora", "Contorno e menos inchaço, como complemento.", [P.natielli]],
    ] },
  { area: "corpo", img: "ihfc-corpo-bumbum", q: "Bumbum caído, celulite, estrias", tag: "Glúteos · firmeza e pele",
    intro: "O plano pode combinar bioestimuladores, Endolaser, tecnologias e tratamentos para celulite e estrias. Volume é decisão médica, não tendência.",
    itens: [
      ["Bioestimulador glúteo", "Firmeza e qualidade da pele do bumbum.", [P.ionara]],
      ["Harmonização glútea", "Bioestimulador, tecnologias e, quando indicado, preenchimento.", [P.ionara]],
      ["Celulite", "Subcisão, bioestimulador diluído, enzimas e tecnologias.", [P.ionara]],
      ["Estrias", "Microagulhamento, laser e radiofrequência.", [P.ionara, P.gisele]],
      ["Endolaser glúteo e culote", "Firmeza e redução de gordura localizada.", [P.ionara]],
    ] },
  { area: "corpo", img: "ihfc-corpo-seios", q: "Seio caído, peito masculino", tag: "Seios e peitoral",
    intro: "Em flacidez leve a moderada, há caminhos sem cortes. Queda acentuada ou desejo de mais volume pedem avaliação com cirurgião plástico.",
    itens: [
      ["Endolaser mamário", "Retrai os tecidos e estimula colágeno, com recuperação rápida.", [P.ionara]],
      ["Colo", "Bioestimulador e skinbooster para firmeza e textura.", [P.ionara]],
      ["Peitoral masculino", "Endolaser e mini lipo para a gordura localizada no peito.", [P.ionara]],
    ] },
  { area: "corpo", img: "ihfc-pernas-vasinhos", q: "Vasinhos nas pernas", tag: "Pernas · microvasos",
    intro: "Vasinhos, celulite e flacidez pedem tratamentos diferentes, que podem caber no mesmo plano. Varizes pedem avaliação com o especialista vascular.",
    itens: [
      ["PEIM", "Microinjeções nos vasinhos que levam à retração e ao clareamento gradual.", [P.jessica, P.ionara]],
      ["Escleroterapia com espuma", "Para vasos um pouco mais calibrosos.", [P.ionara]],
      ["Flacidez de braços e coxas", "Bioestimulador, Endolaser e radiofrequência.", [P.ionara]],
      ["Clareamento de áreas", "Axilas, virilha e entre pernas.", [P.jessica]],
    ] },
  { area: "corpo", img: "ihfc-emagrecimento", q: "Não consigo emagrecer", tag: "Emagrecimento com saúde",
    intro: "Obesidade é uma doença crônica e merece tratamento sério, com consulta, exames e acompanhamento de perto.",
    itens: [
      ["Emagrecimento com acompanhamento médico", "Consulta completa, exames e, quando indicado, medicação com prescrição e retornos periódicos.", [P.ionara]],
      ["Plano alimentar", "Avaliação nutricional e plano individual, preservando a massa muscular.", [P.sabrina]],
      ["Bioimpedância", "Mostra a sua composição corporal: o ponto de partida em números.", [P.sabrina, P.ionara]],
      ["Flacidez depois de emagrecer", "Bioestimulador e Endolaser ajudam a pele a acompanhar o novo corpo.", [P.ionara]],
    ] },

  // PELE E SAÚDE
  { area: "saude", img: "ihfc-acne-cicatrizes", q: "Espinhas, cicatrizes de acne, poros", tag: "Pele · acne e textura",
    intro: "Acne ativa e cicatrizes pedem tratamentos diferentes, que se combinam com o cuidado em casa.",
    itens: [
      ["Tratamento da acne", "Avaliação médica, tratamento clínico e procedimentos.", [P.ionara]],
      ["Protocolo Revitalli", "Melhora a textura e o relevo das cicatrizes de acne.", [P.glautium]],
      ["Microagulhamento e radiofrequência", "Estimulam colágeno: cicatrizes, poros e textura.", [P.glautium, P.ionara, P.duda]],
      ["Laser CO₂ fracionado", "Rejuvenescimento intenso para cicatrizes e rugas finas.", [P.ionara]],
      ["Limpeza de pele protocolada", "Específica para o seu tipo de pele, com peeling de diamante e LED.", [P.duda]],
    ] },
  { area: "saude", img: "ihfc-cabelo-implante", q: "Cabelo caindo ou ralo", tag: "Cabelo · tricologia",
    intro: "Queda de cabelo tem causa: genética, hormônios, estresse, alimentação ou doenças do couro cabeludo. E tem tratamento.",
    itens: [
      ["Avaliação tricológica", "Exame do couro cabeludo e dos fios, com tricoscopia e exames quando necessário.", [P.matheus]],
      ["Tratamento clínico", "Medicações, intradermoterapia capilar e cuidados em casa.", [P.matheus, P.ionara]],
      ["Implante capilar", "Fios da nuca levados para as áreas com falhas, com anestesia local.", [P.matheus]],
    ] },
  { area: "saude", img: "ihfc-dermatologia", q: "Pinta estranha, suor excessivo", tag: "Dermatologia · saúde da pele",
    intro: "Antes de ser estética, pele é saúde. Consultas regulares ajudam a prevenir e diagnosticar cedo o câncer de pele.",
    itens: [
      ["Mapeamento de pintas", "Dermatoscopia para detectar alterações cedo (regra do ABCDE).", [P.ionara]],
      ["Pequenas cirurgias", "Retirada de pintas e cistos, com biópsia.", [P.ionara]],
      ["Hiperidrose", "Suor excessivo nas axilas, mãos ou pés tratado com toxina.", [P.ionara]],
      ["Rosácea e check-up da pele", "Controle da vermelhidão e avaliação completa.", [P.ionara]],
    ] },
  { area: "saude", img: "ihfc-podologia", q: "Unha encravada, calo, fungo", tag: "Pés · podologia",
    intro: "A podologia trata unhas, pele e pequenas alterações dos pés, com instrumentos esterilizados e, quando preciso, anestesia.",
    itens: [
      ["Unha encravada e órtese", "Alívio da dor e correção, quase sempre sem cirurgia, evitando que volte.", [P.neuza]],
      ["Fungos nas unhas", "Laser e protocolos tópicos.", [P.neuza]],
      ["Calos e rachaduras", "Remoção cuidadosa, desbaste e hidratação profunda.", [P.neuza]],
      ["Pé diabético", "Avaliação preventiva e cuidados especializados.", [P.neuza]],
      ["Spa dos pés", "Esfoliação, hidratação e massagem.", [P.neuza]],
    ] },
  { area: "saude", img: "ihfc-feridas", q: "Ferida que não cicatriza", tag: "Tratamento de feridas",
    intro: "Feridas que demoram a fechar pedem avaliação e cuidado de perto. No pé diabético, agir cedo faz toda a diferença.",
    itens: [
      ["Pé diabético e úlceras de perna", "Tratamento acompanhando circulação, glicemia e calçado, junto com o seu médico.", [P.equipe]],
      ["Desbridamento e coberturas", "Remoção do tecido sem vida e curativos certos para cada fase.", [P.equipe]],
      ["Ozonioterapia e PRP", "Recursos complementares que ajudam no controle de bactérias e na cicatrização.", [P.equipe]],
    ] },

  // BEM-ESTAR
  { area: "bemestar", img: "ihfc-bem-estar", q: "Inchaço, pós-operatório, tensão", tag: "Bem-estar · fisioterapia e massagem",
    intro: "O cuidado com o corpo continua entre uma sessão e outra: circulação, recuperação e momentos de pausa.",
    itens: [
      ["Drenagem e pós-operatório", "Reduz o inchaço e acelera a recuperação depois de procedimentos.", [P.gisele, P.natielli]],
      ["Liberação miofascial", "Alívio de tensões e dores musculares.", [P.gisele]],
      ["Massagem relaxante", "Velas, pedras quentes e bambu para desacelerar.", [P.natielli]],
      ["Massagem modeladora", "Ajuda no contorno e na retenção de líquidos.", [P.natielli]],
    ] },
  { area: "bemestar", img: "ihfc-nutricao", q: "Quero comer melhor", tag: "Nutrição",
    intro: "Nenhum tratamento estético se sustenta sozinho: a alimentação acompanha cada etapa do plano.",
    itens: [
      ["Avaliação nutricional", "Entende a sua rotina, história e objetivos.", [P.sabrina]],
      ["Recomposição corporal", "Mais músculo e menos gordura, com plano individual.", [P.sabrina]],
      ["Acompanhamento contínuo", "Ajustes do plano ao longo do tempo.", [P.sabrina]],
    ] },
];

const AREAS = [
  ["todos", "Todas"], ["rosto", "Rosto"], ["sorriso", "Sorriso e lábios"],
  ["corpo", "Corpo"], ["saude", "Pele e saúde"], ["bemestar", "Bem-estar"],
];

const ZAP = "https://wa.me/5573981507715?text=";

function montarQueixas() {
  const grade = document.getElementById("grade-dores");
  const filtros = document.getElementById("filtros-dores");
  if (!grade) return;

  grade.innerHTML = QUEIXAS.map((d, i) => `
    <button class="dor" type="button" data-area="${d.area}" data-i="${i}" aria-haspopup="dialog">
      <img src="img/${d.img}.webp" alt="" loading="lazy">
      <div class="dor-txt"><q>${d.q}</q>
        <p>${d.itens.length} ${d.itens.length > 1 ? "caminhos possíveis" : "caminho possível"}</p>
        <small>${d.tag}</small>
        <span class="dor-ver">Ver tratamentos →</span>
      </div>
    </button>`).join("");

  filtros.innerHTML = AREAS.map(([id, nome], i) =>
    `<button type="button" class="filtro${i === 0 ? " ativo" : ""}" data-f="${id}">${nome}</button>`).join("");

  filtros.addEventListener("click", e => {
    const b = e.target.closest(".filtro");
    if (!b) return;
    filtros.querySelectorAll(".filtro").forEach(x => x.classList.toggle("ativo", x === b));
    grade.querySelectorAll(".dor").forEach(c => {
      c.hidden = b.dataset.f !== "todos" && c.dataset.area !== b.dataset.f;
    });
  });

  const dlg = document.getElementById("janela-dor");
  grade.addEventListener("click", e => {
    const c = e.target.closest(".dor");
    if (!c) return;
    const d = QUEIXAS[+c.dataset.i];
    dlg.querySelector(".jd-foto").src = `img/${d.img}.webp`;
    dlg.querySelector(".jd-tag").textContent = d.tag;
    dlg.querySelector(".jd-titulo").textContent = `“${d.q}”`;
    dlg.querySelector(".jd-intro").textContent = d.intro;
    dlg.querySelector(".jd-lista").innerHTML = d.itens.map(([nome, txt, quem]) => `
      <li><h4>${nome}</h4><p>${txt}</p><span>${quem.join(" · ")}</span></li>`).join("");
    dlg.querySelector(".jd-zap").href = ZAP + encodeURIComponent(
      `Olá! Vim pelo site. Me incomoda: "${d.q}". Quero agendar uma avaliação.`);
    dlg.showModal();
    dlg.querySelector(".jd-corpo").scrollTop = 0;
  });
  dlg.addEventListener("click", e => {
    if (e.target === dlg || e.target.closest(".jd-fechar")) dlg.close();
  });
}

montarQueixas();
