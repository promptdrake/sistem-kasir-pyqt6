from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
    QSizePolicy,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("loginPage")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setObjectName("loginCard")
        card.setMaximumWidth(500)
        card.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(15)

        # Logo
        logo = QLabel()
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap("assets/ums_logo.png")
        if pixmap.isNull():
            logo.setText("Logo not found")
        else:
            logo.setPixmap(
                pixmap.scaled(
                    320,
                    120,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )

        # Title
        title = QLabel("UMS Cashier")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Subtitle
        subtitle = QLabel("Universitas Muhammadiyah Surakarta")
        subtitle.setObjectName("subtitleLabel")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Message Label
        self.msg_label = QLabel("")
        self.msg_label.setObjectName("msgLabel")
        self.msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Username
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        # Password
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.setMinimumHeight(45)

        # Sign Up Link
        self.signup_link = QPushButton("Don't have an account? Sign up")
        self.signup_link.setObjectName("linkButton")
        self.signup_link.setCursor(Qt.CursorShape.PointingHandCursor)

        # Footer
        footer = QLabel("© 2026 UMS Cashier")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setObjectName("footerLabel")

        # Layout
        card_layout.addWidget(logo)
        card_layout.addSpacing(10)
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(20)
        card_layout.addWidget(self.msg_label)
        card_layout.addWidget(self.username)
        card_layout.addWidget(self.password)
        card_layout.addSpacing(10)
        card_layout.addWidget(self.login_button)
        card_layout.addWidget(self.signup_link)
        card_layout.addSpacing(10)
        card_layout.addWidget(footer)

        main_layout.addWidget(card)

        self.setStyleSheet("""
            QWidget#loginPage {
                background-color: #f5f7fb;
            }

            QFrame#loginCard {
                background-color: white;
                border: none;
                border-radius: 18px;
            }

            QLabel {
                background: transparent;
            }

            QLabel#titleLabel {
                color: #212260;
                font-size: 30px;
                font-weight: bold;
            }

            QLabel#subtitleLabel {
                color: #777777;
                font-size: 13px;
            }

            QLabel#msgLabel {
                color: red;
                font-size: 13px;
            }

            QLabel#footerLabel {
                color: #999999;
                font-size: 11px;
            }

            QLineEdit {
                border: 2px solid #dddddd;
                border-radius: 10px;
                padding: 12px;
                font-size: 14px;
                background-color: white;
            }

            QLineEdit:focus {
                border: 2px solid #212260;
            }

            QPushButton {
                background-color: #212260;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 15px;
                font-weight: bold;
                min-height: 45px;
            }

            QPushButton:hover {
                background-color: #31349a;
            }

            QPushButton:pressed {
                background-color: #1a1c4d;
            }

            QPushButton#linkButton {
                background: transparent;
                color: #212260;
                font-size: 12px;
                font-weight: normal;
                text-decoration: underline;
                min-height: 25px;
            }

            QPushButton#linkButton:hover {
                color: #31349a;
            }
        """)