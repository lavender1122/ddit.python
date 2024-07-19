from PyQt5 import QtWidgets, uic
import sys

form_window = uic.loadUiType("pyqt03.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #있는것 그대로 만들어주는것
        self.pb.clicked.connect(self.myclick) #버튼 클릭 버튼
        self.show()
    
    def myclick(self):
        f =self.le01.text()
        s =self.le02.text()
       
        ff= int(f)
        ss= int(s)
       
        sum = ff-ss
        print(sum)
        self.le03.setText(str(sum))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())