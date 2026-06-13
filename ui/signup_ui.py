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


class SignupWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("signupPage")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setObjectName("signupCard")
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
        title = QLabel("Create Account")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Error message
        self.msg_label = QLabel("")
        self.msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.msg_label.setObjectName("msgLabel")

        # Username
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        # Password
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Confirm Password
        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.setEchoMode(QLineEdit.EchoMode.Password)

        # Sign Up Button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setMinimumHeight(45)

        # Login Link
        self.login_link = QPushButton("Already have an account? Log in")
        self.login_link.setObjectName("linkButton")
        self.login_link.setCursor(Qt.CursorShape.PointingHandCursor)

        # Footer
        footer = QLabel("© 2026 UMS Cashier")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setObjectName("footerLabel")

        # Add widgets
        card_layout.addWidget(logo)
        card_layout.addSpacing(10)
        card_layout.addWidget(title)
        card_layout.addWidget(self.msg_label)
        card_layout.addWidget(self.username)
        card_layout.addWidget(self.password)
        card_layout.addWidget(self.confirm_password)
        card_layout.addSpacing(10)
        card_layout.addWidget(self.signup_button)
        card_layout.addWidget(self.login_link)
        card_layout.addSpacing(10)
        card_layout.addWidget(footer)

        main_layout.addWidget(card)

        self.setStyleSheet("""
            QWidget#signupPage {
                background-color: #f5f7fb;
            }

            QFrame#signupCard {
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