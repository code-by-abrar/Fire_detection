# src/detect.py

from ultralytics import YOLO
import cv2

# Load the trained YOLOv8 model
model = YOLO("best.pt")

# Source (change to image path or video path)
source = "test_video.mp4"   

# Run detection
results = model.predict(source=source, show=True, conf=0.5, save=True)

print("✅ Detection completed! Results are saved.")
