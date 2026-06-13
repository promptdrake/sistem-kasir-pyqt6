from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFrame, QRadioButton, QTableWidget, QTableWidgetItem, QHeaderView, QButtonGroup
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class CashierWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("cashierPage")
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QHBoxLayout(header_frame)
        
        logo = QLabel()
        pixmap = QPixmap("assets/ums_logo.png")
        if not pixmap.isNull():
            logo.setPixmap(pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        
        title = QLabel("Cashier")
        title.setObjectName("headerTitle")
        
        self.history_btn = QPushButton("Order History")
        self.history_btn.setObjectName("textButton")
        
        self.username_label = QLabel("username")
        self.username_label.setObjectName("usernameLabel")
        
        header_layout.addWidget(logo)
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(self.history_btn)
        header_layout.addWidget(self.username_label)
        
        # Content
        content_frame = QFrame()
        content_layout = QVBoxLayout(content_frame)
        
        input_label = QLabel("Input Data")
        input_label.setObjectName("sectionTitle")
        
        input_row = QHBoxLayout()
        
        self.nama_barang = QLineEdit()
        self.nama_barang.setPlaceholderText("Nama Barang")
        
        self.harga_barang = QLineEdit()
        self.harga_barang.setPlaceholderText("Harga Barang")
        
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Quantity")
        
        input_row.addWidget(self.nama_barang)
        input_row.addWidget(self.harga_barang)
        input_row.addWidget(self.quantity)
        
        self.add_btn = QPushButton("Add new data")
        self.add_btn.setObjectName("actionButton")
        
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Nama Barang", "Harga Barang", "Quantity", "Subtotal"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        content_layout.addWidget(input_label)
        content_layout.addLayout(input_row)
        content_layout.addWidget(self.add_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        content_layout.addWidget(self.table)
        
        # Footer
        footer_frame = QFrame()
        footer_frame.setObjectName("footerFrame")
        footer_layout = QHBoxLayout(footer_frame)
        
        calc_layout = QVBoxLayout()
        calc_label = QLabel("Total Kalkulasi:")
        self.total_label = QLabel("Rp 0")
        self.total_label.setObjectName("totalLabel")
        calc_layout.addWidget(calc_label)
        calc_layout.addWidget(self.total_label)
        
        payment_layout = QVBoxLayout()
        payment_label = QLabel("Metode Pembayaran")
        self.radio_tunai = QRadioButton("tunai")
        self.radio_qris = QRadioButton("Qris")
        self.radio_tunai.setChecked(True)
        
        self.payment_group = QButtonGroup()
        self.payment_group.addButton(self.radio_tunai)
        self.payment_group.addButton(self.radio_qris)
        
        payment_layout.addWidget(payment_label)
        payment_layout.addWidget(self.radio_tunai)
        payment_layout.addWidget(self.radio_qris)
        
        self.pay_btn = QPushButton("Bayar")
        self.pay_btn.setObjectName("payButton")
        
        footer_layout.addLayout(calc_layout)
        footer_layout.addStretch()
        footer_layout.addLayout(payment_layout)
        footer_layout.addStretch()
        footer_layout.addWidget(self.pay_btn)
        
        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame)
        main_layout.addWidget(footer_frame)
        
        self.setStyleSheet("""
            QWidget#cashierPage {
                background-color: #f5f7fb;
            }
            QFrame#headerFrame {
                background-color: white;
                border-bottom: 1px solid #e0e0e0;
                padding: 10px 20px;
            }
            QLabel#headerTitle {
                font-size: 20px;
                font-weight: 800;
                color: #212260;
                margin-left: 10px;
            }
            QPushButton#textButton {
                background-color: transparent;
                color: #212260;
                font-size: 14px;
                font-weight: bold;
                border: 1px solid #212260;
                border-radius: 15px;
                padding: 5px 15px;
                margin-right: 10px;
            }
            QPushButton#textButton:hover {
                background-color: #212260;
                color: white;
            }
            QLabel#usernameLabel {
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: #212260;
                padding: 5px 15px;
                border-radius: 15px;
            }
            QLabel#sectionTitle {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                margin-top: 10px;
                margin-bottom: 5px;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 10px;
                background-color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #212260;
            }
            QPushButton#actionButton {
                background-color: #212260;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            QPushButton#actionButton:hover {
                background-color: #31349a;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
            }
            QHeaderView::section {
                background-color: #f0f0f0;
                padding: 5px;
                border: 1px solid #e0e0e0;
                font-weight: bold;
            }
            QFrame#footerFrame {
                background-color: white;
                border-top: 1px solid #e0e0e0;
                padding: 20px;
            }
            QLabel#totalLabel {
                font-size: 24px;
                font-weight: bold;
                color: #212260;
            }
            QPushButton#payButton {
                background-color: #212260;
                color: white;
                border: none;
                font-size: 18px;
                font-weight: bold;
                padding: 15px 40px;
                border-radius: 12px;
            }
            QPushButton#payButton:hover {
                background-color: #31349a;
            }
        """)
