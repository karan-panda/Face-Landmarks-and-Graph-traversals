import tkinter as tk
from tkinter import filedialog
import subprocess

def run_script(script_path):
    subprocess.Popen(['python', script_path])

def select_script():
    file_path = filedialog.askopenfilename(filetypes=[('Python scripts', '*.py')])
    if file_path:
        run_script(file_path)

root = tk.Tk()
root.title("FaceLandmark Tracker & Graph Traversal Visualizer")
root.geometry("400x500")

button_frame = tk.Frame(root)
button_frame.pack(pady=20)
button_style = {'padx': 20, 'pady': 10, 'width': 20}

btn_landmark_generator = tk.Button(button_frame, text="Landmark Generator", command=lambda: run_script('Landmark_generator.py'), **button_style)
btn_landmark_generator.grid(row=0, column=0, pady=5)

btn_landmark_motion_visualizer = tk.Button(button_frame, text="Landmark Motion Visualizer", command=lambda: run_script('Landmark_motion_visualizer.py'), **button_style)
btn_landmark_motion_visualizer.grid(row=1, column=0, pady=5)

btn_emotion_detection = tk.Button(button_frame, text="Realtime Emotion Detection", command=lambda: run_script('RealtimeEmotionDetection.py'), **button_style)
btn_emotion_detection.grid(row=2, column=0, pady=5)

# Button to select and run DFS script
btn_dfs = tk.Button(button_frame, text="DFS", command=lambda: run_script('DFS.py'), **button_style)
btn_dfs.grid(row=3, column=0, pady=5)

# Button to select and run BFS script
btn_bfs = tk.Button(button_frame, text="BFS", command=lambda: run_script('BFS.py'), **button_style)
btn_bfs.grid(row=4, column=0, pady=5)

# Button to select and run Dijkstra's script
btn_dijkstra = tk.Button(button_frame, text="Dijkstra's", command=lambda: run_script('Djikstra_algo.py'), **button_style)
btn_dijkstra.grid(row=5, column=0, pady=5)

# Button to select and run A* script
btn_astar = tk.Button(button_frame, text="A*", command=lambda: run_script('A_star.py'), **button_style)
btn_astar.grid(row=6, column=0, pady=5)

# Button to select and run any other script
btn_select_script = tk.Button(root, text="Select and Run Other Script", command=select_script)
btn_select_script.pack(pady=10)

root.mainloop()
