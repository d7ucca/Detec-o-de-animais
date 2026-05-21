# -*- coding: utf-8 -*-

import cv2
import numpy as np


# ======================================
# PROCESSAMENTO PRINCIPAL
# ======================================

def processar_imagem(frame):

    # brilho e contraste
    frame = cv2.convertScaleAbs(
        frame,
        alpha=1.3,
        beta=25
    )

    # escala de cinza
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # redução de ruído
    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # detecção de bordas
    edges = cv2.Canny(
        blur,
        50,
        150
    )

    # filtro de nitidez
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharpen = cv2.filter2D(
        frame,
        -1,
        kernel
    )

    return gray, blur, edges, sharpen


# ======================================
# HSV + MÁSCARA DE COR
# ======================================

def aplicar_hsv(frame):

    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )

    # separação dos canais
    h, s, v = cv2.split(hsv)

    # intervalo de cores
    lower = np.array([0, 50, 50])
    upper = np.array([180, 255, 255])

    # máscara
    mask = cv2.inRange(
        hsv,
        lower,
        upper
    )

    # redução de ruído na máscara
    kernel = np.ones((5,5), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    return mask, h, s, v