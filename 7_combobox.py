import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Comboboxes")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150,100)
        button = QPushButton("Save",self)
        button.move(150,130)
        button.clicked.connect(self.getValue)
        self.combo.addItem("Python")
        self.combo.addItems(["C","C#","PHP"])
        self.show()

    def getValue(self):
        value = self.combo.currentText()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()