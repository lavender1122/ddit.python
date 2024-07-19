from PyQt5 import QtWidgets, uic
import sys
from random import random
from PyQt5.Qt import QMessageBox

form_window = uic.loadUiType("pyqt09.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()

    def myclick(self):
        mine = self.le_mine.text()
        com=""
        result=""
        
        rnd = random()
        
        if rnd >0.66:
            com="가위"
        elif rnd >0.33:
            com="바위"
        else:
            com="보"
       
        
        if mine == com : result="비김"
        
        if com == "가위" and mine =="바위" : result="짐"
        if com == "가위" and mine =="보" : result="이김"
        
        if com == "바위" and mine =="가위" : result="짐"
        if com == "바위" and mine =="보" : result="이김"
        
        if com == "보" and mine =="가위" : result="이김"
        if com == "보" and mine =="바위" : result="짐"
        
        # if mine=="가위"and com=="보" or mine=="바위"and com=="가위" or mine=="보"and com=="바위":
        #     result= "이김"
        # if mine=="가위"and com=="바위" or mine=="바위"and com=="보" or mine=="보"and com=="가위":
        #     result= "짐"
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())