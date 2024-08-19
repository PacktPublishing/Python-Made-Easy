import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

window.show()
