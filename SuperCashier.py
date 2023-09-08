#!/usr/bin/env python
# coding: utf-8


import random
from datetime import datetime
from tabulate import tabulate
import numpy as np



def validate_name(name):
    """Validasi nama item, nama item harus berupa string"""
    if not isinstance(name, str):
        raise ValueError("nama item harus string")
    
def validate_qty(qty):
    """validasi kuantitas item, harus lebih besar dari 0"""
    if not isinstance(qty, (int, float)) or qty <= 0:
        raise ValueError("Kuantitas item harus lebih besar daripada 0")
    
def validate_price(price):
    """validasi harga, harga tidak boleh minus"""
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Harga item tidak boleh negatif")



class Transaction:
    """Sebuah kelas untuk mewakili transaksi pelanggan."""
    
    def __init__(self):
        """Inisialisasi objek Transaksi baru."""
        self.transaction_id = f"TRX-{random.randint(1000, 9999)}"
        self.transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.items = {}

    def add_item(self, item_details):
        """Add an item to the transaction."""
        try:
            name, qty, price = item_details
            validate_name(name)
            validate_qty(qty)
            validate_price(price)
            self.items[name] = {'quantity': qty, 'price': price}
        except ValueError as e:
            print(f"Kesalahan saat menambahkan item: {e}")

    def update_item_name(self, old_name, new_name):
        """Perbarui nama item dalam transaksi."""
        try:
            validate_name(new_name)
            if old_name in self.items:
                self.items[new_name] = self.items.pop(old_name)
            else:
                raise ValueError("Item tidak ditemukan dalam transaksi")
        except ValueError as e:
            print(f"Kesalahan saat memperbarui nama item: {e}")

    def update_item_qty(self, name, new_qty):
        """Perbarui kuantitas item dalam transaksi."""
        try:
            validate_qty(new_qty)
            if name in self.items:
                self.items[name]['quantity'] = new_qty
            else:
                raise ValueError("Item tidak ditemukan dalam transaksi")
        except ValueError as e:
            print(f"Kesalahan saat memperbarui kuantitas item: {e}")

    def update_item_price(self, name, new_price):
        """Perbarui harga item dalam transaksi."""
        try:
            validate_price(new_price)
            if name in self.items:
                self.items[name]['price'] = new_price
            else:
                raise ValueError("Item tidak ditemukan dalam transaksi")
        except ValueError as e:
            print(f"Kesalahan saat memperbarui harga item: {e}")

    def delete_item(self, name):
        """Hapus item dari transaksi."""
        try:
            validate_name(name)
            if name in self.items:
                del self.items[name]
            else:
                raise ValueError("Item tidak ditemukan dalam transaksi")
        except ValueError as e:
            print(f"Kesalahan saat menghapus item: {e}")

    def reset_transaction(self):
        """Reset transaksi dengan menghapus semua item."""
        self.items.clear()

    def check_order(self):
        """Periksa pesanan untuk melihat apakah valid."""
        try:
            if all(self.items[item].get('quantity') and self.items[item].get('price') for item in self.items):
                print("Pesanan sudah benar")
                total, discounted_price, discount_percentage = self.total_price()
                discount_amount = total - discounted_price
                table_data = []
                for item_name, details in self.items.items():
                    item_total_price = details['quantity'] * details['price']
                    table_data.append(["", "", item_name, details['quantity'], details['price'], item_total_price, "", "", ""])
                table_data.append([self.transaction_id, self.transaction_date, "Total", "", "", total, discount_amount, discounted_price, f"{persentase_diskon}%"])
                print(tabulate(table_data, headers=['ID Transaksi', 'Tanggal Transaksi', 'Item', 'Kuantitas', 'Harga', 'Total Harga', 'Jumlah Diskon', 'Harga Diskon', 'Diskon %']))
            else:
                raise ValueError("Ada kesalahan dalam data masukan")
        except ValueError as e:
            print(f"Kesalahan saat memeriksa pesanan: {e}")

    def total_price(self):
        """Hitung harga total transaksi, termasuk diskon yang berlaku."""
        try:
            total = np.sum([details['price'] * details['quantity'] for details in self.items.values()])
            discount_percentage = 0
            if total > 500000:
                discount_percentage = 10
            elif total > 300000:
                discount_percentage = 8
            elif total > 200000:
                discount_percentage = 5

            discounted_price = total * ((100 - discount_percentage) / 100)
            return total, discounted_price, discount_percentage
        except Exception as e:
            print(f"Kesalahan saat menghitung harga total: {e}")


def create_invoice(transaction):
    print("Membuat faktur...")
    border = "*" * 50
    header = """
    ___   _   _   ___   _   _   ___   _   _   _   _  
   / _ \ | | | | / _ \ | \ | | / _ \ | | | | | \ | | 
  | | | || | | || | | ||  \| || | | || | | ||  \| | 
  | | | || |_| || | | || |\  || | | || |_| || |\  | 
   \___/  \___/  \___/ |_| \_| \___/  \___/ |_| \_|
    """
    
    # Dapatkan detail transaksi dalam bentuk tabel
    total, discounted_price, discount_percentage = transaction.total_price()
    discount_amount = total - discounted_price
    table_data = []
    for item_name, details in transaction.items.items():
        item_total_price = details['quantity'] * details['price']
        table_data.append([item_name, details['quantity'], details['price'], item_total_price])
    table_data.append(["", "", "", ""])
    table_data.append(["Total", "", "", total])
    table_data.append(["Jumlah Diskon", "", "", discount_amount])
    table_data.append(["Harga Diskon", "", "", discounted_price])
    table_data.append(["Persentase Diskon", "", "", f"{persentase_diskon}%"])
    table_string = tabulate(table_data, headers=['Item', 'Kuantitas', 'Harga', 'Total Harga'], tablefmt='plain')
    
    # Menggabungkan semua elemen untuk membuat invoice
    invoice = f"{border}\n{header}\nID Transaksi: {transaction.transaction_id}\nTanggal Transaksi: {transaction.transaction_date}\n{border}\n{table_string}\n{border}"
    
    # Mencetak invoice
    print(invoice)
    print("Faktur dibuat.")
# menampilkan menu
def display_menu():
    print("""
    +-----------------------------------+
    |          BARATIE STORE            |
    +-----------------------------------+
    |                                   |
    | 1. Add Item                       |
    | 2. Update Item                    |
    | 3. Delete Item                    |
    | 4. Reset Transaction              |
    | 5. Check Order                    |
    | 6. End Transaction and Invoice    |
    |                                   |
    |                                   |
    +-----------------------------------+
    """)
# Menginisialisasi transaksi baru
trnsct_123 = Transaction()

# Loop untuk memungkinkan pengguna menambahkan item secara manual
while True:
    display_menu()
    # Meminta masukan dari pengguna
    action = input("""
    Pilih lah dari angka 1-6 : """).strip()
    print(" ")
    if action == '1':
        # Mendapatkan detail item dari pengguna
        item_name = input("Masukkan nama item: ").strip().lower().capitalize()
        item_qty = int(input("Masukkan kuantitas item: ").strip())
        item_price = float(input("Masukkan harga item: ").strip())
        
        # Menambahkan item ke transaksi
        trnsct_123.add_item([item_name, item_qty, item_price])
    elif action == '2':
        # Mendapatkan detail item yang akan diperbarui
        item_name = input("Masukkan nama item yang akan diperbarui: ").strip()
        update_type = input("""
        What would you like to update?
        1 - Name
        2 - Kuantitas
        3 - Harga
        Your choice: """).strip()
        
        if update_type == '1':
            new_name = input("Masukkan nama baru: ").strip().lower().capitalize()
            trnsct_123.update_item_name(item_name, new_name)
        elif update_type == '2':
            new_qty = int(input("Masukkan kuantitas baru: ").strip())
            trnsct_123.update_item_qty(item_name, new_qty)
        elif update_type == '3':
            new_price = float(input("Masukkan harga baru: ").strip())
            trnsct_123.update_item_price(item_name, new_price)
    elif action == '3':
        # Mendapatkan nama item yang akan dihapus
        item_name = input("Masukkan nama item yang akan dihapus: ").strip().lower().capitalize()
        trnsct_123.delete_item(item_name)
    elif action == '4':
        # Mereset transaksi
        trnsct_123.reset_transaction()
    elif action == '5':
        # Memeriksa pesanan
        trnsct_123.check_order()
    elif action == '6':
        # Mengakhiri transaksi dan mencetak faktur
        print("Transaksi berakhir. Berikut adalah faktur Anda:")
        trnsct_123.check_order()
        print(" ")
        create_invoice(trnsct_123)
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")



