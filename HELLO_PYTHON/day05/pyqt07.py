from PyQt5 import QtWidgets, uic
import sys
from random import random
from PyQt5.Qt import QMessageBox

form_window = uic.loadUiType("pyqt07.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.mycall)

    def myclick(self):
        str_old = self.le.text() 
        str_new = self.sender().text() # sender : 기존에 존재하는 text의 값을 가져옴
        self.le.setText(str_old+str_new)
    
    def mycall(self):
        str = self.le.text()
        QMessageBox.about(self,'Calling',str) # 파이썬 alert 창
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())