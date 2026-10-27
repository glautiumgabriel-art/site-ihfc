# Publicar o site do IHFC em www.ihfc.com.br

Situação em 25/10/2026: o domínio ihfc.com.br está registrado na Super Domínios e "estacionado" (servidores ns1/ns2.sdparking.com.br, página "Em breve"). O site fica hospedado de graça no GitHub Pages (conta glautiumgabriel-art, repositório `site-ihfc`).

**Conta da Super Domínios:** e-mail **ihfcjequie@gmail.com** (titular IHFC, CNPJ 39.698.984/0001-61, conforme Registro.br em 25/10/2026). Domínio registrado em 23/10/2025 e **vencido em 23/10/2026**: renovar antes de mexer no DNS.

## 1. GitHub (feito em 25/10/2026: repositório glautiumgabriel-art/site-ihfc + Pages ligado) (Claude faz, com o OK do Dr.)
- Criar o repositório público `glautiumgabriel-art/site-ihfc` e enviar esta pasta (já é um repositório git com o arquivo `CNAME` = www.ihfc.com.br).
- Ligar o GitHub Pages: ramo `main`, pasta `/`, domínio próprio `www.ihfc.com.br`, HTTPS obrigatório.

## 2. DNS na Super Domínios (precisa do login do Dr.)
No painel do domínio ihfc.com.br, zona DNS:

| Tipo | Nome | Valor |
|---|---|---|
| A | @ (ihfc.com.br) | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | glautiumgabriel-art.github.io |

Apagar o registro A antigo (208.115.225.220) do @ e do www. Se o painel não deixar editar a zona com os servidores "sdparking", primeiro trocar os servidores DNS para os da hospedagem DNS da Super Domínios (ou Registro.br).

## 3. Conferir
Em até algumas horas: https://www.ihfc.com.br abre o site, com cadeado (HTTPS).

## Atualizar o site depois
Editar os arquivos aqui, `git commit` e `git push`; o GitHub Pages publica sozinho em ~1 minuto.

## v4 em prévia (27/10/2026)
Situação real em 27/10: domínio renovado até **23/10/2027** (Registro.br) e site no ar com HTTPS. Nada a pagar.

Páginas novas (todas com `noindex` até o OK do Dr.):
- Prévia da nova página inicial: https://www.ihfc.com.br/novo.html
- Procedimentos completos: procedimentos.html · Dr. Glautium: dr-glautium.html · Revista: essencia.html
- Uma página por frente (gerador `_trabalho/gerar_frentes.py`, editar lá): papada-e-rosto, sorriso, implante, corpo, tricologia, nutricao, pele. WhatsApp com PALAVRA-CHAVE no início da mensagem (lista em `_trabalho/links-whatsapp-por-frente.md`).
- Já valendo: privacidade.html (Meta: URL da política e da exclusão de dados = privacidade.html#exclusao) e links.html (bio do Instagram e QR).
- Revista no site: só páginas sem antes/depois, sem nome de remédio e sem espaço de foto vazio.

### Quando o Dr. aprovar
1. `novo.html` vira `index.html` (guardar o antigo como `_trabalho/index-v3.html`).
2. Em todos os .html e no gerador: trocar `novo.html` por `./` e apagar a linha `<meta name="robots" content="noindex">`.
3. `git commit` + `git push`; conferir https://www.ihfc.com.br.

## v5 enxuta (27/10, pedido do Dr.: "muito poluído e grande")
Prévia: https://www.ihfc.com.br/v5.html (gerada por `_trabalho/montar_v5.py` a partir do novo.html). Se aprovada, ela vira a index.html no lugar da v4: guardar o index antigo em `_trabalho/`, trocar `v5.html` por `./`, tirar o noindex e publicar.
