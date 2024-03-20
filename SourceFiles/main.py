#################################
## IMPORT LIBS
#################################
import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from qt_material import *
from PySide6.QtCore import QPropertyAnimation
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QVBoxLayout

import json
import threading

#################################
## IMPORT GUI
#################################
from UI import *


#################################
## IMPORT STUFF
#################################
from CONFIG import *
from KML import *
from VIDEOPLAYER import *


#################################
## MAINWINDOW CLASS
#################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        


        self.folder_path = None
        self.cfg = Config()
        self.cfg.check_config()
        self.check_folders = Folders()

        self.folder_path = self.cfg.folder_path
        self.videoFrame_width = self.cfg.videoFrame_width
        self.videoFrame_height = self.cfg.videoFrame_height


        #################################
        ## REMOVE FRAME
        #################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #################################
        ## SET ICON AND TITLE
        #################################
        self.setWindowIcon(QtGui.QIcon(":/icons/assets/road.png"))
        self.setWindowTitle("Road Analyse")

        #################################
        ## SHADOW EFFECT
        #################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 42, 77, 250))
        #self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #################################
        ## SIZE GRIP
        #################################
        QSizeGrip(self.ui.size_grip)


        #################################
        ## CLOSE APP
        #################################
        self.ui.close_button.clicked.connect(
            lambda: self.close()
            )

        #################################
        ## MINIMIZE WINDOW
        #################################
        self.ui.minimize_button.clicked.connect(
            lambda: self.showMinimized()
            )

        #################################
        ## MAXIMIZE WINDOW
        #################################
        self.ui.maximize_button.clicked.connect(
            lambda: self.restore_or_maximize()
            )
        



        #################################
        ## SIDE MENU
        #################################
        self.ui.MenuButton.clicked.connect(lambda:
                                           self.slide_menu())          #TOGGLE SLIDE MENU

        self.ui.Analyse_Button.clicked.connect(lambda:
                                               self.ui.stackedWidget.setCurrentWidget(
                                                   self.ui.Analyse_Widget))
        self.ui.Archive_Button.clicked.connect(lambda:
                                               self.ui.stackedWidget.setCurrentWidget(
                                                   self.ui.Archive_Widget))
        self.ui.Settings_Button.clicked.connect(lambda:
                                               self.ui.stackedWidget.setCurrentWidget(
                                                   self.ui.Settings_Widget))
        self.ui.Info_Button.clicked.connect(lambda:
                                               self.ui.stackedWidget.setCurrentWidget(
                                                   self.ui.Information_Widget))
        

        self.ui.Header_Frame.mouseMoveEvent = self.move_window
        self.ui.Footer_Frame.mouseMoveEvent = self.move_window




        #################################
        ## ARCHIVE
        #################################

        #CARDS
        self.Card_Frame = QtWidgets.QFrame()
        cards_layout = QVBoxLayout()
        cards_layout.setAlignment(Qt.AlignCenter)
        self.Card_Frame.setLayout(cards_layout)

        self.check_folders.created_folders(self.folder_path, cards_layout)

        self.ui.Cards_Frame.layout().addWidget(self.Card_Frame)
        #REFRESH BUTTON
        self.ui.refresh_button.clicked.connect(lambda: self.check_folders.created_folders(self.folder_path, cards_layout))


        #################################
        ## ANALYSE
        #################################
        self.video_file = ""
        self.kml_file = ""
        self.ui.BrowseVideo_Button.clicked.connect(lambda: self.select_source("video"))
        self.ui.BrowseKML_Button.clicked.connect(lambda: self.select_source("KML"))
        self.ui.StartAnalyse_Button.clicked.connect(lambda: self.start_analyse())


        #################################
        ## Settings
        #################################
        self.resultsDir = ""
        self.ui.setResultsDir.clicked.connect(lambda: self.config_select_path())
        self.ui.save_settingsButton.clicked.connect(lambda: self.cfg.save_config(self.resultsDir))
        self.ui.restore_defaultSettings.clicked.connect(lambda: self.cfg.restore_default())
        self.ui.results_dir_input.setText(self.cfg.folder_path)


        #################################
        ## Info
        #################################
        self.ui.github_Button.clicked.connect(lambda: self.open_link("github"))
        self.ui.Github_Button.clicked.connect(lambda: self.open_link("github"))
        self.ui.colab_Button.clicked.connect(lambda: self.open_link("colab"))
        self.ui.docs_Button.clicked.connect(lambda: self.open_link("docs"))


        self.show()


    def config_select_path(self):
        self.resultsDir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder for save results")
        self.ui.results_dir_input.setText(self.resultsDir)
       
           

    def select_source(self, type):
        if type == "video":
            self.video_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "", "*.mp4;;*.avi")
            self.ui.VideoPath.setText(self.video_path)
        elif type == "KML":
            self.kml_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select KML File", "", "*.kml")
            self.ui.KMLPath.setText(self.kml_path)
    
    def start_analyse(self):
        #check folder
        project_name = self.ui.ProjectName.text()
        if not project_name:
            print("project name is empty")
        else:
            folder_exist = self.check_folders.resultFolder_path_exist(self.cfg.folder_path, project_name)
        
        #print(f"result folder: je {folder_exist}")

        KML_exist = self.check_kml()


    def play_video(self):
        project_name = self.ui.ProjectName.text()
        video_file = self.ui.VideoPath.text()
        kml_file = self.ui.KMLPath.text()
        #print(f"Nazov projektu {project_name}")
        #print(video_file)
        #print(f"toto je kml: {kml_file}")
        if video_file == "":
            return
        else:
            if kml_file == "":
                video_player = VideoPlayer(project_name, video_file, self.videoFrame_width, self.videoFrame_height)
                video_player.setup_window()
                video_player.play_video()
            else:
                self.distance = calculate_flight_distance(kml_file)
                print("Celková preletená vzdialenosť: {:.2f} km".format(self.distance))
                video_player = VideoPlayer(video_file, self.videoFrame_width, self.videoFrame_height)
                video_player.setup_window()
                video_player.play_video()
        




    
    #################################
    ## VYPISANIE HIERARCHIE
    #################################
        # Vypisanie Hierarchie (Debug)
        #self.print_object_hierarchy(self.ui.centralwidget)

    def print_object_hierarchy(self, obj, indent=0):
        print(' ' * indent + obj.objectName())
        for child in obj.children():
            if child is not None:
                self.print_object_hierarchy(child, indent + 4)



    def open_link(self, link_type):
        if link_type == "github":
            QDesktopServices.openUrl("https://github.com/Dominikk27")
        elif link_type == "colab":
            QDesktopServices.openUrl("https://colab.research.google.com/drive/1SX7YN-mBcEuoC__TfYaM6bC-gBM6tUv5")
        elif link_type == "docs":
            QDesktopServices.openUrl("https://github.com/Dominikk27")
        else:
            print("ERROR")

    
    #################################
    ## FUNCTION TO MAXIMIZE/NORMALIZE
    #################################
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.maximize_button.setIcon(QtGui.QIcon(u":/icons/assets/maximize.png"))
        else:
            self.showMaximized()
            self.ui.maximize_button.setIcon(QtGui.QIcon(u":/icons/assets/normalize.png"))
    
    #################################
    ## FUNCTION DETECT MOUSE PRESS
    #################################
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    #################################
    ## FUNCTION TO MOVE WINDOW
    #################################
    def move_window(self, e):
        if self.isMaximized() == False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()


    #########################################
    ## FUNCTION TO Create Results Folder
    #########################################
    def results_folder(self):
        print("y")
        #results_dir_input



    ############################################################
    ## FUNCTION TO Calculate Flight distance generate map
    ############################################################
    def check_kml(self):
        print("x")
        #results_dir_input

    #################################
    ## SLIDE LEFT MENU
    #################################
    def slide_menu(self):
        current_width = self.ui.SideMenu_Frame.width()

        if current_width == 50:
            new_width = 200
        else:
            new_width = 50
        
        self.animation = QPropertyAnimation(self.ui.SideMenu_Frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(current_width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    

#################################
## EXECUTE APP
#################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())