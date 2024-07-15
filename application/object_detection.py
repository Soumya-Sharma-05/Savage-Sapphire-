from ultralytics import YOLO
import cv2
import os

# Load the YOLOv5 model
model_path = 'models/best.pt'
model = YOLO(model_path)

def detect_objects(image_path):
    # Run object detection
    results = model(image_path)

    # Extract the result images from the results list
    result_image = results[0].plot()  # Plot the results to get the image with bounding boxes

    # Save the results image
    result_image_path = 'static/results/' + os.path.basename(image_path)
    cv2.imwrite(result_image_path, result_image)  # Save the result image to 'static/results'

    return result_image_path
