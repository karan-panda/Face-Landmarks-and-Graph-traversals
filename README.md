# FaceLandmark Tracker, Graph Traversal Visualizer & Emotion Detection 🎯🔍😃

This application combines face landmark tracking with graph traversal visualization. It allows users to track 468 landmarks of a face in a video, store the landmark data in MongoDB, and replay the landmark motion. Additionally, users can visualize graph traversal algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), A* algorithm, and Dijkstra's algorithm across the landmarks.

The machine learning model added for emotion recognition is trained on facial expression data, and it classifies each face into one of seven categories: 'angry', 'disgust', 'fear', 'happy', 'neutral', 'sad' and 'surprise', this feature further enhances the abilty of the application making it more versatile.

## Installation and Usage 🛠️📝

### Installation

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:

```
git clone https://github.com/karan-panda/Face-Landmarks-and-Graph-traversals
```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies by running:
```
pip install -r requirements.txt
```

4. **Ensure MongoDB is Running**: Make sure MongoDB is running locally on your machine. If not, start the MongoDB service.

### Usage

To use the application, follow these steps:

1. **Run the GUI Application**: Launch the graphical user interface (GUI) by running the `main.py` script:
```
python main.py
```

3. **Click on Landmark Generator**: To track face landmarks in a video, click on the "Landmark Generator" button. This will initiate the process of detecting and tracking 468 landmarks of a face in the video.

4. **Replay Landmark Motion**: After generating the landmarks, you can replay the motion of face landmarks by clicking on the "Landmark Motion Visualizer" button. This will visualize the tracked landmarks and their motion.

5. **Explore Graph Traversal Algorithms**:
 - **DFS (Depth-First Search)**: Click on the "DFS" button to visualize the Depth-First Search traversal across the landmarks.
 - **BFS (Breadth-First Search)**: Click on the "BFS" button to visualize the Breadth-First Search traversal across the landmarks.
 - **Dijkstra's Algorithm**: Click on the "Dijkstra's" button to visualize the Dijkstra's algorithm traversal across the landmarks.
 - **A* Algorithm**: Click on the "A*" button to visualize the A* algorithm traversal across the landmarks.

5. **Select and Run Other Scripts**: You can also select and run custom Python scripts by clicking on the "Select and Run Other Script" button. This allows you to explore additional functionalities or customize the application according to your requirements.

6. **Enjoy the Application**: Explore the capabilities of the application and enjoy visualizing face landmark tracking and graph traversal algorithms!

## Features 🚀

- **Face Landmark Tracking**: Utilizes MediaPipe to detect and track 468 landmarks of a face in a video.
- **Emotion Detection**: Uses machine learning to detect seven emotions based on facial expressions.
- **MongoDB Integration**: Stores the face landmark data of each frame in MongoDB for future reference.
- **Landmark Motion Replay**: Users can replay the motion of face landmarks from stored data.
- **Graph Traversal Visualization**: Offers visualization of BFS, DFS, A*, and Dijkstra's algorithm traversing across the landmarks.

## Tech Stack 💻

- Python 🐍
- MediaPipe 🎥
- OpenCV 🖼️
- NumPy 🔢
- pymongo 📁
- NetworkX 📊
- Machine Learning 🧠