import sys
from PyQt6.QtWidgets import QApplication,QWidget

class Window(QWidget): #inherit from QWidget
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,250) #ตำแหน่ง X Y /ขนาด W h
        self.setWindowTitle("This our window's Title")
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()