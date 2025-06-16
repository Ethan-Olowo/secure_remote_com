from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class ReceiveMessagePage(QWidget):
    def __init__(self, decrypt_callback):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Receive Secure Message"))
        layout.addSpacing(10)

        layout.addWidget(QLabel("Enter OTP:"))
        self.otp_input = QLineEdit()
        layout.addWidget(self.otp_input)

        layout.addWidget(QLabel("Paste Encrypted Message:"))
        self.encrypted_input = QTextEdit()
        layout.addWidget(self.encrypted_input)

        decrypt_button = QPushButton("Decrypt Message")
        decrypt_button.clicked.connect(decrypt_callback)
        layout.addWidget(decrypt_button)

        self.setLayout(layout)

    def get_otp(self):
        return self.otp_input.text()

    def get_encrypted_message(self):
        return self.encrypted_input.toPlainText().strip()
