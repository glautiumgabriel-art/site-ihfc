# Site IHFC: auditoria + melhorias premium (27/10/2026)

Pasta das prévias: `C:\Users\glaut\VIDEOS IA\_clinica\site-ihfc\_trabalho\previas-premium\` (7 jpg, 1280x800)

## Pendências verificadas (15 páginas, ao vivo + prévia v4)
| Item | Resultado |
|---|---|
| Links e imagens quebrados | nenhum (todos 200) |
| WhatsApp | todos os links usam o mesmo número, 5573981507715, com texto e palavra-chave por área |
| Fotos de exemplo/placeholder, texto faltando | nenhum |
| Celular | sem rolagem lateral, nenhuma imagem quebrada; peso ~0,1–1,4 MB por página (a mais pesada é a v4, com fotos lazy) |
| CFO | sem preço, sem promessa, sem antes/depois. "melhor" aparece só dentro de avaliação de paciente e em "o melhor caminho é a avaliação" |
| **Prévia do link no WhatsApp/Facebook** | **CORRIGIDO e publicado (commit a94f3a4):** antes a imagem era relativa e em .webp, e o WhatsApp não mostrava a foto. Agora todas as páginas usam `img/ihfc-compartilhar-1200x630.jpg` (fachada + logo), com og:url, og:type, og:locale e canonical. Não muda nada na página. |
| Descrições longas (>160 caracteres) em 6 páginas | não corrigido: o Google só corta o texto; dá para ajustar junto com a v4 |
| Retrato do Dr. Mateus | fundo azul, diferente da equipe. Pedir foto no padrão ou tratar o fundo |
| Depoimentos do Google no site | conferir com a regra do CFO sobre depoimentos antes de destacar mais (melhoria 5) |

## Melhorias "mais premium" (cada uma tem prévia em jpg)
1. **Hero com vídeo de bastidor** (`ihfc-site_melhoria01-hero-video-bastidor_previa.jpg`): loop de 20 s, mudo, com grade cinematográfico (recepção, esterilização, consultório). Precisa de filmagem com o celular na clínica.
2. **Escolha guiada em 3 toques** (`…02-escolha-guiada…`): quiz rápido que abre o WhatsApp já com a palavra-chave da área. A recomendação é esta, porque é a que mais converte.
3. **Equipe com filtro por área** (`…03-equipe-por-area…`): botões Face/Corpo/Sorriso… filtram os cartões, combinando com a policlínica.
4. **Bloco "Visite o IHFC"** (`…04-visite-mapa…`): fachada, mapa escuro do Google, horário e botão "Como chegar".
5. **Avaliações do Google em destaque** (`…05-avaliacoes-google…`): nota e número de avaliações reais em carrossel. Não inventar número; conferir o CFO.
6. **Tipografia editorial da ESSÊNCIA** (`…06-tipografia-editorial…`): áreas numeradas 01–07, números grandes, capitular dourada. Site e revista com a mesma identidade.
7. **Tour pela clínica em tela cheia** (`…07-tour-clinica…`): galeria com legendas, podendo incluir o 360° do Google. Faltam fotos novas da recepção, Sala VIP e esterilização.
8. (sem prévia) Retratos da equipe no mesmo padrão: fundo, luz e enquadramento iguais.

Ordem sugerida: 2 → 3 → 4 → 6 (dá para fazer já, sem material novo); 1, 7 e 8 dependem de filmagem ou fotos na clínica.
Nada disso foi publicado: tudo depende do OK do Dr.
