import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton


def convert_length():
    length = float(length_input.text())
    units = unit_combo.currentText()

    if units == "Centimeters to Inches":
        result = length / 2.54
    elif units == "Inches to Centimeters":
        result = length * 2.54
    elif units == "Centimeters to Feet":
        result = length / 30.48
    elif units == "Feet to Centimeters":
        result = length * 30.48
    elif units == "Inches to Feet":
        result = length / 12
    elif units == "Feet to Inches":
        result = length * 12
    else:
        result = length

    result_label.setText(f"Result: {result:.2f}")


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Length Converter")
window.setGeometry(100, 100, 400, 200)

main_widget = QWidget()
window.setCentralWidget(main_widget)

layout = QVBoxLayout()
main_widget.setLayout(layout)

length_input = QLineEdit()
layout.addWidget(length_input)

unit_combo = QComboBox()
unit_combo.addItems([
    "Centimeters to Inches",
    "Inches to Centimeters",
    "Centimeters to Feet",
    "Feet to Centimeters",
    "Inches to Feet",
    "Feet to Inches"
])
layout.addWidget(unit_combo)

convert_button = QPushButton("Convert")
convert_button.clicked.connect(convert_length)
layout.addWidget(convert_button)

result_label = QLabel("Result: ")
layout.addWidget(result_label)

window.show()
sys.exit(app.exec_())
