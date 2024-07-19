from PyQt5 import QtWidgets, uic
import sys
from random import random
from PyQt5.Qt import QMessageBox

form_window = uic.loadUiType("pyqt10.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        self.b = int(random()*99)+1
        print("com",self.com)
    
    
    def myclick(self):
        mine = self.le.text()
        print(mine)
        imine = int(mine)
        
        rnd = int(self.b)
        print(rnd)
        
        result=""
        
        if imine == rnd:
            result+=mine+"anwser" 
            QMessageBox.about(self,'result1',result) # 파이썬 alert 창
        if imine < rnd:
            result+=mine+"up\n"
        if imine > rnd:
            result+=mine+"dw\n"
            
        str_old = self.pte.toPlainText()
        self.pte.setPlainText(str_old+result)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())