# -*- coding: utf-8 -*-

import cv2
import tkinter as tk

from processamento import processar_imagem, aplicar_hsv
from yolo_detector import detectar_animais
from histograma import mostrar_histograma
from segmentacao import segmentar_imagem
from interpretacao import analisar_imagem
from interface import App


# =========================
# IMAGEM BASE
# =========================

frame = cv2.imread("animal.jpg")

if frame is None:
    print("Erro: imagem não encontrada")
    exit()

frame = cv2.resize(frame, (800, 600))


# =========================
# HISTOGRAMA
# =========================

mostrar_histograma(frame)


# =========================
# PROCESSAMENTO
# =========================

gray, blur, edges, sharpen = processar_imagem(frame)

mask, h, s, v = aplicar_hsv(frame)

thresh = segmentar_imagem(gray)


# =========================
# YOLO (FRAME ORIGINAL LIMPO + FRAME DETECTADO)
# =========================

frame_original = frame.copy()

frame_yolo, contagem, recortes = detectar_animais(frame)


# =========================
# INTERPRETAÇÃO IA
# =========================

iluminacao, objetos = analisar_imagem(gray, contagem)


# =========================
# INTERFACE
# =========================

root = tk.Tk()

app = App(root)

app.atualizar(
    frame_original,
    frame_yolo,
    gray,
    blur,
    edges,
    sharpen,
    mask,
    thresh,
    contagem,
    iluminacao,
    objetos,
    recortes
)

root.mainloop()