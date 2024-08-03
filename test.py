from ultralytics import YOLO
import cv2

model = YOLO("yolov10n-doubleconv-pose.yaml",task="pose").load("best.pt")
model.train(data="../datasets/rune/rune.yaml", epochs=300, imgsz=416)
model.export(format="onnx")
