import cv2 as cv
import numpy as np
import base64

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

limitesDasCores = {
    'rosa': [[173, 199, 188], [178, 255, 255]],
    'prata': [[0, 0, 107], [173, 34, 189]]
}

cores = ['rosa', 'prata']
cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0)
cap.set(cv.CAP_PROP_EXPOSURE, -5)

def analisaImagem():
    _, frame = cap.read()
    _, frame = cap.read()
    recorte = frame[34:115, 496:591]
    frameHSV = cv.cvtColor(recorte, cv.COLOR_BGR2HSV)
    dados = np.array([])
    for limite in limitesDasCores:
        mask = cv.inRange(
            frameHSV,
            np.array(limitesDasCores[limite][0], dtype=np.uint8),
            np.array(limitesDasCores[limite][1], dtype=np.uint8)
        )
        dados = np.append(dados, np.sum(mask != 0))
    if dados.max() > 3500:
        cor = cores[dados.argmax()]
    else:
        cor = 'preto'
    print(cor)
    # cv.imwrite('imagem.jpg', frame)

    _, buffer = cv.imencode('.png', frame)
    frame64 = base64.b64encode(buffer)
    string64 = frame64.decode('ascii')
    return frame, recorte, string64, cor

if __name__ == '__main__':
    while True:
        frame, recorte, _, _ = analisaImagem()
        cv.rectangle(frame, (496, 34), (591, 115), (0, 0, 255), 2)
        cv.imshow('bgr', frame)
        cv.imshow('recorte', recorte)
        tecla = cv.waitKey(1)
        if tecla == ord('q'):
            break
        elif tecla == ord('z'):
            limMax = [0, 0, 0]
            limMin = [180, 255, 255]
