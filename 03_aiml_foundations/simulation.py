import cv2
import numpy as np

# Canvas Setup (mimicking our road grid)
width, height = 800, 600
road_y = 300

# Simulation States
car_x = 50
car_speed = 5
safe_braking_dist = 200
obstacle_x = 650

print("Neural Navigator - OpenCV Simulation Engine Initialized.")
print("Press 'q' inside the simulation window to exit.")

while True:
    # 1. Create a blank green field background
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:] = (46, 204, 113) # Green background (BGR format)

    # 2. Draw the Dark Gray Asphalt Roadway
    cv2.rectangle(frame, (0, road_y - 100), (width, road_y + 100), (50, 50, 50), -1)
    # White dotted lane lines
    for x in range(0, width, 40):
        cv2.line(frame, (x, road_y), (x + 20, road_y), (255, 255, 255), 2)

    # 3. Calculate dynamic distance vectors
    distance = obstacle_x - car_x

    # 4. Core Navigation Logic (The Decision Layer)
    if distance <= safe_braking_dist:
        car_speed = 0
        status_text = "EMERGENCY BRAKE ENGAGED - OBJECT DETECTED"
        status_color = (0, 0, 255) # Red warning
    else:
        car_x += car_speed
        status_text = "CRUISE CONTROL ACTIVE"
        status_color = (255, 255, 255) # White operational state

    # 5. Draw the Autonomous Vehicle (Blue Box)
    cv2.rectangle(frame, (car_x, road_y - 20), (car_x + 80, road_y + 20), (255, 150, 0), -1)
    
    # 6. Draw the Static Hazard / Pedestrian (Red Box)
    cv2.rectangle(frame, (obstacle_x, road_y - 35), (obstacle_x + 30, road_y + 35), (0, 0, 255), -1)

    # 7. Dynamic Sensor Proximity Visualizer
    if car_speed > 0:
        cv2.line(frame, (car_x + 80, road_y), (obstacle_x, road_y), (0, 255, 255), 1) # Yellow line
    else:
        cv2.line(frame, (car_x + 80, road_y), (obstacle_x, road_y), (0, 0, 255), 3) # Heavy red alert line

    # 8. Render Real-time HUD Telemetry Overlays
    cv2.putText(frame, f"SYSTEM STATUS: {status_text}", (30, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
    cv2.putText(frame, f"DISTANCE TO HAZARD: {max(0, distance)} px", (30, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show Frame
    cv2.imshow("Neural Navigator - Robust Navigation Simulator", frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
