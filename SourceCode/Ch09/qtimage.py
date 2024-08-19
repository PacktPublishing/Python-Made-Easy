import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create a QLabel widget to display the image
image_label = QLabel(window)

# Load the image using QPixmap
pixmap = QPixmap('rocket.png')

# Set the image pixmap on the QLabel
image_label.setPixmap(pixmap)

# Set the geometry of the QLabel to fit the image
image_label.setGeometry(50, 50, pixmap.width(), pixmap.height())

window.show()

sys.exit(app.exec_())
