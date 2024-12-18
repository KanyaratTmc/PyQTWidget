import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLabel

class Window(QWidget): #inherit from QWidget
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #X Y W h
        self.setWindowTitle("Using Lable")
        self.UI()
    
    def UI(self):
        text1=QLabel("Hello Python",self) #ต้องใส่ self เสมอ ถึงจะแสดงผล
        text2=QLabel("Hello World",self)
        text1.move(50,50)
        text2.move(200,150)
        self.show()

def main():
    App = QApplication(sys.argv) #รับคำสั่งจาก cmd
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()