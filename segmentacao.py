import cv2

def segmentar_imagem(gray):

    _, thresh = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    return thresh