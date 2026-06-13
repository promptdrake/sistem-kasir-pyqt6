# 🛒 UMS Cashier
Aplikasi kasir desktop berbasis **Python**, **PyQt6**, dan **SQLite** yang dirancang untuk membantu pencatatan transaksi penjualan secara mudah, cepat, dan efisien.

---
## Demo Account
- Username: ``demo``
- Password: ``demo``

## Fitur

* Login dan Registrasi
* Input Data Transaksi
* Perhitungan Total Otomatis
* Riwayat Transaksi
* Ringkasan Pembelian
* Hashing Password Dengan SHA-256

---

## Mockup Aplikasi

### Halaman Login

![Login](https://files.catbox.moe/sqpj5a.png)

### Halaman Registrasi

![Registrasi](https://files.catbox.moe/88drwq.png)

### Input Data Transaksi

![Input Data](https://files.catbox.moe/ohv7eg.png)

### Riwayat Transaksi

![Riwayat](https://files.catbox.moe/4pimrn.png)

### Ringkasan Pembelian

![Ringkasan](https://files.catbox.moe/v1y5jb.png)

---

## 📂 Struktur Proyek

```text
sistem-kasir-pyqt6/
│
├── main.py
├── database.py
├── kasir.sqlite
├── requirements.txt
│
└── ui/
    ├── login_ui.py
    ├── signup_ui.py
    ├── cashier_ui.py
    ├── history_ui.py
    └── summary_ui.py
```

---

## Cara Menjalankan / Develop

### 1. Clone Repository

```bash
git clone https://github.com/promptdrake/sistem-kasir-pyqt6.git
cd sistem-kasir-pyqt6
```

### 2. Install Dependency

```bash
pip install PyQt6
```

### 3. Jalankan Aplikasi

```bash
python main.py
```


---
