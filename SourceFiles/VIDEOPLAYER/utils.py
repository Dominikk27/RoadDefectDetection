from ultralytics import YOLO
import numpy
import cv2
import cvzone
import math

class Utils():
    def __init__(self):
        #init YOLO model
        self.model = YOLO('./VIDEOPLAYER/pretrained_models/smallTest.pt')

    def Detection(self, frame):     
        results = self.model(frame)
        return results
    

    def detection_visuals(self, frame, results):
        detection_results = results[0]
        for detection in detection_results.boxes.data.cpu().numpy():
            x1, y1, x2, y2 = detection[:4].astype(int)
            class_id = int(detection[5])
            #print(results)
            class_name = detection_results.names[class_id]
            #print(detection)
            conf = detection[4]
            conf_percentage = int(conf * 100)
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), self.setColor(class_name), 2)
            cv2.putText(frame, f"{class_name}: [{conf_percentage}%]", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


    def setColor(self, class_name):
        if class_name == "D00":
            color = (0, 0, 255)
        elif class_name == "D10":
            color = (255, 0, 0)
        elif class_name == "D20":
            color = (255, 255, 255)
        elif class_name == "D40":
            color = (0, 255, 0)
        else:
            color = (255, 255, 0)
        return color