import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

def show_information():
    QMessageBox.information(window, "Information", "Button clicked!")

def show_warning():
    QMessageBox.warning(window, "Warning", "Button clicked!")

def show_critical():
    QMessageBox.critical(window, "Critical", "Button clicked!")

def show_confirmation():
    reply = QMessageBox.question(window, "Confirmation", "Are you sure you want to proceed?", QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        QMessageBox.information(window, "Response", "You clicked Yes!")
    else:
        QMessageBox.information(window, "Response", "You clicked No!")


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create buttons for each type of message box
info_button = QPushButton("Information", window)
info_button.setGeometry(50, 50, 100, 50)
info_button.clicked.connect(show_information)

warning_button = QPushButton("Warning", window)
warning_button.setGeometry(200, 50, 100, 50)
warning_button.clicked.connect(show_warning)

critical_button = QPushButton("Critical", window)
critical_button.setGeometry(50, 150, 100, 50)
critical_button.clicked.connect(show_critical)

confirmation_button = QPushButton("Confirmation", window)
confirmation_button.setGeometry(200, 150, 100, 50)
confirmation_button.clicked.connect(show_confirmation)

window.show()
sys.exit(app.exec_())
