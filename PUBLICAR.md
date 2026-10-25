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
