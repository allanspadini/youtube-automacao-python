import os

pasta = "/home/allan/Imagens/capturas_de_tela/"
arquivos = os.listdir(pasta)

for i, nome in enumerate(arquivos, start=1):
    extensao = os.path.splitext(nome)[1]
    novo_nome = f"Captura_{i}{extensao}"
    os.rename(os.path.join(pasta, nome), os.path.join(pasta, novo_nome))

print("Arquivos renomeados com sucesso!")
