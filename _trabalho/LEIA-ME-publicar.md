# Publicar o site IHFC sem erro (para qualquer modelo)

Tudo de dentro de `_clinica/site-ihfc`.

## Mudar algo e publicar
1. Edite o GERADOR, nunca o .html gerado (o topo do .html diz qual é): home = `montar_v5.py`, páginas por procedimento = `gerar_frentes.py`, páginas de anúncio = `gerar_lp.py`, equipe = `montar_equipe.py`.
2. Rode o gerador (ex.: `cd _trabalho && python gerar_lp.py && cd ..`).
3. `python _trabalho/publicar.py publicar "o que mudou" arquivo1.html arquivo2.html`
   - confere: noindex fora do lugar, link quebrado, sitemap, WhatsApp fixo, alt de imagem, JSON-LD, afirmação clínica sem fonte, arquivo proibido no repositório público;
   - commita SÓ os arquivos citados (nunca `git add -A`: tem tarefa automática publicando o mestre no mesmo repositório);
   - espera cada página ficar igual no ar (até 5 min).

**Pronto quando:** aparece `NO AR` para cada arquivo. `ATRASO` = fila do GitHub Pages: confira em 10 min, não republique.

## Página de anúncio nova (procedimento novo)
Copie um bloco de `LPS` em `gerar_lp.py` (arq `lp-<nome>.html`, chave em MAIÚSCULAS sem acento, pasta, título, h1, dor, foto existente em `img/`, itens só do `CATALOGO-IHFC.md`, quem com CRO/CRM). Rode o gerador e publique como acima. Nada de preço, "grátis", promessa ou tempo de recuperação (CFO). Antes e depois/depoimentos entram sozinhos quando a recepção puser o material aprovado em `_aprovados/<pasta>/aprovado.json`.

## Nunca
- Foto de paciente sem `termo_assinado: true` no aprovado.json; foto de banco/IA como resultado.
- Arquivo interno (pedido, planilha, nome de paciente) dentro desta pasta: o repositório é PÚBLICO. Use `_conhecimento/marketing-clinica/`.

## Sobe de modelo quando
- `publicar.py` para com erro e a correção não é óbvia na fonte (gerador) depois de 1 tentativa;
- precisa mudar layout/CSS, criar gerador novo ou mexer em JSON-LD/pixel;
- `push` falha 2 vezes ou o `ATRASO` dura mais de 30 min.

Teste provado (13/11): a versão de `corpo.html` de antes do commit 0a7def4 (com noindex) faz `publicar.py conferir` parar com `corpo.html: tem noindex…`; a atual passa.
