import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from ui.login_ui import LoginWidget
from ui.signup_ui import SignupWidget
from ui.cashier_ui import CashierWidget
from ui.history_ui import HistoryWidget
from ui.summary_ui import SummaryWidget
from PyQt6.QtWidgets import QTableWidgetItem
import database
# MainWindow adalah kelas utama yang mengelola semua widget dan logika aplikasi. 
# Di dalamnya terdapat metode untuk menangani navigasi antar halaman, login, signup, penambahan 
# item ke keranjang
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UMS Cashier App")
        self.resize(1200, 800)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.current_user = None
        self.cart = []

        # Inisialisasi semua widget
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
        
        # Hubungkan sinyal dan slot untuk navigasi dan aksi
        self.login_widget.signup_link.clicked.connect(self.go_to_signup)
        self.signup_widget.login_link.clicked.connect(self.go_to_login)

        self.login_widget.login_button.clicked.connect(self.handle_login)
        self.signup_widget.signup_button.clicked.connect(self.handle_signup)
        
        self.cashier_widget.history_btn.clicked.connect(self.go_to_history)
        self.cashier_widget.add_btn.clicked.connect(self.add_item)
        self.cashier_widget.pay_btn.clicked.connect(self.handle_payment)
        
        self.history_widget.back_btn.clicked.connect(self.go_to_cashier)
        self.summary_widget.back_btn.clicked.connect(self.go_to_cashier)
# Metode untuk navigasi ke halaman signup dari halaman login, 
# termasuk reset pesan error jika ada pada halaman signup
    def go_to_signup(self):
        self.stacked_widget.setCurrentWidget(self.signup_widget)
        self.signup_widget.msg_label.setText("")

# Metode untuk kembali ke halaman login dari halaman signup, termasuk reset pesan error jika 
# ada pada halaman login
    def go_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_widget)
        self.login_widget.msg_label.setText("")

# Metode untuk menangani login, termasuk validasi input dan interaksi dengan database untuk memverifikasi kata sandi pengguna
    def handle_login(self):
        username = self.login_widget.username.text()
        password = self.login_widget.password.text()

# Validasi input untuk memastikan bahwa pengguna telah mengisi semua field yang diperlukan sebelum mencoba login
        if not username or not password:
            self.login_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.login_widget.msg_label.setText("Isi semua input yang diperlukan")
            return
# Interaksi dengan database untuk memverifikasi kata sandi pengguna. Jika login berhasil, 
# simpan username saat ini dan navigasi ke halaman kasir. Jika login gagal, tampilkan pesan error yang sesuai.
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
# Metode untuk menangani signup, termasuk validasi input dan interaksi dengan database untuk membuat akun baru
    def handle_signup(self):
        username = self.signup_widget.username.text()
        password = self.signup_widget.password.text()
        confirm_password = self.signup_widget.confirm_password.text()
# Validasi input untuk memastikan bahwa pengguna telah mengisi semua field yang diperlukan
        if not username or not password or not confirm_password:
            self.signup_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.signup_widget.msg_label.setText("Isi semua input yang diperlukan")
            return
# Validasi input untuk memastikan bahwa pengguna telah mengisi semua field yang diperlukan dan bahwa 
# password dan konfirmasi password cocok sebelum mencoba membuat akun baru
        if password != confirm_password:
            self.signup_widget.msg_label.setStyleSheet("color: red; font-size: 13px;")
            self.signup_widget.msg_label.setText("Password tidak cocok")
            return
# Interaksi dengan database untuk membuat akun baru. Jika pembuatan akun berhasil, 
# tampilkan pesan sukses dan navigasi ke halaman login. Jika gagal, tampilkan pesan error yang sesuai.
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
# Metode untuk navigasi ke halaman kasir dari halaman history atau summary, 
# termasuk set username saat ini pada label di halaman kasir
    def go_to_cashier(self):
        self.cashier_widget.username_label.setText(self.current_user)
        self.stacked_widget.setCurrentWidget(self.cashier_widget)
# Metode untuk menambahkan item ke keranjang belanja, termasuk validasi input dan update tampilan 
# tabel serta total harga
    def add_item(self):
        name = self.cashier_widget.nama_barang.text()
        harga_str = self.cashier_widget.harga_barang.text()
        qty_str = self.cashier_widget.quantity.text()
# Validasi input untuk memastikan bahwa pengguna telah mengisi semua field yang diperlukan 
# dan bahwa harga dan quantity memiliki format yang benar sebelum menambahkan item ke keranjang belanja
        if not name or not harga_str or not qty_str:
            QMessageBox.warning(self, "Warning", "Isi semua input yang diperlukan")
            return
        # Validasi input untuk memastikan bahwa harga dan quantity memiliki format yang benar sebelum menambahkan item ke keranjang belanja.
        try:
            harga = float(harga_str)
            qty = int(qty_str)
    # Jika harga atau quantity tidak memiliki format yang benar, tampilkan pesan error dan hentikan proses penambahan item ke keranjang belanja
        except ValueError:
            QMessageBox.warning(self, "Warning", "Harga harus berupa angka dan quantity harus berupa integer")
            return
    # Jika semua validasi input berhasil, hitung subtotal untuk item tersebut, tambahkan item ke keranjang belanja, update tampilan tabel dengan item baru, dan update total harga keseluruhan
        subtotal = harga * qty
        self.cart.append({'name': name, 'price': harga, 'quantity': qty})
    # Update tampilan tabel dengan item baru 
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
    # Metode untuk menghitung total harga keseluruhan dari semua item di keranjang belanja dan update label total harga di halaman kasir    
    def update_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.cart)
        self.cashier_widget.total_label.setText(f"Rp {total:,.2f}")
    # jika keranjang belanja kosong, tampilkan pesan peringatan.
    def handle_payment(self):
        if not self.cart:
            QMessageBox.warning(self, "Warning", "Keranjang belanja masih kosong")
            return
        # Hitung total harga keseluruhan dari semua item di keranjang belanja dan tentukan metode pembayaran berdasarkan pilihan pengguna. Kemudian, 
        # interaksi dengan database untuk menyimpan data transaksi. Jika penyimpanan berhasil, tampilkan pesan sukses, navigasi ke halaman summary, dan reset
        #  keranjang belanja serta tampilan tabel. Jika penyimpanan gagal, tampilkan pesan error yang sesuai.
        total = sum(item['price'] * item['quantity'] for item in self.cart)
        method = "tunai" if self.cashier_widget.radio_tunai.isChecked() else "Qris"
        # Interaksi dengan database untuk menyimpan data transaksi. Jika penyimpanan berhasil, tampilkan pesan sukses, navigasi ke halaman 
        # summary, dan reset keranjang belanja serta tampilan tabel. Jika penyimpanan gagal, tampilkan pesan error yang sesuai.
        success, msg = database.save_order(self.current_user, total, method, self.cart)
        if success:
            QMessageBox.information(self, "Success", "Payment Sukses")
            self.display_summary(total, method)
            self.cart.clear()
            self.cashier_widget.table.setRowCount(0)
            self.update_total()
        else:
            QMessageBox.critical(self, "Error", f"Payment Gagal: {msg}")
# Metode untuk navigasi ke halaman history dari halaman kasir, termasuk set username saat ini pada label di halaman history dan load data transaksi dari database untuk ditampilkan di tabel history
    def go_to_history(self):
        self.history_widget.username_label.setText(self.current_user)
        self.load_history()
        self.stacked_widget.setCurrentWidget(self.history_widget)
    # Metode untuk load data transaksi dari database dan menampilkannya di tabel history pada halaman history    
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
    # Metode untuk menampilkan ringkasan pembelian di halaman summary setelah pembayaran berhasil, termasuk set username saat ini pada label di halaman summary, 
    # update tabel dengan item yang dibeli, dan update detail pembayaran seperti metode pembayaran, total harga, dan tanggal pembelian    
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


# kode ini adalah entry point untuk aplikasi kasir. Di sini kita menginisialisasi database, 
# membuat instance dari QApplication, dan menampilkan MainWindow. MainWindow adalah kelas utama yang 
# mengelola semua widget dan logika aplikasi.
if __name__ == "__main__":
    print("init Database...")
    database.init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())