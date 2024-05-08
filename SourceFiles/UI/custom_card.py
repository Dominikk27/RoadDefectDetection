import sys
import json
import os
import shutil
import subprocess
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



from .icons import icons_rc


class CustomCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.card_frame = None
        self.card_list = []
        self.card_frames = []
        self.project_name = None
        self.flight_distance = None
        self.flight_location = None

        
        self.initUI()



    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)

        # Card Background
        self.setStyleSheet("background-color: #8BE9FD;")

        # Card Frame
        self.card_frame = QFrame()
        self.card_frame.setStyleSheet("background-color: #8BE9FD;")
        card_layout = QHBoxLayout()
        self.card_frame.setMaximumHeight(300)
        self.card_frame.setMaximumWidth(700)
        self.card_frame.setMinimumHeight(300)
        self.card_frame.setMinimumWidth(670)
        card_layout.setAlignment(Qt.AlignCenter)

        self.card_frames.append(self.card_frame)

        # Image Frame
        image_frame = QFrame()
        image_layout = QHBoxLayout()
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("map.png")) 
        self.image_label.setAlignment(Qt.AlignCenter) 
        image_layout.setAlignment(Qt.AlignCenter)
        self.image_label.setMaximumSize(250, 250)
        self.image_label.setScaledContents(True)
        image_layout.addWidget(self.image_label)
        image_frame.setLayout(image_layout)

        # Content Frame
        content_frame = QFrame()
        content_layout = QVBoxLayout()

        # Content
        self.project_name_label = QLabel("Project Name")
        self.project_name_label.setStyleSheet("font: bold 22px Arial Black;")
        self.project_date_label = QLabel("Date: ")
        self.project_length_label = QLabel("Length: ")
        self.project_location_label = QLabel("Location: ")

        content_layout.addWidget(self.project_name_label)
        content_layout.addWidget(self.project_date_label)
        content_layout.addWidget(self.project_length_label)
        content_layout.addWidget(self.project_location_label)

        # Buttons
        buttons_frame = QFrame()
        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignLeft)
        buttons_frame.setStyleSheet("border: none;")

        open_folder_button = QPushButton("Open Folder")
        open_folder_button.setIcon(QIcon(":/icons/icons/folder.png"))
        open_folder_button.setStyleSheet("background-color: #ffffff; padding: 10px;") 
        self.folder_path = None
        open_folder_button.clicked.connect(lambda: self.open_folder())

        open_analyse_button = QPushButton("Open Analyse")
        open_analyse_button.setIcon(QIcon(":/icons/icons/file.png"))
        open_analyse_button.setStyleSheet("background-color: #ffffff; padding: 10px;")  
        self.analyse_path = None
        open_analyse_button.clicked.connect(lambda: self.open_analyse())

        delete_project_button = QPushButton("Delete Project")
        delete_project_button.setIcon(QIcon(":/icons/icons/trash.png"))
        delete_project_button.setStyleSheet("background-color: #ffffff; padding: 10px;")  
        delete_project_button.clicked.connect(lambda: self.delete_project())


        
        buttons_layout.addWidget(open_folder_button)
        buttons_layout.addWidget(open_analyse_button)
        buttons_layout.addWidget(delete_project_button)


        buttons_frame.setLayout(buttons_layout)
        content_layout.addWidget(buttons_frame)

        content_frame.setLayout(content_layout)
        card_layout.addWidget(image_frame)
        card_layout.addWidget(content_frame)
        self.card_frame.setLayout(card_layout)
        self.layout.addWidget(self.card_frame)


        self.setLayout(self.layout)
    
    #################################
    ## Open Folder
    #################################
    def open_folder(self):
        #QFileDialog.getExistingDirectory(self, "", self.folder_path)
        print(self.folder_path)
        subprocess.Popen(f'explorer "{self.folder_path}"')


    #################################
    ## Open Analyse video
    #################################
    def open_analyse(self):
        analysed_file = os.path.join(self.analyse_path, f"{self.project_name}.mp4")
        try:
            # Spustite externý program pre otvorenie .docx súboru
            subprocess.Popen(["start", "", analysed_file], shell=True)
        except Exception as e:
            print(f"Chyba pri otváraní súboru: {str(e)}")
    
    #################################
    ## Delete Folder
    #################################
    def delete_project(self):
        try:
            shutil.rmtree(self.folder_path)
            # Odstránenie karty z rozloženia
            self.layout.removeWidget(self.card_frame)
            # Uvoľnenie zdrojov karty
            self.card_frame.deleteLater()
            print(f"Adresár '{self.folder_path}' bol odstránený ")
        except Exception as e:
            print(f"Chyba pri odstráneni adresáru '{self.folder_path}': {str(e)}")
    

    def remove_all_cards(self):
        for card_frame in self.card_frames:
            parent_widget = card_frame.parentWidget()
            if parent_widget is not None:
                layout = parent_widget.layout()
                if layout is not None:
                    layout.removeWidget(card_frame)
                card_frame.deleteLater()
        self.card_frames = []

    
    #################################
    ## Project Info
    #################################
    def set_project_info(self, image_path, project_name, project_date, project_folder):
            self.project_name = project_name
            self.card_list.append(self.project_name)
            # Project INFO setup
            project_image = QPixmap(image_path)
            if not project_image.isNull():
                self.image_label.setPixmap(project_image)
            else:
                print(f"Could not load image from: {image_path}")

            self.project_name_label.setText(project_name)

            date_label = f"Date: {project_date}"
            self.project_date_label.setText(date_label)
            #print(project_folder)

            flight_data_path = os.path.join(project_folder, "flight_info.json")
            try:
                with open(flight_data_path, 'r') as file:
                    flight_data = json.load(file)
                    self.flight_distance = "{:.2f}".format(flight_data.get("flight_distance"))
                    self.flight_location = flight_data.get("location")
            except Exception as e:
                self.flight_distance = "N/A"
                self.flight_distance = "N/A"
                print(f"Flight data file not found at: {flight_data_path}")
            
            # Set project length and location labels
            self.project_length_label.setText(f"Flight distance: {str(self.flight_distance)} km")
            self.project_location_label.setText(f"Location: {self.flight_location}")
            self.folder_path = project_folder
            self.analyse_path = os.path.join(self.folder_path, "Video")
           

# CARD UI init
def main():
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.setWindowTitle("Custom Card Widget")
    mainWindow.setGeometry(100, 100, 600, 280)

    centralWidget = QWidget()
    custom_card = CustomCard()
    central_layout = QVBoxLayout()
    central_layout.addWidget(custom_card)
    centralWidget.setLayout(central_layout)

    mainWindow.setCentralWidget(centralWidget)
    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
