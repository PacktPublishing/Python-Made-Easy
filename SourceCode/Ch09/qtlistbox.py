import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QMessageBox

def handle_selection(item):
    selected_item = item.text()
    QMessageBox.information(window, "Selection", f"You selected: {selected_item}")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("PyQt Demo")
window.setGeometry(100, 100, 400, 300)  # Set window position and size

# Create a QListWidget
list_box = QListWidget(window)
list_box.setGeometry(50, 50, 300, 200)  # Set list box position and size

# Add items to the list box
list_box.addItem("Item 1")
list_box.addItem("Item 2")
list_box.addItem("Item 3")

# Connect the handle_selection function to the itemClicked signal
list_box.itemClicked.connect(handle_selection)

window.show()
sys.exit(app.exec_())
