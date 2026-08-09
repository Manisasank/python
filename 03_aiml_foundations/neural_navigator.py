import cv2
import numpy as np
from ultralytics import YOLO
import sys

# 1. Initialize YOLOv8 Model
model = YOLO("yolov8n.pt")
TARGET_CLASSES = [0, 2, 7] # 0: Person, 2: Car, 7: Truck

# 2. Initialize Camera Video Capture
cap = cv2.VideoCapture(0)

# 3. Simulation Variables
width, height = 800, 600
road_y = 300
car_x = 50
car_speed = 4
safe_braking_dist = 220
obstacle_x = 650

print("==================================================")
print("INTEGRATED NEURAL NAVIGATOR PIPELINE RUNNING")
print("Point your camera at a person, car, or phone screen with a car photo!")
print("Press 'q' inside the window to exit.")
print("==================================================")

while cap.isOpened():
    success, camera_frame = cap.read()
    if not success:
        print("Camera feed disconnected.")
        break

    # 4. Run AI Perception Inference
    results = model(camera_frame, classes=TARGET_CLASSES, verbose=False)
    
    # Check if any target objects were detected in the room/camera view
    object_detected = len(results[0].boxes) > 0

    # 5. Create the Simulation Canvas Background
    sim_frame = np.zeros((height, width, 3), dtype=np.uint8)
    sim_frame[:] = (46, 204, 113) # Green grass background

    # Draw the Roadway
    cv2.rectangle(sim_frame, (0, road_y - 100), (width, road_y + 100), (50, 50, 50), -1)
    for x in range(0, width, 40):
        cv2.line(sim_frame, (x, road_y), (x + 20, road_y), (255, 255, 255), 2)

    # 6. Hybrid Navigation & Safety Logic
    distance = obstacle_x - car_x

    if object_detected:
        # AI spotted an obstacle -> Trigger Emergency Brake!
        car_speed = 0
        status_text = "AI WARNING: OBSTACLE DETECTED -> BRAKING!"
        status_color = (0, 0, 255) # Bright Red Alert
        
        # Spawn the obstacle visually in the simulation because AI sees it
        cv2.rectangle(sim_frame, (obstacle_x, road_y - 35), (obstacle_x + 30, road_y + 35), (0, 0, 255), -1)
        cv2.line(sim_frame, (car_x + 80, road_y), (obstacle_x, road_y), (0, 0, 255), 3)
    else:
        # Clear path -> Drive forward
        if car_speed == 0: 
            car_speed = 4 # Resume cruise speed if obstacle disappears
        car_x += car_speed
        if car_x > width - 150: # Reset position loop if it drives off screen
            car_x = 50
        status_text = "CRUISE CONTROL ACTIVE - PATH CLEAR"
        status_color = (255, 255, 255) # White Operational State

    # 7. Draw the Autonomous Vehicle (Blue Box)
    cv2.rectangle(sim_frame, (car_x, road_y - 20), (car_x + 80, road_y + 20), (255, 150, 0), -1)

    # 8. Overlay Live HUD Telemetry
    cv2.putText(sim_frame, f"STATUS: {status_text}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, status_color, 2)
    cv2.putText(sim_frame, f"AI CAMERA ACTIVE: {object_detected}", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # 9. Resize and Show the Webcam view in a small corner window frame
    small_cam = cv2.resize(camera_frame, (200, 150))
    # Render the AI bounding boxes onto the small camera view window
    annotated_small_cam = results[0].plot()
    annotated_small_cam = cv2.resize(annotated_small_cam, (200, 150))
    
    # Inject the camera display into top right corner of simulation window
    sim_frame[0:150, width-200:width] = annotated_small_cam

    # Render complete display
    cv2.imshow("Neural Navigator - Full Pipeline MVP", sim_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
sys.exit()