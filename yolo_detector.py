# -*- coding: utf-8 -*-
from ultralytics import YOLO
import cv2

model = YOLO("yolov8l.pt")

animais = ["cat", "dog", "bird", "horse", "cow", "sheep"]

# Nome sem acento (OpenCV não suporta bem)
nomes_cv2 = {
    "dog": "Cachorro",
    "cat": "Gato",
    "bird": "Passaro",
    "horse": "Cavalo",
    "cow": "Vaca",
    "sheep": "Ovelha"
}

def detectar_animais(frame):
    results = model(frame)

    contagem = {}
    recortes = []

    for r in results:
        for box in r.boxes:

            conf = float(box.conf[0])

            if conf > 0.5:
                cls = int(box.cls[0])
                nome = model.names[cls]

                if nome in animais:
                    contagem[nome] = contagem.get(nome, 0) + 1

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Caixa rosa
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 3)

                    # Nome na imagem principal
                    nome_pt = nomes_cv2.get(nome, nome)

                    cv2.putText(frame, nome_pt,
                                (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (255,0,255),
                                2)

                    # Recorte do animal
                    corte = frame[y1:y2, x1:x2].copy()
                    recortes.append((nome, corte))

    return frame, contagem, recortes