import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap

def convert():
    if conversions.currentIndex() == 0:
        n = float(userInput.text()) * 0.39
        textLabel.setText(str(n))
    elif conversions.currentIndex() == 1:
        n = float(userInput.text()) * 2.54
        textLabel.setText(str(n))
    elif conversions.currentIndex() == 2:
        n = float(userInput.text()) * 0.62
        textLabel.setText(str(n))
    elif conversions.currentIndex() == 3:
        n = float(userInput.text()) * 1.60
        textLabel.setText(str(n))

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Unit Converter")
window.setGeometry(500, 20, 525, 180)

widget = QWidget(window)
window.setCentralWidget(widget)

layout = QGridLayout()
widget.setLayout(layout)


imgLabel = QLabel()
pixmap = QPixmap("logo.png")
imgLabel.setPixmap(pixmap)
layout.addWidget(imgLabel, 0, 0, 4, 1)  # span 4 rows, 1 column

textLabel = QLabel("Convert:")
layout.addWidget(textLabel, 0, 1)

conversions = QComboBox()
conversions.addItems([
    "Cm to Inch",
    "Inch to Cm",
    "Km to Miles",
    "Miles to Km"
])
layout.addWidget(conversions, 0, 2)

userInput = QLineEdit()
layout.addWidget(userInput, 1, 1, 1, 2)  # span 1 row, 2 columns

textLabel = QLabel()
layout.addWidget(textLabel, 2, 1, 1, 2)  # span 1 row, 2 columns

myButton = QPushButton("OK")
myButton.clicked.connect(convert)
layout.addWidget(myButton, 3, 1, 1, 2)  # span 1 row, 2 columns



window.show()
sys.exit(app.exec_())
