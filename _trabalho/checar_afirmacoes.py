"""Trava L-362: antes de publicar, nenhuma afirmação clínica sem fonte (anestesia, medicação, tempo,
frequência, recuperação, promessa). Rodar: python _trabalho/checar_afirmacoes.py  (sai com erro se achar)."""
import re, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
PROIBIDO = [r'anestesia', r'na maioria das vezes', r'geralmente', r'normalmente', r'em média', r'\d+\s*(minutos|horas|dias|semanas|meses)',
            r'em poucos dias', r'poucas sessões', r'recuperação rápida', r'volta à rotina', r'sem dor', r'indolor',
            r'resultado definitivo', r'garant', r'teste alérgico', r'midazolam', r'clonazepam', r'não faz (tratamento|nada|procedimento)', r'às vezes']  # L-nova 28/10: nunca dizer o que o Dr. não faz
LIBERADO = [r'em até 15 dias',  # privacidade (LGPD), não é afirmação clínica
            r'não some em duas semanas',  # sinal de alerta de lesão na boca, aprovado na página do Dr.
            r'garanta sua vaga', r'às vezes com respostas automáticas', r'climatizado 24 horas']  # inscrição em curso e estrutura da clínica, não são afirmações clínicas
erros = 0
for arq in sorted(list(raiz.glob('*.html')) + [raiz / 'queixas.js']):
    texto = re.sub(r'<[^>]+>', ' ', arq.read_text(encoding='utf-8'))
    for p in PROIBIDO:
        for m in re.finditer(p, texto, re.I):
            trecho = texto[max(0, m.start() - 70):m.end() + 50].replace('\n', ' ')
            if any(re.search(l, trecho, re.I) for l in LIBERADO):
                continue
            print(f'SEM FONTE?  {arq.name}: ...{trecho.strip()}...'); erros += 1
print('ok, nenhuma afirmação clínica suspeita' if not erros else f'{erros} trecho(s) para conferir com o Dr.')
sys.exit(1 if erros else 0)
