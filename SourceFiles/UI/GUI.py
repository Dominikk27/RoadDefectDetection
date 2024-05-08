# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_designtvMgBE.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PyQt5 import *


from .icons import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 639)
        MainWindow.setStyleSheet(u"border:none;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header_Frame = QFrame(self.centralwidget)
        self.Header_Frame.setObjectName(u"Header_Frame")
        self.Header_Frame.setStyleSheet(u"border:none;\n"
"background-color: rgb(56, 58, 89);")
        self.Header_Frame.setFrameShape(QFrame.NoFrame)
        self.Header_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header_Frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header_Left_Frame = QFrame(self.Header_Frame)
        self.Header_Left_Frame.setObjectName(u"Header_Left_Frame")
        self.Header_Left_Frame.setMinimumSize(QSize(0, 0))
        self.Header_Left_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.Header_Left_Frame.setFrameShape(QFrame.NoFrame)
        self.Header_Left_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Header_Left_Frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.MenuButton = QPushButton(self.Header_Left_Frame)
        self.MenuButton.setObjectName(u"MenuButton")
        self.MenuButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/assets/apps.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuButton.setIcon(icon)
        self.MenuButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.MenuButton, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.Header_Left_Frame)

        self.Header_Center_Frame = QFrame(self.Header_Frame)
        self.Header_Center_Frame.setObjectName(u"Header_Center_Frame")
        self.Header_Center_Frame.setFrameShape(QFrame.NoFrame)
        self.Header_Center_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Header_Center_Frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.Header_Center_Frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/assets/Road2.png"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.AppName = QLabel(self.Header_Center_Frame)
        self.AppName.setObjectName(u"AppName")
        self.AppName.setMaximumSize(QSize(16777215, 42))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(28)
        font.setBold(True)
        self.AppName.setFont(font)

        self.horizontalLayout_3.addWidget(self.AppName, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.Header_Center_Frame, 0, Qt.AlignRight)

        self.Header_Right_Frame = QFrame(self.Header_Frame)
        self.Header_Right_Frame.setObjectName(u"Header_Right_Frame")
        self.Header_Right_Frame.setFrameShape(QFrame.NoFrame)
        self.Header_Right_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header_Right_Frame)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.Header_Right_Frame)
        self.minimize_button.setObjectName(u"minimize_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self.Header_Right_Frame)
        self.maximize_button.setObjectName(u"maximize_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.maximize_button)

        self.close_button = QPushButton(self.Header_Right_Frame)
        self.close_button.setObjectName(u"close_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.Header_Right_Frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Header_Frame, 0, Qt.AlignTop)

        self.Main_Frame = QFrame(self.centralwidget)
        self.Main_Frame.setObjectName(u"Main_Frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Frame.sizePolicy().hasHeightForWidth())
        self.Main_Frame.setSizePolicy(sizePolicy)
        self.Main_Frame.setFrameShape(QFrame.NoFrame)
        self.Main_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Main_Frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.SideMenu_Frame = QFrame(self.Main_Frame)
        self.SideMenu_Frame.setObjectName(u"SideMenu_Frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SideMenu_Frame.sizePolicy().hasHeightForWidth())
        self.SideMenu_Frame.setSizePolicy(sizePolicy1)
        self.SideMenu_Frame.setMinimumSize(QSize(50, 0))
        self.SideMenu_Frame.setMaximumSize(QSize(40, 16777215))
        self.SideMenu_Frame.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.SideMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.SideMenu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.SideMenu_Frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Menu_Frame = QFrame(self.SideMenu_Frame)
        self.Menu_Frame.setObjectName(u"Menu_Frame")
        self.Menu_Frame.setMinimumSize(QSize(200, 0))
        self.Menu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menu_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Menu_Frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Analyse_Button = QPushButton(self.Menu_Frame)
        self.Analyse_Button.setObjectName(u"Analyse_Button")
        self.Analyse_Button.setMaximumSize(QSize(42, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Analyse_Button.setIcon(icon4)
        self.Analyse_Button.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.Analyse_Button, 0, 0, 1, 1, Qt.AlignLeft)

        self.Archive_Button = QPushButton(self.Menu_Frame)
        self.Archive_Button.setObjectName(u"Archive_Button")
        self.Archive_Button.setMaximumSize(QSize(42, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/archive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Archive_Button.setIcon(icon5)
        self.Archive_Button.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.Archive_Button, 1, 0, 1, 1, Qt.AlignLeft)

        #self.Info_Button = QPushButton(self.Menu_Frame)
        #self.Info_Button.setObjectName(u"Info_Button")
        #self.Info_Button.setMaximumSize(QSize(42, 16777215))
        #icon6 = QIcon()
        #icon6.addFile(u":/icons/assets/info.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.Info_Button.setIcon(icon6)
        #self.Info_Button.setIconSize(QSize(42, 42))

        #self.gridLayout.addWidget(self.Info_Button, 8, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.Settings_Button = QPushButton(self.Menu_Frame)
        self.Settings_Button.setObjectName(u"Settings_Button")
        self.Settings_Button.setMaximumSize(QSize(42, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settings_Button.setIcon(icon7)
        self.Settings_Button.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.Settings_Button, 7, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.Analyse_Label = QLabel(self.Menu_Frame)
        self.Analyse_Label.setObjectName(u"Analyse_Label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.Analyse_Label.setFont(font1)
        self.Analyse_Label.setMargin(10)

        self.gridLayout.addWidget(self.Analyse_Label, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.Archive_Label = QLabel(self.Menu_Frame)
        self.Archive_Label.setObjectName(u"Archive_Label")
        self.Archive_Label.setFont(font1)
        self.Archive_Label.setMargin(10)

        self.gridLayout.addWidget(self.Archive_Label, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.Settings_Label = QLabel(self.Menu_Frame)
        self.Settings_Label.setObjectName(u"Settings_Label")
        self.Settings_Label.setFont(font1)
        self.Settings_Label.setMargin(10)

        self.gridLayout.addWidget(self.Settings_Label, 7, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.Info_Label = QLabel(self.Menu_Frame)
        self.Info_Label.setObjectName(u"Info_Label")
        self.Info_Label.setFont(font1)
        self.Info_Label.setMargin(10)

        self.gridLayout.addWidget(self.Info_Label, 8, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.Menu_Frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.SideMenu_Frame)

        self.MainContent_Frame = QFrame(self.Main_Frame)
        self.MainContent_Frame.setObjectName(u"MainContent_Frame")
        self.MainContent_Frame.setMinimumSize(QSize(800, 0))
        self.MainContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.MainContent_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainContent_Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.MainContent_Frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Analyse_Widget = QWidget()
        self.Analyse_Widget.setObjectName(u"Analyse_Widget")
        self.Analyse_Widget.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(139, 233, 253);\n"
"	padding: 3px\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Analyse_Widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.AnalyseTitle_Frame = QFrame(self.Analyse_Widget)
        self.AnalyseTitle_Frame.setObjectName(u"AnalyseTitle_Frame")
        self.AnalyseTitle_Frame.setFrameShape(QFrame.StyledPanel)
        self.AnalyseTitle_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.AnalyseTitle_Frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.AnalyseTitle_Frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.AnalyseTitle_Frame, 0, Qt.AlignTop)

        self.AnalyseMain_Frame = QFrame(self.Analyse_Widget)
        self.AnalyseMain_Frame.setObjectName(u"AnalyseMain_Frame")
        sizePolicy.setHeightForWidth(self.AnalyseMain_Frame.sizePolicy().hasHeightForWidth())
        self.AnalyseMain_Frame.setSizePolicy(sizePolicy)
        self.AnalyseMain_Frame.setFrameShape(QFrame.StyledPanel)
        self.AnalyseMain_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.AnalyseMain_Frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.AnalyseContent_Frame = QFrame(self.AnalyseMain_Frame)
        self.AnalyseContent_Frame.setObjectName(u"AnalyseContent_Frame")
        self.AnalyseContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.AnalyseContent_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.AnalyseContent_Frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(0, 40, 0, 0)
        self.BrowseVideo_Button = QPushButton(self.AnalyseContent_Frame)
        self.BrowseVideo_Button.setObjectName(u"BrowseVideo_Button")
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BrowseVideo_Button.setIcon(icon8)

        self.gridLayout_2.addWidget(self.BrowseVideo_Button, 1, 2, 1, 1, Qt.AlignHCenter)

        self.BrowseKML_Button = QPushButton(self.AnalyseContent_Frame)
        self.BrowseKML_Button.setObjectName(u"BrowseKML_Button")
        self.BrowseKML_Button.setIcon(icon8)

        self.gridLayout_2.addWidget(self.BrowseKML_Button, 2, 2, 1, 1, Qt.AlignHCenter)

        self.ProjectName = QLineEdit(self.AnalyseContent_Frame)
        self.ProjectName.setObjectName(u"ProjectName")
        self.ProjectName.setMinimumSize(QSize(300, 20))
        self.ProjectName.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.ProjectName, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.VideoPath = QLineEdit(self.AnalyseContent_Frame)
        self.VideoPath.setObjectName(u"VideoPath")
        self.VideoPath.setMinimumSize(QSize(300, 20))

        self.gridLayout_2.addWidget(self.VideoPath, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.KMLPath = QLineEdit(self.AnalyseContent_Frame)
        self.KMLPath.setObjectName(u"KMLPath")
        self.KMLPath.setMinimumSize(QSize(300, 20))

        self.gridLayout_2.addWidget(self.KMLPath, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.StartAnalyse_Button = QPushButton(self.AnalyseContent_Frame)
        self.StartAnalyse_Button.setObjectName(u"StartAnalyse_Button")

        self.gridLayout_2.addWidget(self.StartAnalyse_Button, 3, 1, 1, 1, Qt.AlignVCenter)

        self.ProjectName_Label = QLabel(self.AnalyseContent_Frame)
        self.ProjectName_Label.setObjectName(u"ProjectName_Label")

        self.gridLayout_2.addWidget(self.ProjectName_Label, 0, 0, 1, 1)

        self.VideoPath_Label = QLabel(self.AnalyseContent_Frame)
        self.VideoPath_Label.setObjectName(u"VideoPath_Label")

        self.gridLayout_2.addWidget(self.VideoPath_Label, 1, 0, 1, 1)

        self.KML_Label = QLabel(self.AnalyseContent_Frame)
        self.KML_Label.setObjectName(u"KML_Label")

        self.gridLayout_2.addWidget(self.KML_Label, 2, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.AnalyseContent_Frame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.AnalyseMain_Frame)

        self.stackedWidget.addWidget(self.Analyse_Widget)
        self.Settings_Widget = QWidget()
        self.Settings_Widget.setObjectName(u"Settings_Widget")
        self.verticalLayout_8 = QVBoxLayout(self.Settings_Widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.SettingsTitle_Frame = QFrame(self.Settings_Widget)
        self.SettingsTitle_Frame.setObjectName(u"SettingsTitle_Frame")
        self.SettingsTitle_Frame.setFrameShape(QFrame.StyledPanel)
        self.SettingsTitle_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.SettingsTitle_Frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.SettingsTitle_Frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.SettingsTitle_Frame, 0, Qt.AlignTop)

        self.SettingsMain_Frame = QFrame(self.Settings_Widget)
        self.SettingsMain_Frame.setObjectName(u"SettingsMain_Frame")
        sizePolicy.setHeightForWidth(self.SettingsMain_Frame.sizePolicy().hasHeightForWidth())
        self.SettingsMain_Frame.setSizePolicy(sizePolicy)
        self.SettingsMain_Frame.setFrameShape(QFrame.StyledPanel)
        self.SettingsMain_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SettingsMain_Frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.settingsContent_frame = QFrame(self.SettingsMain_Frame)
        self.settingsContent_frame.setObjectName(u"settingsContent_frame")
        self.settingsContent_frame.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 5;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	height: 25;\n"
"}")
        self.settingsContent_frame.setFrameShape(QFrame.StyledPanel)
        self.settingsContent_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.settingsContent_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.settingsContent_frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.results_dir_input = QLineEdit(self.settingsContent_frame)
        self.results_dir_input.setObjectName(u"results_dir_input")
        self.results_dir_input.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.results_dir_input, 0, 1, 1, 1)

        self.setResultsDir = QPushButton(self.settingsContent_frame)
        self.setResultsDir.setObjectName(u"setResultsDir")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setResultsDir.setIcon(icon9)

        self.gridLayout_3.addWidget(self.setResultsDir, 0, 2, 1, 1)

        self.label_6 = QLabel(self.settingsContent_frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        #self.something_input = QLineEdit(self.settingsContent_frame)
        #self.something_input.setObjectName(u"something_input")
        #self.something_input.setMinimumSize(QSize(300, 0))

        #self.gridLayout_3.addWidget(self.something_input, 1, 1, 1, 1)

        #self.BrowseSomething = QPushButton(self.settingsContent_frame)
        #self.BrowseSomething.setObjectName(u"BrowseSomething")
        #self.BrowseSomething.setIcon(icon9)

        #self.gridLayout_3.addWidget(self.BrowseSomething, 1, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.settingsContent_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.buttons_frame = QFrame(self.SettingsMain_Frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 10;\n"
"}")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.restore_defaultSettings = QPushButton(self.buttons_frame)
        self.restore_defaultSettings.setObjectName(u"restore_defaultSettings")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_defaultSettings.setIcon(icon10)

        self.horizontalLayout_11.addWidget(self.restore_defaultSettings)

        self.save_settingsButton = QPushButton(self.buttons_frame)
        self.save_settingsButton.setObjectName(u"save_settingsButton")
        self.save_settingsButton.setIcon(icon7)

        self.horizontalLayout_11.addWidget(self.save_settingsButton)


        self.verticalLayout_10.addWidget(self.buttons_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.SettingsMain_Frame)

        self.stackedWidget.addWidget(self.Settings_Widget)
        self.Information_Widget = QWidget()
        self.Information_Widget.setObjectName(u"Information_Widget")
        self.verticalLayout_12 = QVBoxLayout(self.Information_Widget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.InformationTitle_Frame = QFrame(self.Information_Widget)
        self.InformationTitle_Frame.setObjectName(u"InformationTitle_Frame")
        self.InformationTitle_Frame.setFrameShape(QFrame.StyledPanel)
        self.InformationTitle_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.InformationTitle_Frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.InformationTitle_Frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.InformationTitle_Frame, 0, Qt.AlignTop)

        self.InformationsMain_Frame = QFrame(self.Information_Widget)
        self.InformationsMain_Frame.setObjectName(u"InformationsMain_Frame")
        sizePolicy.setHeightForWidth(self.InformationsMain_Frame.sizePolicy().hasHeightForWidth())
        self.InformationsMain_Frame.setSizePolicy(sizePolicy)
        self.InformationsMain_Frame.setFrameShape(QFrame.StyledPanel)
        self.InformationsMain_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.InformationsMain_Frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.InformationsMain_Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(26)
        font3.setBold(True)
        self.label_8.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignBottom)

        #self.Links_Frame = QFrame(self.frame)
        #self.Links_Frame.setObjectName(u"Links_Frame")
        #self.Links_Frame.setFrameShape(QFrame.StyledPanel)
        #self.Links_Frame.setFrameShadow(QFrame.Raised)
        #self.horizontalLayout_12 = QHBoxLayout(self.Links_Frame)
        #self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        #self.docs_Button = QPushButton(self.Links_Frame)
        #self.docs_Button.setObjectName(u"docs_Button")
        #icon11 = QIcon()
        #icon11.addFile(u":/icons/assets/docs.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.docs_Button.setIcon(icon11)
        #self.docs_Button.setIconSize(QSize(54, 54))

        #self.horizontalLayout_12.addWidget(self.docs_Button)

        #self.colab_Button = QPushButton(self.Links_Frame)
        #self.colab_Button.setObjectName(u"colab_Button")
        #icon12 = QIcon()
        #icon12.addFile(u":/icons/assets/colab.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.colab_Button.setIcon(icon12)
        #self.colab_Button.setIconSize(QSize(54, 54))

        #self.horizontalLayout_12.addWidget(self.colab_Button)

        #self.github_Button = QPushButton(self.Links_Frame)
        #self.github_Button.setObjectName(u"github_Button")
        #icon13 = QIcon()
        #icon13.addFile(u":/icons/assets/github.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.github_Button.setIcon(icon13)
        #self.github_Button.setIconSize(QSize(54, 54))

        #self.horizontalLayout_12.addWidget(self.github_Button)


        #self.verticalLayout_14.addWidget(self.Links_Frame)


        self.verticalLayout_7.addWidget(self.frame)

        #self.frame_2 = QFrame(self.InformationsMain_Frame)
        #self.frame_2.setObjectName(u"frame_2")
        #self.frame_2.setFrameShape(QFrame.StyledPanel)
        #self.frame_2.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_15 = QVBoxLayout(self.frame_2)
        #self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        #self.label_9 = QLabel(self.frame_2)
        #self.label_9.setObjectName(u"label_9")

        #self.verticalLayout_15.addWidget(self.label_9)


        #self.verticalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_12.addWidget(self.InformationsMain_Frame)

        self.stackedWidget.addWidget(self.Information_Widget)
        self.Archive_Widget = QWidget()
        self.Archive_Widget.setObjectName(u"Archive_Widget")
        self.verticalLayout_6 = QVBoxLayout(self.Archive_Widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ArchiveTitle_Frame = QFrame(self.Archive_Widget)
        self.ArchiveTitle_Frame.setObjectName(u"ArchiveTitle_Frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(150)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ArchiveTitle_Frame.sizePolicy().hasHeightForWidth())
        self.ArchiveTitle_Frame.setSizePolicy(sizePolicy2)
        self.ArchiveTitle_Frame.setFrameShape(QFrame.StyledPanel)
        self.ArchiveTitle_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.ArchiveTitle_Frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.ArchiveTitle_Frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(400, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setFont(font2)
        self.label_3.setScaledContents(False)

        self.horizontalLayout_10.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.refresh_button = QPushButton(self.ArchiveTitle_Frame)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy4)
        self.refresh_button.setMaximumSize(QSize(50, 50))
        self.refresh_button.setIcon(icon10)
        self.refresh_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.refresh_button, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.ArchiveTitle_Frame, 0, Qt.AlignRight|Qt.AlignTop)

        self.scrollArea = QScrollArea(self.Archive_Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 500))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.CardScroll = QWidget()
        self.CardScroll.setObjectName(u"CardScroll")
        self.CardScroll.setGeometry(QRect(0, 0, 794, 505))
        sizePolicy.setHeightForWidth(self.CardScroll.sizePolicy().hasHeightForWidth())
        self.CardScroll.setSizePolicy(sizePolicy)
        self.CardScroll.setMinimumSize(QSize(0, 0))
        self.verticalLayout_11 = QVBoxLayout(self.CardScroll)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Cards_Frame = QVBoxLayout()
        self.Cards_Frame.setSpacing(0)
        self.Cards_Frame.setObjectName(u"Cards_Frame")

        self.verticalLayout_11.addLayout(self.Cards_Frame)

        self.scrollArea.setWidget(self.CardScroll)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.Archive_Widget)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.MainContent_Frame)


        self.verticalLayout.addWidget(self.Main_Frame)

        self.Footer_Frame = QFrame(self.centralwidget)
        self.Footer_Frame.setObjectName(u"Footer_Frame")
        self.Footer_Frame.setStyleSheet(u"background-color: rgb(72, 208, 109);")
        self.Footer_Frame.setFrameShape(QFrame.NoFrame)
        self.Footer_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Footer_Frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Footer_Left_Frame = QFrame(self.Footer_Frame)
        self.Footer_Left_Frame.setObjectName(u"Footer_Left_Frame")
        self.Footer_Left_Frame.setFrameShape(QFrame.StyledPanel)
        self.Footer_Left_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Footer_Left_Frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.madeBy_label = QLabel(self.Footer_Left_Frame)
        self.madeBy_label.setObjectName(u"madeBy_label")
        self.madeBy_label.setMargin(5)

        self.horizontalLayout_6.addWidget(self.madeBy_label, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.Footer_Left_Frame)

        #self.Footer_Right_Frame = QFrame(self.Footer_Frame)
        #self.Footer_Right_Frame.setObjectName(u"Footer_Right_Frame")
        #self.Footer_Right_Frame.setFrameShape(QFrame.StyledPanel)
        #self.Footer_Right_Frame.setFrameShadow(QFrame.Raised)
        #self.horizontalLayout_7 = QHBoxLayout(self.Footer_Right_Frame)
        #self.horizontalLayout_7.setSpacing(0)
        #self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        #self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        #self.Github_Button = QPushButton(self.Footer_Right_Frame)
        #self.Github_Button.setObjectName(u"Github_Button")
        #self.Github_Button.setIcon(icon13)
        #self.Github_Button.setIconSize(QSize(26, 26))

        #self.horizontalLayout_7.addWidget(self.Github_Button, 0, Qt.AlignRight|Qt.AlignVCenter)


        #self.horizontalLayout_5.addWidget(self.Footer_Right_Frame)

        self.size_grip = QFrame(self.Footer_Frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.Footer_Frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MenuButton.setText("")
        self.label.setText("")
        self.AppName.setText(QCoreApplication.translate("MainWindow", u"Road Analyse", None))
        self.minimize_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.Analyse_Button.setText("")
        self.Archive_Button.setText("")
        #self.Info_Button.setText("")
        self.Settings_Button.setText("")
        self.Analyse_Label.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.Archive_Label.setText(QCoreApplication.translate("MainWindow", u"Archive", None))
        self.Settings_Label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        #self.Info_Label.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.BrowseVideo_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.BrowseKML_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.StartAnalyse_Button.setText(QCoreApplication.translate("MainWindow", u"Start Analyse", None))
        self.ProjectName_Label.setText(QCoreApplication.translate("MainWindow", u"Project Name:", None))
        self.VideoPath_Label.setText(QCoreApplication.translate("MainWindow", u"Video File:", None))
        self.KML_Label.setText(QCoreApplication.translate("MainWindow", u"KML File: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Results Directory:", None))
        self.setResultsDir.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        #self.BrowseSomething.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.restore_defaultSettings.setText(QCoreApplication.translate("MainWindow", u"Restore Default Settings", None))
        self.save_settingsButton.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        #self.label_7.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        #self.label_8.setText(QCoreApplication.translate("MainWindow", u"Links", None))
        #self.docs_Button.setText("")
        #self.colab_Button.setText("")
        #self.github_Button.setText("")
        #self.label_9.setText(QCoreApplication.translate("MainWindow", u"Info Text....", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Archive", None))
        self.refresh_button.setText("")
        self.madeBy_label.setText(QCoreApplication.translate("MainWindow", u"Dominik Bu\u010d\u00e1k", None))
        #self.Github_Button.setText("")
    # retranslateUi

