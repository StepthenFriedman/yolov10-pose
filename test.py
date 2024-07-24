from ultralytics import YOLO
import cv2
model = YOLO("yolov10n-pghost-pose.yaml",task="pose").load("yolov10n-ghost-100epochs.pt")
model.train(data="../datasets/rune/rune.yaml", epochs=100, imgsz=640)
