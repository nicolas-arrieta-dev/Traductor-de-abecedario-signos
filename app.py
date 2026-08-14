from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import cv2
import tensorflow as tf
import numpy as np
import mediapipe as mp
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Crear carpeta uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Mapeo índice a letra
class_to_letter = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
    25: 'Z'
}

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Cargar modelo TensorFlow SavedModel
model = tf.saved_model.load("./model_saved")
infer = model.signatures['serving_default']

def preprocess_image_for_model(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img_norm = img_resized / 255.0
    img_expanded = np.expand_dims(img_norm, axis=0).astype(np.float32)
    return img_expanded

def predict_letter(image):
    input_tensor = tf.convert_to_tensor(preprocess_image_for_model(image))
    outputs = infer(input_tensor)
    prediction = list(outputs.values())[0].numpy()
    predicted_index = np.argmax(prediction)
    return class_to_letter.get(predicted_index, '?')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'})

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    image = cv2.imread(filepath)
    if image is None:
        return jsonify({'error': 'Failed to read uploaded image'})

    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.multi_hand_landmarks:
        return jsonify({'error': 'No hand detected'})

    hand_landmarks = results.multi_hand_landmarks[0]

    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    h, w, _ = image.shape
    coords = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]
    x_vals = [pt[0] for pt in coords]
    y_vals = [pt[1] for pt in coords]

    margin = 60  # Aumenté el margen de 20 a 60 pixeles
    x_min, x_max = max(min(x_vals) - margin, 0), min(max(x_vals) + margin, w)
    y_min, y_max = max(min(y_vals) - margin, 0), min(max(y_vals) + margin, h)

    roi = image[y_min:y_max, x_min:x_max]

    pred_letter = predict_letter(roi)

    # Dibujar rectángulo con margen más grande
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)

    processed_filename = f'processed_{filename}'
    processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
    cv2.putText(image, f'Letra: {pred_letter}', (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imwrite(processed_path, image)

    return jsonify({
        'letter': pred_letter,
        'original': filename,
        'processed': processed_filename
    })

@app.route('/video_feed')
def video_feed():
    def generate():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("No se pudo abrir la cámara")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Voltear horizontalmente para efecto espejo
            frame = cv2.flip(frame, 1)

            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            pred_letter = ''

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                h, w, _ = frame.shape
                coords = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]
                x_vals = [pt[0] for pt in coords]
                y_vals = [pt[1] for pt in coords]

                margin = 40  # Aquí también margen aumentado
                x_min, x_max = max(min(x_vals) - margin, 0), min(max(x_vals) + margin, w)
                y_min, y_max = max(min(y_vals) - margin, 0), min(max(y_vals) + margin, h)

                roi = frame[y_min:y_max, x_min:x_max]

                if roi.size != 0:
                    try:
                        pred_letter = predict_letter(roi)
                    except Exception as e:
                        print("Error en predicción:", e)
                        pred_letter = '?'

                # Dibujar rectángulo con margen más grande
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)

                cv2.putText(frame, f'Letra: {pred_letter}', (x_min, y_min - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            frame_bytes = jpeg.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        cap.release()

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
