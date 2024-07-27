from ultralytics import YOLO
import cv2
<<<<<<< Updated upstream
model = YOLO("yolov10n-pghost-pose.yaml",task="pose").load("yolov10n-ghost-200epochs.pt")
model.train(data="../datasets/rune/rune.yaml", epochs=100, imgsz=640)
=======
model = YOLO("yolov10n-doubleconv-pose.yaml",task="pose").load("best.pt")
model.train(data="../datasets/rune/rune.yaml", epochs=300, imgsz=416)
model.export(format="onnx")
>>>>>>> Stashed changes
