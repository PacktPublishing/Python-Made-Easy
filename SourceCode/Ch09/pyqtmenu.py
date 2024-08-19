import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt5 Demo")
window.setGeometry(100, 100, 400, 300)

# Create a menu bar
menu_bar = window.menuBar()

# Create a menu
file_menu = menu_bar.addMenu("File")

# Create a menu item
exit_action = QAction("Exit", window)
exit_action.triggered.connect(window.close)

# Add the menu item to the menu
file_menu.addAction(exit_action)

window.show()

sys.exit(app.exec_())
