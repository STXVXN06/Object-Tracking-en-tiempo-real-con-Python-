# importamos las librerias

import cv2
import numpy as np

# Nodos de ejecucion

# vc = 0 --> 48 # Captura de video
# vc = 1 --> 49 # Filtro desenfoque
# vc = 2 --> 50 # Filtro detector de esquinas
# vc = 3 --> 51 # Filtro de bordes


# Parametros para detector de esquinas
esquinas_param = dict(maxCorners = 500,     # Maximo numero de esquinas a detectar
                      qualityLevel = 0.2,   # Umbral minimo para deteccion de esquinas
                      minDistance = 15,     # Distancia entre pixeles
                      blockSize = 9)        # Area de pixeles




# Modo
mood = 48

# Creamos la Video Captura
cap = cv2.VideoCapture(0)

# DCreamos un ciclo para ejecutar los frames
while True:
    # Leemos los frames
    ret, frame = cap.read()

    # DEcidimos el mood
    # Normal
    if mood == 48:
        # Mostramos los frames
        resultado = frame

    # Desenfoque
    elif mood == 49:
        # Modificamos frames
        resultado = cv2.blur(frame, (15, 15)) # (5,5) es k¿la mascara de deenfoque se usará,
                                                  # Entre mayor sean lo snumero mayor sera el desenfoque

    # Bordes
    elif mood == 51:
        # Modificamos frames
        resultado = cv2.Canny(frame, 80, 120) # UMbral inferior y umbral  superior
                                            # Si el gradiente de intensidad supera el umbral superior
                                            # Es considerado como un borde, tambien si esta por debajo
                                            # Del umbral inferior es un bnorde


    # Filtro detector de esquinas
    elif mood == 50:
        # Obtenemos los frames
        resultado = frame

        # Conversion a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculamos las caracteristicas de las esquinas
        esquinas = cv2.goodFeaturesToTrack(gray, **esquinas_param)

        # Preguntamos si detectamos esquinas con esas caracteristicas
        if esquinas is not None:


            # Iteramos32
            for x,y in np.float32(esquinas).reshape(-1,2):
                # Convertimos en enteros
                x,y = int(x), int(y)

                # Dibujamos la ubicacion de las esquinas
                cv2.circle(resultado, (x,y), 10, (255,0,0), 1)


    # Si presionamos otra tecla
    elif mood != 48 or mood != 49 or mood != 50 or mood != 51 or mood != -1:
        # NO hacemos nada
        resultado = frame

        # Imprimimos mensaje
        print("TECLA INCORRECTA")



    # Mostramos los frames
    cv2.imshow("VIDEO CAPTURA", resultado)

    # Cerramos con lectura de teclado
    t = cv2.waitKey(1)
    # Salimos
    if t == 27:
        break

    # Modificamo mood
    elif t != -1:
        mood = t


# LIberamos la VIDEOCAPTURA
cap.release()

# Cerramos la ventana
cv2.destroyAllWindows()