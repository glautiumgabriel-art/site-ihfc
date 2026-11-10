# Republica o ARQUIVO MESTRE DAS IAs no site (mesmo caminho secreto). Uso: python republicar_mestre_ias.py
import shutil, subprocess, pathlib, sys
raiz = pathlib.Path(__file__).resolve().parent.parent
d = raiz / (raiz / "_trabalho" / "caminho_mestre_ias.txt").read_text().strip()
src = pathlib.Path(r"C:/Users/glaut/VIDEOS IA/_conhecimento/conselho")
shutil.copyfile(src / "ARQUIVO-MESTRE-DAS-IAS.html", d / "index.html")
shutil.copyfile(src / "ARQUIVO-MESTRE-DAS-IAS.txt", d / "mestre.txt")
rel = d.relative_to(raiz).as_posix()
run = lambda *a: subprocess.run(["git", "-C", str(raiz), *a], check=False)
run("add", rel)
if subprocess.run(["git", "-C", str(raiz), "diff", "--cached", "--quiet", "--", rel]).returncode:
    run("commit", "-m", "Arquivo mestre das IAs (atualização)", "--", rel)
    run("push")
print("https://www.ihfc.com.br/" + rel + "/  e  .../mestre.txt")
