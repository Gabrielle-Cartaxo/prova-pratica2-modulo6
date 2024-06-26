
from flask import Flask, Response, send_from_directory
import cv2
import threading
import numpy as np

app = Flask(__name__)

# Inicializar os Haar Cascades. Nesse caso, estou utilizando dois deles: o que detecta os rostos que estão frontais e o que detecta os que estão de perfil.
frontal_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

# Verificar se carregou certinho
if frontal_face_cascade.empty():
    print("Erro: O classificador de detecção de rostos frontal não pôde ser carregado.")
if profile_face_cascade.empty():
    print("Erro: O classificador de detecção de rostos de perfil não pôde ser carregado.")

# Pegar os frames do vídeo
cap = cv2.VideoCapture('video.mp4')
cap_lock = threading.Lock()

@app.route("/")
def read_root():
    try:
        return send_from_directory('.', 'index.html')
    except Exception as e:
        return str(e), 500

@app.route("/stream")
def stream():
    return Response(generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_video():
    while True:
        with cap_lock:
            ret, frame = cap.read()
        if not ret:
            print("Erro: Não foi possível ler o frame.")
            break

        # Converter a imagem para escala de cinza pq assim o haar funciona melhor
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Detectar rostos frontais!!!
        if not frontal_face_cascade.empty():
            # Detectar rostos frontais na imagem
            frontal_faces = frontal_face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
            # Desenhar retângulos >>vermelhos<< em rostos frontais
            for (x, y, w, h) in frontal_faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        #Detectar rostos de perfil!!!
        if not profile_face_cascade.empty():
            # Detectar rostos de perfil na imagem
            profile_faces = profile_face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
            # Desenhar retângulos >>verdes<< em rostos de perfil
            for (x, y, w, h) in profile_faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Transformar os frames em jpeg
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        # Definir o delimitador de frames
        boundary = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'

        # Enviar o frame com o delimitador
        yield boundary + frame_bytes + b'\r\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
