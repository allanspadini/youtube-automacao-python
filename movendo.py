import os
import shutil

origem = "/home/allan/Downloads"
destino = {
    ".png": "/home/allan/Imagens",
    ".pdf": "/home/allan/Documentos",
    ".mp4": "/home/allan/Vídeos"
}

for arquivo in os.listdir(origem):
    extensao = os.path.splitext(arquivo)[1].lower()
    if extensao in destino:
        pasta_destino = destino[extensao]
        os.makedirs(pasta_destino, exist_ok=True)
        shutil.move(os.path.join(origem, arquivo),
                    os.path.join(pasta_destino, arquivo))

print("Arquivos organizados automaticamente!")
