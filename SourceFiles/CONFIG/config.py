import os
import json



class Config():
    def __init__(self):
        self.config_file = 'config.json'
        self.parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        self.default_results_path = os.path.join(self.parent_directory, 'Results')
        self.custom_results_path = None


        self.folder_path = None
        self.Video_width = None
        self.Video_height = None
    

    def create_defaultConfig(self):
        self.default_config = {
            "Results_Directory": self.default_results_path,
        }
        try:
            with open(self.config_file, "w") as config_json:
                json.dump(self.default_config, config_json, indent = 4)
                #print("config sa vytvoril")
        except Exception as e:
            print(f"Chyba pri vytváraní konfiguračného súboru: {e}")
        self.load_config()



    def check_config(self):
        print("checking config")
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
                    #print(f"Folder path: {self.folder_path}")
            except Exception as e:
                print(f"Error: {e}")


    def save_config(self, custom_results_path):
        if custom_results_path == '':
            self.custom_results_path = self.default_results_path
        else: 
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
        self.default_config = {
            "Results_Directory": self.default_results_path,
        }
        try: 
            with open(self.config_file, "w") as config_json:
                json.dump(self.default_config, config_json, indent = 4)
                #print("Default config sa obnovil")
        except Exception as error:
            print( f"Config Error: {error}")



     


