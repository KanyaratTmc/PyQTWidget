import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtGui import QFont

font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Message Boxes")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        button = QPushButton("Click ME!", self)
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.messageBox)
        self.show()

    def messageBox(self):
        mbox = QMessageBox()
        mbox.setWindowTitle("Warning!!!")
        mbox.setText("Are you sure to exit?")
        mbox.setIcon(QMessageBox.Icon.Question)
        mbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
        mbox.setDefaultButton(QMessageBox.StandardButton.No)
        buttonReply = mbox.exec()

        if buttonReply == QMessageBox.StandardButton.Yes:
            sys.exit()
        elif buttonReply == QMessageBox.StandardButton.No:
            print("You Clicked No Button")
    
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()