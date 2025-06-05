from controller import SecureMessengerController
import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("Secure Messenger")

    controller = SecureMessengerController(None)
    window = MainWindow(controller)
    controller.main_window = window

    window.show()
    sys.exit(app.exec())
