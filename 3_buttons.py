import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Button")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

#ทำไมบางอันมี self บางอันไม่มี เนื่องจาก 
    def UI(self):
        #ถ้ามีใช้จากที่อิ่น ควรใส่ self ไปด้วย
        self.text = QLabel("My Text",self)
        enterButton = QPushButton("Enter",self)
        exitButton = QPushButton("Exit",self)
        self.text.move(160,50)
        enterButton.move(100,80)
        exitButton.move(200,80)

        enterButton.clicked.connect(self.enterFunc) #คลิกแล้วไปไหน ไป enterFunc ด้านล่าง ใส่ self ไปด้วย
        exitButton.clicked.connect(self.exitFunc)

        self.show()

    def enterFunc(self):
        self.text.setText("You clicked Enter")
        self.text.resize(150,20) #ปรับขนาด ให้แสดงผลครบทุกคำ

    def exitFunc(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150,20)  

#

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())  # Changed from exec_() to exec()

if __name__ == '__main__':
    main()