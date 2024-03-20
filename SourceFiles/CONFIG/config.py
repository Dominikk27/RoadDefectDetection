import sys
import os
import json



class Config():
    def __init__(self):
        self.config_file = 'config.json'
        self.parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        self.default_results_path = os.path.join(self.parent_directory, 'Results')
        self.default_width = 1000
        self.default_height = 700
        self.custom_results_path = None
    

    def create_defaultConfig(self):
        self.default_config = {
            "Results_Directory": self.default_results_path,
            "width": self.default_width,
            "height": self.default_height
        }
        try:
            with open(self.config_file, "w") as config_json:
                json.dump(self.default_config, config_json, indent = 4)
                #print("config sa vytvoril")
        except Exception as e:
            print(f"Chyba pri vytváraní konfiguračného súboru: {e}")
        self.load_config()



    def check_config(self):
        if os.path.exists(self.config_file):
            #print("config už existuje")
            self.load_config()
        else: 
            self.create_defaultConfig()

    def load_config(self):
            #print("load config")
            try:
                if self.config_file is not None:
                    with open(self.config_file, "r") as config_json:
                        config_data = json.load(config_json)
                        self.folder_path = config_data.get("Results_Directory", "")
                        self.videoFrame_width = config_data.get("width")
                        self.videoFrame_height = config_data.get("height")
                    #print(f"Folder path: {self.folder_path}")
            except Exception as e:
                print(f"Error: {e}")


    def save_config(self, custom_results_path):
        self.custom_results_path = custom_results_path
        try:
            data = {
                "Results_Directory": self.custom_results_path
            }
            with open(self.config_file, "w") as config_json:
                json.dump(data, config_json, indent=4)
        except Exception as e:
            print(f"Error: {e}")
    
    def restore_default(self):
        try: 
            with open(self.config_file, "w") as config_json:
                json.dump(self.default_config, config_json, indent = 4)
                #print("Default config sa obnovil")
        except Exception as error:
            print( f"Config Error: {error}")



     


