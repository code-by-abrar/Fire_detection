#Run this code in Google Colab
from google.colab import drive
drive.mount('/content/drive')

!pip install roboflow
!pip install ultralytics


from roboflow import Roboflow
rf = Roboflow(api_key="put your api key here")

project = rf.workspace("").project("")
dataset = project.version().download("yolov8")

from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data=dataset.location + "/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    lr0=0.01,
    optimizer="AdamW",
    patience=20,
    augment=True,
    degrees=10,
    translate=0.1,
    scale=0.5,
    flipud=0.0,
    fliplr=0.5,
    mosaic=1.0,
    mixup=0.2,
    project="/content/drive/MyDrive/Fire/model",
    name="fire_model"
)