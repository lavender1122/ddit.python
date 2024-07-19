from PyQt5 import QtWidgets, uic
import sys
from anaconda_navigator.utils.qthelpers import qapplication

form_window = uic.loadUiType("pyqt04.ui")[0]

class WindowClass(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
    def myclick(self):
        dan= self.le.text()
        idan=int(dan)
        txt =""
        
        for i in range(1,9+1):
            txt +="{}*{}={}\n".format(dan,i,i*idan)
        
        self.te.setText(txt)
           
        

    

if __name__ == "__main__":
    app = qapplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()