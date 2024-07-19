from PyQt5 import QtWidgets, uic
import sys
from random import random
from PyQt5.Qt import QMessageBox

form_window = uic.loadUiType("pyqt08.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()

    def myclick(self):
        self.pte.setText("")
        f= self.le_first.text()
        l= self.le_last.text()
        print(f)
        print(l)
        
        ff=int(f)
        ll=int(l)
        
        for i in range(ff,ll+1):
            # print(i)
            star ="⭐"*i
            print("⭐"*i)
            # self.pte.setText("1")
            self.pte.append(star)
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())