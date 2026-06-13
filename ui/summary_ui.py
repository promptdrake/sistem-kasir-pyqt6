from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class SummaryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("summaryPage")
        
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
        
        title = QLabel("Kasir")
        title.setObjectName("headerTitle")
        
        self.back_btn = QPushButton("Kembali Ke Kasir")
        self.back_btn.setObjectName("textButton")
        
        self.username_label = QLabel("username")
        self.username_label.setObjectName("usernameLabel")
        
        header_layout.addWidget(logo)
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(self.back_btn)
        header_layout.addWidget(self.username_label)
        
        # Content
        content_frame = QFrame()
        content_layout = QVBoxLayout(content_frame)
        
        summary_label = QLabel("Ringkasan Pembelian")
        summary_label.setObjectName("sectionTitle")
        
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Nama Barang", "Harga Barang", "Quantity"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Details section
        details_layout = QHBoxLayout()
        
        col1 = QVBoxLayout()
        method_title = QLabel("Metode Pembayaran")
        method_title.setObjectName("detailTitle")
        self.method_val = QLabel("tunai")
        self.method_val.setObjectName("detailValue")
        
        date_title = QLabel("Pembelian Tanggal")
        date_title.setObjectName("detailTitle")
        self.date_val = QLabel("dd - mm - yyyy")
        self.date_val.setObjectName("detailValue")
        
        col1.addWidget(method_title)
        col1.addWidget(self.method_val)
        col1.addSpacing(10)
        col1.addWidget(date_title)
        col1.addWidget(self.date_val)
        col1.addStretch()
        
        col2 = QVBoxLayout()
        total_title = QLabel("Total Kalkulasi")
        total_title.setObjectName("detailTitle")
        self.total_val = QLabel("Rp 0")
        self.total_val.setObjectName("detailValue")
        col2.addWidget(total_title)
        col2.addWidget(self.total_val)
        col2.addStretch()
        
        details_layout.addLayout(col1)
        details_layout.addLayout(col2)
        
        content_layout.addWidget(summary_label)
        content_layout.addWidget(self.table)
        content_layout.addLayout(details_layout)
        
        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame)
        
        self.setStyleSheet("""
            QWidget#summaryPage {
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
            QLabel#detailTitle {
                font-size: 16px;
                font-weight: bold;
                color: #333;
            }
            QLabel#detailValue {
                font-size: 16px;
                color: #555;
            }
        """)
