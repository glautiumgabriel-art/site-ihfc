# Equipe no site IHFC: de onde veio cada dado (27/10/2026, L-318)

Regra: nome, registro e foto só valem se vieram do Dr., da própria pessoa ou do Simples Dental. O que veio da web sai do site até confirmar.
Fontes conferidas:
- Simples Dental: backup em D:/IHFC-Sistema, tabelas `profissionais` e `profissional`.
- Revista: anotações de origem em `_clinica/revista-essencia/material/dados.json`.
- Fotos: a maioria veio dos posts de equipe do Instagram oficial do IHFC (`material/instagram/ihfc-equipe-N.jpg`).

| Profissional no site | Nome | Registro | Foto | O que foi feito |
|---|---|---|---|---|
| Dr. Glautium Gabriel | Simples ✔ | CRO-BA 16384: Simples ✔ | Instagram IHFC | mantido |
| Dr. Mateus | Dr. (só "Dr. Mateus") | **saiu** CRM-BA 49804 (era de outra pessoa, achada na web) | **trocada** pela foto que o Dr. mandou hoje (recortada sem a marca "Hairzy" da camisa) | corrigido em todas as páginas; @ não estava no site. Obs.: o Simples tem um "Matheus Carvalho"; confirmar se é ele |
| Dra. Jéssica Lopes | Simples ✔ (Jéssica Lopes Santos) | **saiu** CRBM 42499 (post da própria @dra.jessicalopees), porque o Simples diz **CRBM 15493**. Os dois não batem: confirmar qual vale | Instagram IHFC | registro em branco até confirmar |
| Dra. Ionara Caroso | Simples ✔ (Ionara Novaes Caroso) | **saiu** CRM-BA 16679 (posts de outras clínicas na web) | `ionara-caroso-1.jpg`, origem não anotada: **confirmar** | registro em branco |
| Dr. Hudson D. Soares | Simples ✔ (Hudson Dias Soares) | **saiu** CRO-BA 23283 (sem fonte anotada; Simples sem número) | Instagram IHFC | registro em branco |
| Dra. Juliana Coelho Moreno | Simples ✔ | **saiu** CRO-BA 27601 (sem fonte anotada) | Instagram IHFC | registro em branco |
| Sabrina Amparo | Simples ✔ (Sabrina Kelly Amparo da Silva) | **saiu** CRN-5 20406 (sem fonte anotada) | Instagram IHFC | registro em branco |
| Gisele Gomes | Simples ✔ | CREFITO-7 441870-F: Simples ✔ | Instagram IHFC | mantido |
| Maria Eduarda Brisola | Simples ✔ | sem registro | "foto do site" antigo, origem não anotada: **confirmar** | mantido |
| Maria Neuza | Simples ✔ (Maria Neuza Pires Soares) | sem registro | Instagram IHFC | mantido |
| Natieli Batista | grafia **corrigida** de "Natielli" para "Natieli", como no Simples | sem registro no site | Instagram IHFC | Função a confirmar: o site diz massoterapeuta, mas em `_clinica/equipe-docs` há um documento de COREN (enfermagem) |

Para confirmar com o Dr. ou com cada profissional:
- registros de Ionara, Hudson, Juliana e Sabrina;
- qual é o CRBM da Jéssica;
- CRM e sobrenome do Dr. Mateus;
- função da Natieli;
- origem das fotos da Ionara e da Maria Eduarda.

Dado confirmado volta a aparecer assim: editar `_trabalho/gerar_frentes.py`, editar index/novo/procedimentos e publicar.
