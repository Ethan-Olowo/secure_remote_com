from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class SendMessagePage(QWidget):
    def __init__(self, send_callback):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Message:"))
        self.message_input = QLineEdit()
        layout.addWidget(self.message_input)

        layout.addWidget(QLabel("Receiver Phone:"))
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_input)

        layout.addWidget(QLabel("Peer IP:"))
        self.ip_input = QLineEdit()
        layout.addWidget(self.ip_input)

        send_button = QPushButton("Send Secure Message")
        send_button.clicked.connect(send_callback)
        layout.addWidget(send_button)

        self.setLayout(layout)

    def get_inputs(self):
        return self.message_input.text(), self.phone_input.text(), self.ip_input.text()
