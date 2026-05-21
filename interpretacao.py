import numpy as np

def analisar_imagem(gray, contagem):

    brilho = np.mean(gray)

    if brilho < 60:
        iluminacao = "Imagem escura"

    elif brilho > 180:
        iluminacao = "Imagem muito clara"

    else:
        iluminacao = "Iluminacao normal"

    total = sum(contagem.values())

    if total == 0:
        objetos = "Nenhum animal detectado"

    else:
        objetos = f"{total} animal(is) detectado(s)"

    return iluminacao, objetos