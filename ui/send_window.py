from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QTextEdit, QHBoxLayout
import re

class SendMessagePage(QWidget):
    def __init__(self, send_callback, encrypt_only_callback=None):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Message:"))
        self.message_input = QLineEdit()
        layout.addWidget(self.message_input)

        layout.addWidget(QLabel("Receiver Phone:"))
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_input)

        layout.addWidget(QLabel("Peer Device:"))
        self.ip_dropdown = QComboBox()
        layout.addWidget(self.ip_dropdown)

        # Buttons
        button_layout = QHBoxLayout()
        send_button = QPushButton("Send Secure Message")
        send_button.clicked.connect(self.validate_and_send)
        button_layout.addWidget(send_button)

        encrypt_only_button = QPushButton("Encrypt Only (Don't Send)")
        encrypt_only_button.clicked.connect(self.validate_and_encrypt_only)
        button_layout.addWidget(encrypt_only_button)

        layout.addLayout(button_layout)

        # Encrypted message display
        self.encrypted_label = QLabel("Encrypted Message (copy below):")
        self.encrypted_label.setVisible(False)
        layout.addWidget(self.encrypted_label)
        self.encrypted_output = QTextEdit()
        self.encrypted_output.setReadOnly(True)
        self.encrypted_output.setVisible(False)
        layout.addWidget(self.encrypted_output)

        self.send_callback = send_callback
        self.encrypt_only_callback = encrypt_only_callback
        self.setLayout(layout)

    def set_ip_choices(self, device_list):
        self.ip_dropdown.clear()
        self.device_map = {}  # device_name -> ip
        for entry in device_list:
            name = entry['device_name']
            ip = entry['ip']
            self.device_map[name] = ip
            self.ip_dropdown.addItem(name)

    def get_inputs(self):
        message = self.message_input.text()
        phone = self.phone_input.text()
        device_name = self.ip_dropdown.currentText()
        ip = self.device_map.get(device_name, device_name)
        return message, phone, ip

    def validate_and_send(self):
        phone = self.phone_input.text().strip()
        # Example: Kenyan phone number validation (starts with 07 or +2547 and 10/13 digits)
        pattern = r"^(07\d{8}|(\+2547\d{8}))$"
        if not re.match(pattern, phone):
            QMessageBox.warning(self, "Invalid Phone Number", "Please enter a valid Kenyan phone number (e.g., 0712345678 or +254712345678).")
            return
        self.send_callback()

    def validate_and_encrypt_only(self):
        phone = self.phone_input.text().strip()
        pattern = r"^(07\d{8}|(\+2547\d{8}))$"
        if not re.match(pattern, phone):
            QMessageBox.warning(self, "Invalid Phone Number", "Please enter a valid Kenyan phone number (e.g., 0712345678 or +254712345678).")
            return
        if self.encrypt_only_callback:
            self.encrypt_only_callback()

    def show_encrypted_message(self, encrypted_msg):
        self.encrypted_label.setVisible(True)
        self.encrypted_output.setVisible(True)
        self.encrypted_output.setPlainText(encrypted_msg)
