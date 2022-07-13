from PySide2.QtWidgets import QApplication
from controllers.main_window import ModelWindow

if __name__ == "__main__":
    app = QApplication()
    window = ModelWindow()
    window.show()

    app.exec_()