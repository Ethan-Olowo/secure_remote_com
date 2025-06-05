from PyQt6.QtWidgets import (
    QMainWindow, QTextEdit, QStatusBar, QMessageBox, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from ui.send_window import SendMessagePage
from ui.receive_window import ReceiveMessagePage
from ui.about_page import AboutPage

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Secure Messenger")
        self.resize(600, 400)

        # Color scheme variables
        columbia_blue = "#bfd7ea"
        cadet_gray = "#91aec1"
        air_force_blue = "#508ca4"
        sea_green = "#0a8754"
        cal_poly_green = "#004f2d"

        # Set main stylesheet for color scheme and padding
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {columbia_blue};
            }}
            QWidget {{
                background-color: {columbia_blue};
                color: {cal_poly_green};
                font-size: 15px;
            }}
            QPushButton {{
                background-color: {air_force_blue};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 18px;
                margin: 6px 0;
            }}
            QPushButton:hover {{
                background-color: {sea_green};
            }}
            QLabel {{
                color: {cal_poly_green};
                padding: 4px 0;
            }}
            QTextEdit {{
                background-color: {cadet_gray};
                color: {cal_poly_green};
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
            }}
            QStatusBar {{
                background-color: {air_force_blue};
                color: white;
                padding: 6px;
            }}
        """)


        # Sidebar setup
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(18, 18, 18, 18)  # Padding inside sidebar
        sidebar_layout.setSpacing(12)
        sidebar.setLayout(sidebar_layout)
        sidebar.setFixedWidth(180)
        sidebar.setStyleSheet(f"background-color: {cadet_gray}; border-radius: 12px;")

        # Server control with indicator
        server_row = QHBoxLayout()
        server_row.setSpacing(10)
        self.server_btn = QPushButton("Start Server")
        self.server_btn.clicked.connect(self.toggle_server)

        self.server_indicator = QLabel()
        self.set_server_indicator(False)
        self.server_indicator.setFixedSize(16, 16)
        self.server_indicator.setStyleSheet("margin-left: 8px; margin-right: 8px;")

        server_row.addWidget(self.server_btn)
        server_row.addWidget(self.server_indicator)
        server_row.addStretch()

        sidebar_layout.addLayout(server_row)
        sidebar_layout.addSpacing(10)

        btn_send = QPushButton("Send Message")
        btn_send.clicked.connect(self.controller.show_send_page)
        sidebar_layout.addWidget(btn_send)

        btn_receive = QPushButton("Receive Message")
        btn_receive.clicked.connect(self.controller.show_receive_page)
        sidebar_layout.addWidget(btn_receive)

        sidebar_layout.addSpacing(10)

        btn_about = QPushButton("About")
        btn_about.clicked.connect(self.show_about)
        sidebar_layout.addWidget(btn_about)

        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.close)
        sidebar_layout.addWidget(btn_exit)

        sidebar_layout.addStretch()

        # Central area setup (will swap widgets here)
        self.central_area = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_layout.setContentsMargins(24, 24, 24, 24)  # Padding inside central area
        self.central_layout.setSpacing(16)
        self.central_area.setLayout(self.central_layout)

        self.central_log = QTextEdit("Welcome to Secure Messenger.")
        self.central_log.setReadOnly(True)
        self.central_log.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.central_layout.addWidget(self.central_log)

        # Main layout: sidebar + central area
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_widget.setLayout(main_layout)
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.central_area, 1)  # Stretch factor for central area

        self.setCentralWidget(main_widget)

        self.server_running = False

    def set_server_indicator(self, running: bool):
        color = "#0a8754" if running else "#b22222"  # green or red
        self.server_indicator.setStyleSheet(
            f"background-color: {color}; border-radius: 8px; border: 1px solid #333;"
        )

    def toggle_server(self):
        if self.server_running:
            self.controller.stop_server()
        else:
            self.controller.start_server()

    def update_server_status(self, running: bool):
        self.server_running = running
        self.set_server_indicator(running)
        self.server_btn.setText("Stop Server" if running else "Start Server")

    def show_about(self):
        self.set_central_widget(AboutPage())

    def set_central_widget(self, widget):
        # Remove old widgets from central_layout
        for i in reversed(range(self.central_layout.count())):
            old_widget = self.central_layout.itemAt(i).widget()
            if old_widget:
                old_widget.setParent(None)
        self.central_layout.addWidget(widget)

    def show_log(self):
        self.set_central_widget(self.central_log)
