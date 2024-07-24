from ultralytics import YOLO
import cv2
model = YOLO("yolov10n-pose-rune.yaml",task="pose")
model.train(data="../datasets/rune/rune.yaml", epochs=100, imgsz=640)
