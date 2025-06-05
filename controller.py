from ui.main_window import MainWindow
from ui.send_window import SendMessagePage
from ui.receive_window import ReceiveMessagePage
from sms import generate_otp, send_otp_via_sms
from client import send_secure_message_to_peer, read_secure_message_from_local
from PyQt6.QtWidgets import QMessageBox
import subprocess, sys, os, signal

class SecureMessengerController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.send_page = SendMessagePage(self.send_secure_message)
        self.receive_page = ReceiveMessagePage(self.read_secure_message)
        self.server_process = None

    def show_send_page(self):
        self.main_window.set_central_widget(self.send_page)

    def show_receive_page(self):
        self.main_window.set_central_widget(self.receive_page)

    def send_secure_message(self):
        message, phone, ip = self.send_page.get_inputs()
        if not message or not phone or not ip:
            QMessageBox.warning(self.main_window, "Input Error", "All fields required.")
            return

        otp = generate_otp()
        send_otp_via_sms(phone, otp)
        try:
            status = send_secure_message_to_peer(message, otp, ip)
            if status == 200:
                QMessageBox.information(self.main_window, "Success", "Message sent!")
            else:
                QMessageBox.critical(self.main_window, "Error", f"Status: {status}")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", str(e))

    def read_secure_message(self):
        otp = self.receive_page.get_otp()
        if not otp:
            return

        try:
            msg = read_secure_message_from_local(otp)
            if msg:
                QMessageBox.information(self.main_window, "Decrypted", msg)
            else:
                QMessageBox.warning(self.main_window, "Failed", "No message or bad OTP.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", str(e))

    def start_server(self):
        if self.server_process is None:
            self.server_process = subprocess.Popen([sys.executable, "server.py"])
            self.main_window.update_server_status(True)
            QMessageBox.information(self.main_window, "Server", "Local server started.")

    def stop_server(self):
        if self.server_process:
            if sys.platform == "win32":
                self.server_process.terminate()
            else:
                os.kill(self.server_process.pid, signal.SIGTERM)
            self.server_process.wait()
            self.server_process = None
            self.main_window.update_server_status(False)
            QMessageBox.information(self.main_window, "Server", "Server stopped.")

