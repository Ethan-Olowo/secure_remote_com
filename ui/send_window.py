from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
import re

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

        layout.addWidget(QLabel("Peer Device:"))
        self.ip_dropdown = QComboBox()
        layout.addWidget(self.ip_dropdown)

        send_button = QPushButton("Send Secure Message")
        send_button.clicked.connect(self.validate_and_send)
        layout.addWidget(send_button)

        self.send_callback = send_callback
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
