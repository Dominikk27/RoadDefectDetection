import cv2
import numpy as np
from ultralytics import YOLO
import os

import imageio

from .utils import Utils

class VideoPlayer():
    def __init__(self, source, result_directory, project_name, width, height):
        self.width = width
        self.height = height

        self.source = source
        self.project_name = project_name

        self.result_directory = result_directory
        
        #Init model
        self.model = Utils(result_directory)

    def setup_window(self):
        #print(f"VIDEO: {self.source}")
        #print(f"W: {self.width} x H: {self.height}")
        self.video = cv2.VideoCapture(self.source)
        if not self.video.isOpened():
            print("Error: Video not opened")
            return
        
        cv2.namedWindow('Road Analyse', cv2.WINDOW_NORMAL)
        self.resized_window = cv2.resizeWindow('Road Analyse', self.width, self.height)
    
    def play_video(self):
        if self.video is None:
            print("Chyba: Video nie je inicializované")
            return
        
        video_frames = []
        
        while True:
            ret, frame = self.video.read()
            if not ret:
                break

            results = self.model.Detection(frame)
            self.model.detection_visuals(frame, results)
            video_frames.append(frame)


            cv2.putText(frame, f"Project: {self.project_name}", (50,100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            cv2.imshow('Road Analyse', frame)

            #self.model.saveVideo(frame)



            key = cv2.waitKey(1)  # 1 ms
            if key == ord('q') or key == 27:
                break

        self.video.release()
        cv2.destroyAllWindows()

        saveVideoPath = os.path.join(self.result_directory, "Video")
        saveVidePath = os.path.join(saveVideoPath, f"{self.project_name}.mp4")
        saveVideFile = saveVidePath.replace("\\", "/")
        try:
            writer = imageio.get_writer(saveVideFile, format='FFMPEG')
            for frame in video_frames:
                writer.append_data(frame)
            writer.close()
        except Exception as e:
            print("chyba")