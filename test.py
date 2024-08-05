from ultralytics import YOLO
import cv2

model = YOLO("yolov10n-memory.yaml",task="memory")
model.train(data="../datasets/rune/rune.yaml", epochs=300, imgsz=416)
model.export(format="onnx")
