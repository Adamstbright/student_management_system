from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit,QPushButton, QMainWindow
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
        super().__init__()
        self.setWindowTitle("Student management system")

        # Create menu items
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        # Create sub_menu items
        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

app = QApplication(sys.argv)
student_app = MainWindow()
student_app.show()
sys.exit(app.exec())