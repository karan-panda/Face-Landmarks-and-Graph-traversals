import cv2
import mediapipe as mp
import numpy as np
import time
from pymongo import MongoClient

# Function to draw landmarks on the frame
def draw_landmarks_on_frame(frame, landmarks):
    for landmark_coordinates in landmarks:
        for landmark_x, landmark_y in landmark_coordinates:
            cv2.circle(frame, (landmark_x, landmark_y), 1, (255, 0, 0), 1)

cap = cv2.VideoCapture(0)

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode=True, min_tracking_confidence=0.6, min_detection_confidence=0.6)
draw = mp.solutions.drawing_utils

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['landmark_database']
collection = db['landmark_positions']

# Delete all existing data from MongoDB
collection.delete_many({})

# List to store landmark coordinates over time
landmark_positions_over_time = []

# Variable to keep track of time
start_time = time.time()

while True:
    _, frm = cap.read()
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)

    op = face.process(rgb)
    landmark_positions_frame = []  # List to store landmark coordinates for this frame

    if op.multi_face_landmarks:
        for face_landmarks in op.multi_face_landmarks:
            # List to store landmark coordinates for this face
            landmark_coordinates = []

            for landmark in face_landmarks.landmark:
                # Extracting X and Y coordinates of each landmark
                landmark_x = int(landmark.x * frm.shape[1])  # Scaling by frame width
                landmark_y = int(landmark.y * frm.shape[0])  # Scaling by frame height
                landmark_coordinates.append((landmark_x, landmark_y))

            landmark_positions_frame.append(landmark_coordinates)

            draw.draw_landmarks(frm, face_landmarks, facemesh.FACEMESH_CONTOURS, 
                                landmark_drawing_spec=draw.DrawingSpec(color=(255, 0, 0), circle_radius=1, thickness=1), 
                                connection_drawing_spec=draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1))

    # Appending landmark positions for this frame to the list
    landmark_positions_over_time.append(landmark_positions_frame)

    cv2.imshow("window", frm)

    # Exit loop when 'Esc' key is pressed
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

# Store the landmark positions in MongoDB
for i, frame_landmarks in enumerate(landmark_positions_over_time):
    collection.insert_one({"frame": i, "landmarks": frame_landmarks})

# Calculate the duration of the captured video
end_time = time.time()
duration = end_time - start_time

print("Data stored in MongoDB.")