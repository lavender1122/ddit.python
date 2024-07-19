from PyQt5 import QtWidgets, uic
import sys

form_window = uic.loadUiType("pyqt02.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #있는것 그대로 만들어주는것
        self.pb.clicked.connect(self.myclick) #버튼 클릭 버튼
        self.show()
    
    def myclick(self):
        a = self.lineEdit.text() #QlineEdit 는 문자 출력 할때 text() 사용
        print(a)
        aa= int(a) # str -> int
        aa+=1
        # int -> str
        self.lineEdit.setText(str(aa))
       


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())