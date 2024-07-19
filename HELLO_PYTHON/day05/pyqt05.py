from PyQt5 import QtWidgets, uic
import sys
from anaconda_navigator.utils.qthelpers import qapplication
from random import random

form_window = uic.loadUiType("pyqt05.ui")[0]

class WindowClass(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
    def myclick(self):
        arr = list(range(1,45+1))
        for i in range(1000):
            rnd = int(random()*len(arr))
            a= arr[0]
            arr[0] = arr[rnd]
            arr[rnd]= a
            print(arr[0],arr[1],arr[2],arr[3],arr[4])
        
        self.lcd1.display(arr[0])
        self.lcd2.display(arr[1])
        self.lcd3.display(arr[2])
        self.lcd4.display(arr[3])
        self.lcd5.display(arr[4])
        self.lcd6.display(arr[5])


if __name__ == "__main__":
    app = qapplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()