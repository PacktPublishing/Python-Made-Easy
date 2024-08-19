import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create a QLineEdit widget
text_field = QLineEdit(window)
text_field.setGeometry(50, 50, 300, 30)  # Set text field position and size

window.show()
sys.exit(app.exec_())
