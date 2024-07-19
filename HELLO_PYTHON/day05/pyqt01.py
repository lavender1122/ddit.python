from PyQt5 import QtWidgets, uic
import sys

form_window = uic.loadUiType("pyqt01.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #있는것 그대로 만들어주는것
        self.pb.clicked.connect(self.myclick)
        self.show()
        self.clicked_once = False  # 버튼이 클릭되었는지 여부를 저장하는 변수

    def myclick(self):
        if not self.clicked_once:  # 처음 클릭되었을 때
            self.lbl.setText("Good Evening!")
            self.clicked_once = True
        else:  # 두 번째 클릭되었을 때
            self.lbl.setText("Good Morning!")
            self.clicked_once = False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())