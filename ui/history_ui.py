from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class HistoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("historyPage")
        
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
        
        self.back_btn = QPushButton("Back to Cashier")
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
        
        summary_label = QLabel("Order History (All Data)")
        summary_label.setObjectName("sectionTitle")
        
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID Transaksi", "Tanggal", "Total Kalkulasi", "Items Detail"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        content_layout.addWidget(summary_label)
        content_layout.addWidget(self.table)
        
        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame)
        
        self.setStyleSheet("""
            QWidget#historyPage {
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
        """)
