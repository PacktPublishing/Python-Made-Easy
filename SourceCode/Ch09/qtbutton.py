import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def button_clicked():
    print("Button clicked!")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create a button
button = QPushButton("Click Me", window)
button.setGeometry(150, 150, 100, 50)  # Set button position and size
button.clicked.connect(button_clicked)  # Connect button click event to a function

window.show()
sys.exit(app.exec_())
