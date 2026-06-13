import sqlite3
import hashlib

DB_NAME = "kasir.sqlite"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            total_amount REAL NOT NULL,
            payment_method TEXT NOT NULL,
            status TEXT NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(order_id) REFERENCES orders(id)
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                       (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True, "User created successfully"
    except sqlite3.IntegrityError:
        return False, "Username already exists"
    except Exception as e:
        return False, str(e)

def verify_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        stored_password = result[0]
        if stored_password == hash_password(password):
            return True, "Login successful"
        else:
            return False, "Invalid password"
    else:
        return False, "User not found"

def save_order(username, total_amount, payment_method, items):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO orders (username, total_amount, payment_method, status)
            VALUES (?, ?, ?, 'Terbayar')
        ''', (username, total_amount, payment_method))
        order_id = cursor.lastrowid
        
        for item in items:
            cursor.execute('''
                INSERT INTO order_items (order_id, item_name, price, quantity)
                VALUES (?, ?, ?, ?)
            ''', (order_id, item['name'], item['price'], item['quantity']))
            
        conn.commit()
        return True, "Order saved successfully"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()

def get_orders(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, total_amount, payment_method, status, date(order_date) 
        FROM orders WHERE username = ? ORDER BY id DESC
    ''', (username,))
    orders = cursor.fetchall()
    
    result = []
    for order in orders:
        order_id = order[0]
        cursor.execute('''
            SELECT item_name, price, quantity FROM order_items WHERE order_id = ?
        ''', (order_id,))
        items = cursor.fetchall()
        result.append({
            'id': order_id,
            'total_amount': order[1],
            'payment_method': order[2],
            'status': order[3],
            'date': order[4],
            'items': [{'name': i[0], 'price': i[1], 'quantity': i[2]} for i in items]
        })
    conn.close()
    return result

