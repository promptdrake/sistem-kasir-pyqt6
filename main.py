import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from ui.login_ui import LoginWidget
from ui.signup_ui import SignupWidget
from ui.cashier_ui import CashierWidget
from ui.history_ui import HistoryWidget
from ui.summary_ui import SummaryWidget
from PyQt6.QtWidgets import QTableWidgetItem
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UMS Cashier App")
        self.resize(1200, 800)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.current_user = None
        self.cart = []


        self.login_widget = LoginWidget()
        self.signup_widget = SignupWidget()
        self.cashier_widget = CashierWidget()
        self.history_widget = HistoryWidget()
        self.summary_widget = SummaryWidget()

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.signup_widget)
        self.stacked_widget.addWidget(self.cashier_widget)
        self.stacked_widget.addWidget(self.history_widget)
        self.stacked_widget.addWidget(self.summary_widget)

        self.login_widget.signup_link.clicked.connect(self.go_to_signup)
        self.signup_widget.login_link.clicked.connect(self.go_to_login)

        self.login_widget.login_button.clicked.connect(self.handle_login)
        self.signup_widget.signup_button.clicked.connect(self.handle_signup)
        
        self.cashier_widget.history_btn.clicked.connect(self.go_to_history)
        self.cashier_widget.add_btn.clicked.connect(self.add_item)
        self.cashier_widget.pay_btn.clicked.connect(self.handle_payment)
        
        self.history_widget.back_btn.clicked.connect(self.go_to_cashier)
        self.summary_widget.back_btn.clicked.connect(self.go_to_cashier)

    def go_to_signup(self):
        self.stacked_widget.setCurrentWidget(self.signup_widget)
        self.signup_widget.msg_label.setText("")

    def go_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_widget)
        self.login_widget.msg_label.setText("")

    def handle_login(self):
        username = self.login_widget.username.text()
        password = self.login_widget.password.text()

        if not username or not password:
            self.login_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.login_widget.msg_label.setText("Isi semua input yang diperlukan")
            return

        success, msg = database.verify_user(username, password)
        if success:
            self.current_user = username
            self.login_widget.msg_label.setStyleSheet("color: green; font-size: 13px;")
            self.login_widget.msg_label.setText("Login Berhasil")
            self.login_widget.username.clear()
            self.login_widget.password.clear()
            self.go_to_cashier()
        else:
            self.login_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.login_widget.msg_label.setText(msg)

    def handle_signup(self):
        username = self.signup_widget.username.text()
        password = self.signup_widget.password.text()
        confirm_password = self.signup_widget.confirm_password.text()

        if not username or not password or not confirm_password:
            self.signup_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.signup_widget.msg_label.setText("Isi semua input yang diperlukan")
            return

        if password != confirm_password:
            self.signup_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.signup_widget.msg_label.setText("Password tidak cocok")
            return

        success, msg = database.create_user(username, password)
        if success:
            self.signup_widget.msg_label.setStyleSheet("color: green; font-size: 13px;")
            self.signup_widget.msg_label.setText("Akun berhasil dibuat! Silahkan login")
            self.signup_widget.username.clear()
            self.signup_widget.password.clear()
            self.signup_widget.confirm_password.clear()
            QMessageBox.information(self, "Success", "Akun berhasil dibuat! Silahkan login")
            self.go_to_login()
        else:
            self.signup_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.signup_widget.msg_label.setText(msg)

    def go_to_cashier(self):
        self.cashier_widget.username_label.setText(self.current_user)
        self.stacked_widget.setCurrentWidget(self.cashier_widget)
        
    def add_item(self):
        name = self.cashier_widget.nama_barang.text()
        harga_str = self.cashier_widget.harga_barang.text()
        qty_str = self.cashier_widget.quantity.text()
        
        if not name or not harga_str or not qty_str:
            QMessageBox.warning(self, "Warning", "Isi semua input yang diperlukan")
            return
            
        try:
            harga = float(harga_str)
            qty = int(qty_str)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Harga harus berupa angka dan quantity harus berupa integer")
            return
            
        subtotal = harga * qty
        self.cart.append({'name': name, 'price': harga, 'quantity': qty})
        
        row = self.cashier_widget.table.rowCount()
        self.cashier_widget.table.insertRow(row)
        self.cashier_widget.table.setItem(row, 0, QTableWidgetItem(name))
        self.cashier_widget.table.setItem(row, 1, QTableWidgetItem(f"Rp {harga:,.2f}"))
        self.cashier_widget.table.setItem(row, 2, QTableWidgetItem(str(qty)))
        self.cashier_widget.table.setItem(row, 3, QTableWidgetItem(f"Rp {subtotal:,.2f}"))
        
        self.cashier_widget.nama_barang.clear()
        self.cashier_widget.harga_barang.clear()
        self.cashier_widget.quantity.clear()
        self.update_total()
        
    def update_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.cart)
        self.cashier_widget.total_label.setText(f"Rp {total:,.2f}")
        
    def handle_payment(self):
        if not self.cart:
            QMessageBox.warning(self, "Warning", "Keranjang belanja masih kosong")
            return
            
        total = sum(item['price'] * item['quantity'] for item in self.cart)
        method = "tunai" if self.cashier_widget.radio_tunai.isChecked() else "Qris"
        
        success, msg = database.save_order(self.current_user, total, method, self.cart)
        if success:
            QMessageBox.information(self, "Success", "Payment Sukses")
            self.display_summary(total, method)
            self.cart.clear()
            self.cashier_widget.table.setRowCount(0)
            self.update_total()
        else:
            QMessageBox.critical(self, "Error", f"Payment Gagal: {msg}")

    def go_to_history(self):
        self.history_widget.username_label.setText(self.current_user)
        self.load_history()
        self.stacked_widget.setCurrentWidget(self.history_widget)
        
    def load_history(self):
        self.history_widget.table.setRowCount(0)
        orders = database.get_orders()
        
        for order in orders:
            row = self.history_widget.table.rowCount()
            self.history_widget.table.insertRow(row)
            self.history_widget.table.setItem(row, 0, QTableWidgetItem(str(order['id'])))
            self.history_widget.table.setItem(row, 1, QTableWidgetItem(order['username']))
            self.history_widget.table.setItem(row, 2, QTableWidgetItem(order['date']))
            self.history_widget.table.setItem(row, 3, QTableWidgetItem(f"Rp {order['total_amount']:,.2f}"))
            items_str = ", ".join([f"{i['quantity']}x {i['name']}" for i in order['items']])
            self.history_widget.table.setItem(row, 4, QTableWidgetItem(items_str))
        
    def display_summary(self, total, method):
        from datetime import datetime
        self.summary_widget.username_label.setText(self.current_user)
        self.summary_widget.table.setRowCount(0)
        
        for item in self.cart:
            row = self.summary_widget.table.rowCount()
            self.summary_widget.table.insertRow(row)
            self.summary_widget.table.setItem(row, 0, QTableWidgetItem(item['name']))
            self.summary_widget.table.setItem(row, 1, QTableWidgetItem(f"Rp {item['price']:,.2f}"))
            self.summary_widget.table.setItem(row, 2, QTableWidgetItem(str(item['quantity'])))
            
        self.summary_widget.method_val.setText(method)
        self.summary_widget.total_val.setText(f"Rp {total:,.2f}")
        self.summary_widget.date_val.setText(datetime.now().strftime("%d - %m - %Y"))
        
        self.stacked_widget.setCurrentWidget(self.summary_widget)

if __name__ == "__main__":
    print("init Database...")
    database.init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())