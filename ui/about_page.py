from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("About Secure Messenger")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 12px;")
        layout.addWidget(title)

        info = QLabel(
            "Secure Messenger\n\n"
            "A simple, secure messaging application for sending and receiving encrypted messages.\n"
            "Developed as a project for Strathmore University.\n\n"
            "By:\n"
            "152894 Ethan Olowo\n"
            "152613 Abdalla Hafsa Fuad\n"
            "148445 Kipng'etich Gideon\n"
        )
        info.setWordWrap(True)
        layout.addWidget(info)

        self.setLayout(layout)