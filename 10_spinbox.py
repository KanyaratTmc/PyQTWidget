import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QPushButton
from PyQt6.QtGui import QFont

font = QFont("Angsana", 16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spin Boxes")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150,100)
        self.spinBox.setFont(font)
        self.spinBox.setRange(25,110)
        self.spinBox.setSuffix(" cm")
        self.spinBox.setSingleStep(5)
        button = QPushButton("send",self)
        button.move(150,140)
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.spinBox.value()
        print(value)




def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()