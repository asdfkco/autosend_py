from copy import copy
import sys
import keyboard
import pyautogui
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui.ui")[0]




class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
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

    
        
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()