import cv2
import mediapipe as mp
import numpy as np
from pymongo import MongoClient
import networkx as nx

# Function to draw landmarks on the frame
def draw_landmarks_on_frame(frame, landmarks):
    for landmark_coordinates in landmarks:
        for landmark_x, landmark_y in landmark_coordinates:
            cv2.circle(frame, (landmark_x, landmark_y), 2, (255, 0, 0), -1)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['landmark_database']
collection = db['landmark_positions']

# Retrieve landmark positions data for frame 0
frame_0_data = collection.find_one({"frame": 0})
landmark_positions_frame_0 = frame_0_data["landmarks"]

# Create a graph representation of the face landmarks
G = nx.Graph()
for landmark_coordinates in landmark_positions_frame_0:
    for i, (landmark_x, landmark_y) in enumerate(landmark_coordinates):
        G.add_node(i, pos=(landmark_x, landmark_y))
    for i in range(len(landmark_coordinates) - 1):
        G.add_edge(i, i+1)

# Perform a graph traversal (DFS) to create a traversal path
traversal_path = list(nx.dfs_edges(G, source=0))

# Draw the face using traversal path with animation
frm = np.zeros((480, 640, 3), dtype=np.uint8)  # Creating an empty frame
draw_landmarks_on_frame(frm, landmark_positions_frame_0)  # Draw face landmarks

# Animation of the traversal path
for u, v in traversal_path:
    cv2.line(frm, G.nodes[u]['pos'], G.nodes[v]['pos'], (200, 200, 200), 1)  # Change color and reduce thickness of traversal path
    cv2.imshow("Face Traversal Animation (DFS)", frm)
    key = cv2.waitKey(100)  # Delay (milliseconds) between each step of the animation
    if key == 27:
        break

cv2.destroyAllWindows()
