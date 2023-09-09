![test_cashier drawio](https://github.com/arnanmm2/SuperCashier-Pacmann/assets/107466083/2e4456ff-595f-4747-8ffd-e06e22bda947)
# Supermarket Self-Service Cashier System

## Background

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis dengan menciptakan sistem kasir self-service di supermarket miliknya. Ini memungkinkan pelanggan untuk memasukkan item yang ingin dibeli, jumlah item, dan harga item secara langsung. Selain itu, sistem ini juga memungkinkan pelanggan yang tidak berada di kota tersebut untuk melakukan pembelian. Namun, Andi menghadapi masalah karena ia membutuhkan programmer untuk me...

## Requirements

1. Customer membuat ID transaksi dengan menciptakan objek dari kelas (contoh: `trnsct_123 = Transaction()`).
2. Customer memasukkan nama item, jumlah item, dan harga barang dengan metode `add_item([<nama item>, <jumlah item>, <harga item>])`.
3. Customer dapat memperbarui detail item jika terjadi kesalahan dalam input menggunakan metode:
   - `update_item_name(<nama item>, <nama item baru>)`
   - `update_item_qty(<nama item>, <jumlah item baru>)`
   - `update_item_price(<nama item>, <harga item baru>)`
4. Jika customer batal membeli, mereka dapat menghapus item atau mereset transaksi menggunakan metode:
   - `delete_item(<nama item>)`
   - `reset_transaction()`
5. Sebelum menyelesaikan transaksi, customer dapat memeriksa pesanan mereka menggunakan metode `check_order()` yang mencetak detail transaksi dan pesan konfirmasi atau peringatan kesalahan.
6. Setelah memeriksa, customer dapat menghitung total belanja dengan metode `total_price()` yang juga menerapkan diskon berdasarkan total belanja.

## Modules

1. **random**: Digunakan untuk menghasilkan ID transaksi acak.
2. **datetime**: Digunakan untuk mendapatkan tanggal dan waktu transaksi saat ini.
3. **tabulate**: Digunakan untuk mencetak faktur dalam format tabel yang rapi.
4. **numpy**: Digunakan untuk operasi numerik (meskipun tampaknya tidak digunakan dalam kode ini).
## Flowchart
![test_cashier drawio](https://github.com/arnanmm2/SuperCashier-Pacmann/assets/107466083/3238103d-1ff3-40c9-b9ac-6bc7bf645d3b)

## Cara pakai
1. Pertama user membuka file Supercashier.py
2. Setelah program sudah di buka, akan terdapat petunjuk penggunaan.
3. User dapat memilih dari angka 1-6 untuk memilih fitur yang ada pada program ini
   
## Functions

### validate_name(name)
```python
def validate_name(name):
    # Validasi nama item, nama item harus berupa string
    if not isinstance(name, str):
        raise ValueError("nama item harus string")
```
Fungsi ini memvalidasi bahwa nama item yang dimasukkan adalah string. Jika tidak, ia akan memunculkan ValueError.

### validate_qty(qty)
```python
def validate_qty(qty):
    # validasi kuantitas item, harus lebih besar dari 0
    if not isinstance(qty, (int, float)) or qty <= 0:
        raise ValueError("Kuantitas item harus lebih besar daripada 0")
```
Fungsi ini memvalidasi bahwa kuantitas item yang dimasukkan adalah angka yang lebih besar dari 0. Jika tidak, ia akan memunculkan ValueError.

### validate_price(price)
```python
def validate_price(price):
    # validasi harga, harga tidak boleh minus
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Harga item tidak boleh negatif")
```
Fungsi ini memvalidasi bahwa harga item yang dimasukkan adalah angka non-negatif. Jika tidak, ia akan memunculkan ValueError.

## Class: Transaction

Kelas ini mengatur seluruh operasi yang berhubungan dengan transaksi individual.

```python
class Transaction:
    def __init__(self):
        self.transaction_id = f"TRX-{random.randint(1000, 9999)}"
        self.transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.items = {}
```

### __init__(self) - Requirement

Metode konstruktor ini menginisialisasi objek transaksi baru dengan ID transaksi acak dan tanggal transaksi saat ini, serta mendefinisikan dictionary kosong untuk menyimpan item-item yang akan dibeli.

### add_item(self, item_details) - Requirement

```python
def add_item(self, item_details):
    try:
        name, qty, price = item_details
        validate_name(name)
        validate_qty(qty)
        validate_price(price)
        self.items[name] = {'quantity': qty, 'price': price}
    except ValueError as e:
        print(f"Kesalahan saat menambahkan item: {e}")
```

Metode ini memungkinkan pelanggan untuk menambahkan item ke transaksi. Item-details harus berupa list yang berisi nama item (string), kuantitas (angka positif), dan harga (angka non-negatif). Jika terjadi kesalahan validasi, akan mencetak pesan kesalahan.

### update_item_name(self, old_name, new_name) - Requirement

```python
def update_item_name(self, old_name, new_name):
    try:
        validate_name(new_name)
        if old_name in self.items:
            self.items[new_name] = self.items.pop(old_name)
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat memperbarui nama item: {e}")
```

Metode ini memungkinkan pelanggan untuk memperbarui nama item dalam transaksi. Ia memvalidasi nama baru dan memeriksa apakah item lama ada dalam transaksi sebelum memperbaruinya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### update_item_qty(self, name, new_qty) - Requirement

```python
def update_item_qty(self, name, new_qty):
    try:
        validate_qty(new_qty)
        if name in self.items:
            self.items[name]['quantity'] = new_qty
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat memperbarui kuantitas item: {e}")
```

Metode ini memungkinkan pelanggan untuk memperbarui kuantitas item dalam transaksi. Ia memvalidasi kuantitas baru dan memeriksa apakah item ada dalam transaksi sebelum memperbaruinya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### update_item_price(self, name, new_price) - Requirement

```python
def update_item_price(self, name, new_price):
    try:
        validate_price(new_price)
        if name in self.items:
            self.items[name]['price'] = new_price
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat memperbarui harga item: {e}")
```

Metode ini memungkinkan pelanggan untuk memperbarui harga item dalam transaksi. Ia memvalidasi harga baru dan memeriksa apakah item ada dalam transaksi sebelum memperbaruinya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### delete_item(self, name) - Requirement

```python
def delete_item(self, name):
    try:
        validate_name(name)
        if name in self.items:
            del self.items[name]
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat menghapus item: {e}")
```

Metode ini memungkinkan pelanggan untuk menghapus item dari transaksi. Ia memvalidasi nama item dan memeriksa apakah item ada dalam transaksi sebelum menghapusnya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### reset_transaction(self) - Requirement

```python
def reset_transaction(self):
    self.items = {}
```

Metode ini mereset transaksi dengan menghapus semua item dari transaksi saat ini.

### check_order(self) - Requirement

```python
def check_order(self):
    if all(self.items[item].get('quantity', 0) > 0 and self.items[item].get('price', 0) > 0 for item in self.items):
        print("Pemesanan sudah benar")
    else:
        print("Terdapat kesalahan input data")
    print(tabulate([(name, details['quantity'], details['price']) for name, details in self.items.items()], headers=['Nama Item', 'Jumlah Item', 'Harga Item'], tablefmt='pretty'))
```

Metode ini memeriksa pesanan dengan memvalidasi kuantitas dan harga setiap item dalam transaksi. Jika semuanya benar, ia akan mencetak pesan konfirmasi; jika tidak, ia akan mencetak pesan kesalahan. Selain itu, ia juga mencetak detail transaksi dalam format tabel yang rapi.

### total_price(self) - Requirement

```python
def total_price(self):
    total = sum(details['quantity'] * details['price'] for details in self.items.values())
    if total > 500000:
        discount = 0.10
    elif total > 300000:
        discount = 0.08
    elif total > 200000:
        discount = 0.05
    else:
        discount = 0.0
    total_with_discount = total * (1 - discount)
    print(f"Total belanja: Rp. {total_with_discount:.2f}")
```

Metode ini menghitung total harga pesanan dengan menerapkan diskon berdasarkan total belanja. Diskon yang berlaku adalah: 10% untuk belanja di atas Rp 500.000, 8% untuk belanja di atas Rp 300.000, dan 5% untuk belanja di atas Rp 200.000.
