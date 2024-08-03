from ultralytics import YOLO
import cv2

model = YOLO("yolov10-ghost-pose.yaml",task="pose")
model.train(data="../datasets/rune/rune.yaml", epochs=300, imgsz=416)
model.export(format="onnx")
