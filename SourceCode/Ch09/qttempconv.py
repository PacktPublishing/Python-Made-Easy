import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Temperature Converter")
window.setGeometry(100, 100, 400, 200)

widget = QWidget(window)
window.setCentralWidget(widget)

layout = QGridLayout()
widget.setLayout(layout)

input_label = QLabel("Temperature:")
layout.addWidget(input_label, 0, 0)

input_field = QLineEdit()
layout.addWidget(input_field, 0, 1)

celsius_button = QRadioButton("Celsius")
layout.addWidget(celsius_button, 1, 0)

fahrenheit_button = QRadioButton("Fahrenheit")
layout.addWidget(fahrenheit_button, 1, 1)

convert_button = QPushButton("Convert")
layout.addWidget(convert_button, 2, 0, 1, 2)

output_label = QLabel()
layout.addWidget(output_label, 3, 0, 1, 2)

def convert_temperature():
    try:
        temperature = float(input_field.text())
        if celsius_button.isChecked():
            converted_temperature = (temperature * 9/5) + 32
            output_label.setText(f"{temperature} °C = {converted_temperature} °F")
        elif fahrenheit_button.isChecked():
            converted_temperature = (temperature - 32) * 5/9
            output_label.setText(f"{temperature} °F = {converted_temperature} °C")
        else:
            output_label.setText("Please select Celsius or Fahrenheit.")
    except ValueError:
        output_label.setText("Invalid input.")

convert_button.clicked.connect(convert_temperature)

window.show()
sys.exit(app.exec_())
