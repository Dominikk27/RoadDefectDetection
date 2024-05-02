import os
import math
import random
import datetime
import subprocess

import shutil

from .custom_card import CustomCard
from .custom_card import *


class Folders():
    def __init__(self):
        self.folder_list = []
        self.i = 1

    def check_folders(self, cesta_k_priecinku, cards_layout):
        self.folder_list = []
        try:
            if os.path.exists(cesta_k_priecinku) and os.path.isdir(cesta_k_priecinku):
                
                results = os.listdir(cesta_k_priecinku)

                for file in results:
                    if file not in self.folder_list:
                        custom_card = CustomCard()
                        file_path = os.path.join(cesta_k_priecinku, file)
                        norm_path = os.path.normpath(file_path)
                        image_path = os.path.join(file_path, "map.png")
                        if not os.path.isfile(image_path):
                            image_path = "UI/icons/assets/map_not_found.png"
                        project_date = os.path.getctime(file_path)
                        project_date = datetime.datetime.fromtimestamp(project_date).strftime('%d.%m.%Y %H:%M:%S')
                        custom_card.set_project_info(image_path, file, project_date, norm_path)  
                        custom_card.setMinimumHeight(0)  
                        cards_layout.addWidget(custom_card)  
                        self.folder_list.append(file)
                    #else:
                        #print("Karta pre súbor je už vytvorená")
            else:
                print(f"Priečinok s cestou:  '{cesta_k_priecinku}' neexistuje!.")
                
        except Exception as e:
            print(f"Chyba: {str(e)}")



    def resultFolder_path_check(self, folder_path, project_name):
        project_result_directory = os.path.join(folder_path, project_name)
        try:

            if (not os.path.isdir(project_result_directory)):
                os.mkdir(project_result_directory)
                self.create_results_directories(project_result_directory) 
            else:
                print(f"Subor: {project_result_directory} already exists!")
                while True:
                    project_result_directory = f"{project_result_directory}__version_({self.i})"
                    if (not os.path.isdir(project_result_directory)):
                        os.mkdir(project_result_directory)
                        self.create_results_directories(project_result_directory) 
                        self.i = self.i + 1
                        break
        except Exception as e:
            print(f"Problem pri vytvárani priečinku pre výsledky{e}")
        os.chmod(project_result_directory, 0o777)
        return project_result_directory
        


    def create_results_directories(self, project_result_directories):
        IMG_dir = os.path.join(project_result_directories, "Images")
        VIDEO_dir = os.path.join(project_result_directories, "Video")
        try:
            os.mkdir(IMG_dir) 
            os.mkdir(VIDEO_dir)
        except Exception as e:
            print(f"Problem pri vytváraní podpriečinkov{e}")
            
    

