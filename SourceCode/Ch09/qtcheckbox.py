import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

def handle_checkbox(checked):
    if checked:
        print("Checkbox is checked")
    else:
        print("Checkbox is unchecked")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create a QCheckBox
checkbox = QCheckBox("Enable", window)
checkbox.setGeometry(50, 50, 100, 30)  # Set checkbox position and size
checkbox.stateChanged.connect(handle_checkbox)  # Connect checkbox state change to a function

window.show()
sys.exit(app.exec_())
