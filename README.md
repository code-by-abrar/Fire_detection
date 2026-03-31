# 🔥 Fire & Smoke Detection System (Real-Time)

An AI-powered computer vision system designed to detect fire and smoke in real time from video streams, with a focus on enabling automated response systems.

This project goes beyond basic object detection by targeting early hazard detection and future integration with autonomous suppression systems (e.g., drones, smart sprinklers).

##  Overview
Fire incidents often escalate due to delayed human response.  
This system aims to reduce that delay by:

- Continuously monitoring video feeds  
- Detecting fire & smoke instantly  
- Providing confidence-based predictions  
- Enabling integration with automated response mechanisms  
 Goal: Shift from passive monitoring → active, real-time response

## 🧠 Features
- 🔍 Real-time fire and smoke detection  
- 🎯 Bounding box predictions with confidence scores  
- 📹 Works on images, videos, and live streams  
- ⚡ Optimized for fast inference  
- 🔗 Designed for integration with IoT / automation systems  

##  System Architecture
1. Input: Live video stream / recorded footage  
2. Preprocessing: Frame extraction & resizing  
3. Model Inference: Fire & smoke detection  
4. Output:
   - Bounding boxes  
   - Confidence scores  
5. Future Integration:
   - Trigger alerts / alarms  
   - Activate water suppression systems  

##  Tech Stack
- Python  
- OpenCV  
- YOLO (Object Detection Model)  
- NumPy / Pandas  
- PyTorch / Ultralytics  

##  Model Details

- Model: YOLOv8  
- Classes: Fire, Smoke  

## 📦 Installation
git clone 
pip install -r requirements.txt  

## ▶️ Usage
Run on Image:  
python detect.py --source image.jpg  

Run on Video:  
python detect.py --source video.mp4  

Run on Webcam:  
python detect.py --source 0  


##  Future Work
-  Integration with autonomous drones for fire suppression  
-  Automatic sprinkler system activation  
-  Cloud-based monitoring dashboard  
-  IoT-based real-time alert system  
-  Model optimization for edge devices  

## Limitations
- Performance may vary in low-light or fog conditions  
- Requires further validation for real-world deployment  
- False positives possible in fire-like environments  
This is a research/development system, not production-ready yet.

##  Contributing
Contributions, ideas, and improvements are welcome.  
Feel free to open issues or submit pull requests.

##  Contact
If you're working on AI safety systems, computer vision, or smart infrastructure, feel free to connect.

##  Final Note
This project represents a step toward AI systems that don’t just detect problems — but enable immediate action.
Training was performed on Google Colab using Roboflow dataset integration.