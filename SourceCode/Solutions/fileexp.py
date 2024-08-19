import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel

class FileExplorerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)

        # Create a tree view widget
        self.tree_view = QTreeView(self)
        self.tree_view.setGeometry(50, 50, 700, 500)

        # Create a file system model and set it on the tree view
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.tree_view.setModel(self.model)

        # Set the root index of the model to display the file system
        self.tree_view.setRootIndex(self.model.index("/"))

        # Connect item selection signal to handle_file_selection method
        self.tree_view.selectionModel().selectionChanged.connect(self.handle_file_selection)

    def handle_file_selection(self, selected, deselected):
        # Get the selected file path
        indexes = self.tree_view.selectionModel().selectedIndexes()
        if len(indexes) > 0:
            index = indexes[0]
            file_path = self.model.filePath(index)
            print("Selected File:", file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorerWindow()
    window.show()
    sys.exit(app.exec_())
