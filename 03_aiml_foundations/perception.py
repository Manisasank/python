import cv2
from ultralytics import YOLO

# 1. Load the pre-trained YOLOv8 model (nano version for speed)
model = YOLO("yolov8n.pt")

# 2. Target classes we care about based on COCO dataset indices:
# Class 0 is 'person', Class 2 is 'car', Class 7 is 'truck'
TARGET_CLASSES = [0, 2, 7]

# 3. Initialize video capture
# Use 0 for your live webcam, or replace with a path to a dashcam video file (e.g., "dashcam.mp4")
cap = cv2.VideoCapture(0)

print("Neural Navigator Perception System Initialized. Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame or video ended.")
        break

    # 4. Run inference on the frame, filtering by our target classes
    results = model(frame, classes=TARGET_CLASSES, verbose=False)

    # 5. Visualize the results on the frame
    # .plot() automatically draws bounding boxes and labels
    annotated_frame = results[0].plot()

    # 6. Display the live feed
    cv2.imshow("Neural Navigator - Advanced Perception MVP", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up windows and release the camera
cap.release()
cv2.destroyAllWindows()
