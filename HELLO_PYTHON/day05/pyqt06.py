from PyQt5 import QtWidgets, uic
import sys
from anaconda_navigator.utils.qthelpers import qapplication
from random import random

form_window = uic.loadUiType("pyqt06.ui")[0]

class WindowClass(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
    def myclick(self):
        print("on")
        a=self.le1.text()
        b=self.le2.text()
        c=self.le3.text()
        
        aa=int(a)
        bb=int(b)
        cc=int(c)
        
        sum=0
        
        for i in range(aa,bb+1):
            if i%cc==0:
                sum+=i
        print(sum)
        self.le4.setText(str(sum))
        
        

if __name__ == "__main__":
    app = qapplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()