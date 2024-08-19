import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create a QLabel
label = QLabel("This is a text label!", window)
label.setGeometry(50, 50, 200, 30)  # Set label position and size

window.show()
sys.exit(app.exec_())
