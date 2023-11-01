from PyQt6.QtWidgets import QApplication, QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QWidget()
    windows.show()
    app.exec()
