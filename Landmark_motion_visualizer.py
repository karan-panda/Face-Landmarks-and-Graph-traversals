import cv2
import numpy as np
import time
from pymongo import MongoClient

# Function to draw landmarks on the frame
def draw_landmarks_on_frame(frame, landmarks):
    for landmark_coordinates in landmarks:
        for landmark_x, landmark_y in landmark_coordinates:
            cv2.circle(frame, (landmark_x, landmark_y), 1, (255, 0, 0), 1)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['landmark_database']
collection = db['landmark_positions']

# Retrieve data from MongoDB
landmark_positions_over_time = []
for document in collection.find().sort("frame", 1):
    landmark_positions_over_time.append(document["landmarks"])

# Replay the motion using the loaded landmark positions
for landmarks_frame in landmark_positions_over_time:
    frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black frame
    draw_landmarks_on_frame(frame, landmarks_frame)
    cv2.imshow("Replay", frame)
    cv2.waitKey(30) 

cv2.destroyAllWindows()
