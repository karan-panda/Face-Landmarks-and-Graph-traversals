import cv2
import mediapipe as mp
import numpy as np
from keras.models import model_from_json

json_file = open("facialemotionmodel.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("facialemotionmodel.h5")

haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}
facemesh = mp.solutions.face_mesh
face_mesh = facemesh.FaceMesh(static_image_mode=True, min_tracking_confidence=0.6, min_detection_confidence=0.6)
draw = mp.solutions.drawing_utils

def draw_landmarks_on_frame(frame, landmarks):
    for landmark_coordinates in landmarks:
        for landmark_x, landmark_y in landmark_coordinates:
            cv2.circle(frame, (landmark_x, landmark_y), 1, (255, 0, 0), 1)

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    op = face_mesh.process(rgb)
    landmark_positions_frame = []  
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        face_image = gray[y:y + h, x:x + w]
        face_image = cv2.resize(face_image, (48, 48))
        img = extract_features(face_image)
        if op.multi_face_landmarks:
            for face_landmarks in op.multi_face_landmarks:
                landmark_coordinates = []  
                for landmark in face_landmarks.landmark:
                    landmark_x = int(landmark.x * frame.shape[1])
                    landmark_y = int(landmark.y * frame.shape[0])
                    landmark_coordinates.append((landmark_x, landmark_y))

                landmark_positions_frame.append(landmark_coordinates)

                draw.draw_landmarks(frame, face_landmarks, facemesh.FACEMESH_CONTOURS,
                                    landmark_drawing_spec=draw.DrawingSpec(color=(255, 0, 0), circle_radius=1, thickness=1),
                                    connection_drawing_spec=draw.DrawingSpec(color=(0, 255, 0), thickness=1,circle_radius=1))

        pred = model.predict(img)
        prediction_label = labels[pred.argmax()]
        cv2.putText(frame, '%s' % (prediction_label), (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) in [ord('q'), 27]: 
        break

cap.release()
cv2.destroyAllWindows()
