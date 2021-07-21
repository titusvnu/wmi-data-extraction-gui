from src.HardwareInfo import *
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel,  QPushButton, QWidget,QStackedLayout
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor
from PyQt5.QtCore import Qt, QSize
import sys, os, json



class Ui(QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setFixedSize(700, 400)

        self.width = 1000
        self.height = 650

        self.specsPagetitle = 'Static Specification Listing -ohTitus'
        self.settingsPagetitle = 'Settings/Config'
        self.dirc = os.path.dirname(os.path.realpath(__file__))

        self.setFixedSize(self.width, self.height)

        '''Main Window'''

        self.menu = QStackedLayout()
        
        self.specsPage = QWidget()
        self.settingsPage = QWidget()



        self.specsPageUi()
        self.settingsPageUi()

    
        self.menu.addWidget(self.specsPage)
        self.menu.addWidget(self.settingsPage)

        self.mainfont = QFont('Didact Gothic', 21)
        self.mainfont.setUnderline(True)




        


    def specsPageUi(self):


        self.specsPage.setWindowTitle(self.specsPagetitle)



        self.mainfont = QFont('Didact Gothic', 21)
        self.mainfont.setUnderline(True)
        
        
        self.specsPage.setFixedSize(self.width, self.height)
        
        self.specsPageText = QLabel(self.specsPage)

        self.background_image = QLabel('mainwindow_background', self.specsPage)
        self.background_image.setPixmap(QPixmap(self.dirc + '\\images\\specsPageBackground.png'))
        self.background_image.resize(1000, 650)



        self.os_label = QLabel('os_general', self.specsPage)
        self.os_label.setText(system_os)
        self.os_label.setFont(self.mainfont)
        self.os_label.adjustSize()
        self.os_label.move(286, 292)


        self.username_label = QLabel('username_general', self.specsPage)
        self.username_label.setText("   " + system_username + "   ")
        self.username_label.setFont(self.mainfont)
        self.username_label.adjustSize()
        self.username_label.move(286, 225)


        self.processor_label = QLabel('processor_general', self.specsPage)
        self.processor_label.setText((system_cpu.strip()))
        self.processor_label.setFont(self.mainfont)
        self.processor_label.adjustSize()
        self.processor_label.move(174, 352)


        self.motherboard_label = QLabel('motherboard_general', self.specsPage)
        self.motherboard_label.setText(system_motherboard)
        self.motherboard_label.setFont(self.mainfont)
        self.motherboard_label.adjustSize()
        self.motherboard_label.move(220, 410)

        
        self.memory_label = QLabel('memory_general', self.specsPage)
        self.memory_label.setText(str(system_memory) + " GB")
        self.memory_label.setFont(self.mainfont)
        self.memory_label.adjustSize()
        self.memory_label.move(265, 482)     

        self.gpu_label = QLabel('gpu_general', self.specsPage) 
        self.gpu_label.setText(system_graphics)
        self.gpu_label.setFont(self.mainfont)
        self.gpu_label.adjustSize()
        self.gpu_label.move(101, 552)


        self.settings_pixmap = QPixmap(self.dirc + '\\images\\widgets-buttons\\settings.png')

        self.specsPage_to_settingsPage_btn = QPushButton(self.specsPage)

        self.specsPage_to_settingsPage_btn.setIcon(QIcon(self.settings_pixmap))
        self.specsPage_to_settingsPage_btn.setIconSize(QSize(85, 85))

        self.specsPage_to_settingsPage_btn.setStyleSheet("border :3px solid black")
        self.specsPage_to_settingsPage_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.specsPage_to_settingsPage_btn.resize(90,90)
        self.specsPage_to_settingsPage_btn.move(850, 520)


        about_me_label = QLabel(self.specsPage)
        about_me_label.setText('<a href=https://github.com/ohTitus>About the Creator</a>')
        about_me_label.setOpenExternalLinks(True)
        about_me_label.setFont(QFont('KG HAPPY', 17))
        about_me_label.setStyleSheet("color: red;")
        about_me_label.move(330, 600)


    def settingsPageUi(self):

        self.settingsPage.setFixedSize(self.width, self.height)
        self.settingsPageTemplatePixmap = QPixmap(self.dirc + '\\images\\settingsPageTemplate.png')
        self.settingsPageTemplate = QLabel(self.settingsPage)
        self.settingsPageTemplate.setPixmap(self.settingsPageTemplatePixmap)
    

        self.settingsPage_to_specsPage_pixmap = QPixmap(self.dirc + '\\images\\widgets-buttons\\back_arrow.png')
        self.settingsPage_to_specsPage_btn = QPushButton(self.settingsPage)
        self.settingsPage_to_specsPage_btn.setIcon(QIcon(self.settingsPage_to_specsPage_pixmap))
        self.settingsPage_to_specsPage_btn.setIconSize(QSize(100, 100))
        self.settingsPage_to_specsPage_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsPage_to_specsPage_btn.setStyleSheet("border : transparent")
        self.settingsPage_to_specsPage_btn.move(50, 520)

        self.styling = """QCheckBox::indicator:unchecked {
    image: url(images/widgets-buttons/unchecked.png);
}

QCheckBox::indicator:checked {
    image: url(images/widgets-buttons/checked.png);
}
"""


        self.settingsPageFont = QFont('Didact Gothic', 24)
        self.StayOnTopCheckbox = QCheckBox(self.settingsPage)
        self.StayOnTopCheckbox.setStyleSheet(self.styling)
        self.StayOnTopCheckbox.move(140, 280)
        self.StayOnTopLabel = QLabel(self.settingsPage)
        self.StayOnTopLabel.setText("WindowStaysOnTop")
        self.StayOnTopLabel.setFont(self.settingsPageFont)
        self.StayOnTopLabel.setStyleSheet("color: white")
        self.StayOnTopLabel.move(80, 228)
        self.StayOnTopLabel.adjustSize()


        global config_file
        config_file = json.load(open(self.dirc + "\\src\\config.json", "r+"))

        if config_file["StayOnTopHint"] == True:
            self.specsPage.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
            self.StayOnTopCheckbox.setChecked(True)
        else:
            pass
        
        print(config_file)




class Main(QMainWindow, Ui):

    def __init__(self):

        super(Main, self).__init__()
        self.setupUi(self)
        
        self.specsPage_to_settingsPage_btn.clicked.connect(self.settingsPageIndex)
        self.settingsPage_to_specsPage_btn.clicked.connect(self.specsPageIndex)
        self.StayOnTopCheckbox.toggled.connect(self.StayOnTopSwitch)

    def StayOnTopSwitch(self):
        json_true = {
            "StayOnTopHint": True
        }
        json_false = {
            "StayOnTopHint": False
        }


        if self.StayOnTopCheckbox.isChecked() == True:

            self.specsPage.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

            with open(self.dirc + "\\src\\config.json", "r+") as out_file:
                json.dump(json_true, out_file, indent=6)
                out_file.truncate()

        else:
            self.specsPage.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)

            with open(self.dirc + "\\src\\config.json", "r+") as out_file:
                json.dump(json_false, out_file, indent=6)
                out_file.truncate()
            self.StayOnTopCheckbox.isChecked() == False

    def specsPageIndex(self):
        self.menu.setCurrentIndex(0)

    def settingsPageIndex(self):

        self.menu.setCurrentIndex(1)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    M = Main()
    sys.exit(app.exec())
    
 