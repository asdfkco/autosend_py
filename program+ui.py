from copy import copy
import sys
import keyboard
import pyautogui
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5 import uic

# form_class = uic.loadUiType("ui.ui")[0]

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(30, 230, 291, 71))
        self.button.setObjectName("button")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 60, 256, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.copy = QtWidgets.QLineEdit(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(40, 150, 261, 41))
        self.copy.setObjectName("copy")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button.clicked.connect(self.btnClick)



    def btnClick(self): 
        global copy_real 
        copy_real= self.copy.text()
        pyperclip.copy(copy_real)
        while(True):
            if(keyboard.is_pressed('ctrl')&keyboard.is_pressed('caps lock')):
                pyautogui.hotkey('ctrl','v')
                pyautogui.hotkey('enter')
            elif(keyboard.is_pressed('ctrl')&keyboard.is_pressed('shift')):
                break


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "PushButton"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">ctrl+caps lock 고정 멈추는 건 ctrl shift</span></p></body></html>"))
        self.copy.setText(_translate("MainWindow", "ㅂ ㅅ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



# class WindowClass(QMainWindow, form_class): 
#     def __init__(self): 
#         super().__init__()
#         self.setupUi(self)
    #     self.button.clicked.connect(self.btnClick)



    # def btnClick(self): 
    #     global copy_real 
    #     copy_real= self.copy.text()
    #     pyperclip.copy(copy_real)
    #     while(True):
    #         if(keyboard.is_pressed('ctrl')&keyboard.is_pressed('caps lock')):
    #             pyautogui.hotkey('ctrl','v')
    #             pyautogui.hotkey('enter')
    #         elif(keyboard.is_pressed('ctrl')&keyboard.is_pressed('shift')):
    #             break

    
        
         
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = WindowClass()
#     myWindow.show()
#     app.exec_()