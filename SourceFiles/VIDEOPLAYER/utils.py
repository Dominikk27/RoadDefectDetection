from ultralytics import YOLO

import cv2
import os
from datetime import datetime

import imageio
import threading

from .tracking import Tracker

class Utils():
    def __init__(self, result_directory):
        #init YOLO model
        #v3_rem - bad
        #Version3 - best
        #Version2 - good
        #888 - mby
        #nvm pretty good getragee@gmail.com drive
        self.model = YOLO('./VIDEOPLAYER/pretrained_models/Version3.pt')
        self.result_dir = result_directory
        self.tracker = Tracker()
        


    def Detection(self, frame):     
        results = self.model(frame)
        return results
    

    def detection_visuals(self, frame, results):
        detection_results = results[0]
        bounding_boxes = []
        for detection in detection_results.boxes.data.cpu().numpy():
            x1, y1, x2, y2 = detection[:4].astype(int)
            bounding_boxes.append([x1, y1, x2, y2])
            class_id = int(detection[5])
            #print(results)
            class_name = detection_results.names[class_id]
            #print(detection)
            conf = detection[4]
            conf_percentage = int(conf * 100)
            
        bbox_idx = self.tracker.update(bounding_boxes)
        for bbox in bbox_idx:
            x1, y1, x2, y2, objID = bbox

            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(frame, (cx, cy), 4, (255, 255, 0), -1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), self.setColor(class_name), 2)
            cv2.putText(frame, f"{class_name}: [{conf_percentage}%]", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            detectedObject = frame[y1:y2, x1:x2]
            self.cropImage(detectedObject, class_name)
    

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



    def cropImage(self, detectedObject, className):
        
        if detectedObject.size > 0:
            now = datetime.now()
            current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
            imageFile =  f"{className}_{current_time}.jpg"
            #print(f" toto je filename {imageFile}")
           
        
            croppedImage_dir = os.path.join(self.result_dir, "Images")
            saveCropImage = os.path.join(croppedImage_dir, imageFile)
            croppedImage_dir = croppedImage_dir.replace("\\", "/")


            try:
                if os.path.isdir(croppedImage_dir):
                    #print("Exist!")
                    cv2.imwrite(saveCropImage, detectedObject)
                else:
                    print(f"Priečinok s cestou:  '{croppedImage_dir}' neexistuje!.")
                    os.makedirs(croppedImage_dir, exist_ok = True)
                    saveCropImage = os.path.join(croppedImage_dir, imageFile)
                    #print(f"Directory cropped: {croppedImage_dir}")
                    cv2.imwrite(saveCropImage, detectedObject)
                    #print("Detected and cropped object saved successfully")
                        
            except Exception as e:
                print(f"Chyba: {str(e)}")
        else:
            print("Empty Detection!")



        