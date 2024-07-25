# PostgresSQL Manager
Modul sederhana untuk memudahkan pengguna melakukan CRUD dalam database melalui python. Modul ini tidak sepenuhnya dapat melakukan semua CRUD di semua kondisi dalam PostgreSQL, karena keterbatasan pengetahuan dan keterampilan creator masih banyak terdapat celah dan batasan yang memuat modul sering tidak berjalan seperti semestinya. **Modul ini memungkinkan pengguna untuk melakukan operasi CRUD hanya dengan memanggil function dan memasukkan nama tabel serta argumen yang dibutuhkan saja tanpa menulis query masing-masing.**

**DISCLAIMER!**<br>
Modul ini tidak diperuntukkan untuk penggunaan sehari-hari atau bahkan dalam project. Harap gunakan modul hanya untuk memenuhi rasa penasaran, mencoba atau ingin mengetahui cara kerja modul.

**NOTE:**<br>
Creator merasa sangat terbuka dan senang apabila ada yang menyempurnakan atau mengembangkan modul ini dalam repo mereka. Mohon kabari creator apabila ada yang telah mengembangkan modul. Mohon maaf apabila dalam modul ini teradapat banyak kekurangan, saya hanya mencoba mengimplementasikan apa yang saya dapat diperkuliahan. Terimakasih :D

## 1.0 Batasan
- Nama column primary key dan foreign key harus sama.
- Pengisian `values` pada list harus sesuai dengan urutan column pada tabel.
- Function `read_data` belum bisa menampilkan `GROUP BY` dan `HAVING`.
- Pada Function `read_data` argumen `JOIN` belum dapat digunakan bersama dengan `WHERE` dan `ORDER BY`
- Function `delete_data` belum bisa digunakan untuk menghapus data yang memiliki Foreign Key

## 2.0 Pemakaian Modul
1. Install Python melalui microsoft store (windows) atau website official [python](https://www.python.org/downloads/)

2. Install psycopg2
```sh
pip install psycopg2
```
3. copy repository pgsqlmanager atau unduh file `dbmanager.py`
```sh
git clone https://github.com/oujirate/pgsqlmanager.git
```
4. Jalankan `dbmanager.py` sebagai modul pada file python anda
```python
from pgsqlmanager import dbmanager.py
```
5. Buat instance yang pada class `dbmanager` yang berisi host, port, username, password, dbname sesuai dengan PostgreSQL kalian. 
```python
db = dbmanager(host='localhost',port='5432',username='postgres',password='admin123',dbname='mydatabase')
```
Kita bisa mengecek koneksi dengan function `version_pgsql`
```python
db.version_pgsql()
```
Apabila keluar output versi dari PostgreSQL, maka berhasil terhubung dengan database.

## 3.0 Dokumentasi Function
- `version_pgsql()` : Mengecek versi dari PostgreSQL yang digunakan.
- `connect()` : Menyambungkan database degan python secara manual.
- `close()` : Menutup connection dari database.
- `get_columnname()` : Mengembalikan nilai nama kolom dari sebuah tabel.
  - `table=` : nama tabel (string).
  - `idenable=` : memberikan opsi untuk mengambil kolom id (True/False).
- `getall_tablename()` : Mengembalikan nilai semua nama tabel yang ada pada database yang bersifat publik.
- `auth_columntable()` : Mengecek apakah suatu kolom terdapat dalam tabel atau tidak, mengembalikan nilai boolean.
  - `table=` : nama tabel.
  - `column=` : nama kolom.
- `create_data()` : Membuat data baru dari tabel dengan memasukkan values.
  - `table=` : nama tabel.
  - `values=` : list dari nilai-nilai yang ingin dimasukkan pada database (Pastikan jumlah dan urutan dari values sama dengan kolom database)
- `read_data()` : mengembalikan nilai dari data yang diambi dari database.
  - `select=` : memilih kolom yang ingin ditampilkan (string), default=*.
  - `table=` : nama tabel.
  - `join=`  : menggabungkan dua atau lebih tabel menggunakan foreign key.
  - `where=` : filter data.
  - `orderby=` : mengurutkan data berdasarkan argumen.
- `update_data()` : memperbaharui data kolom pada database.
  - `table=` : nama tabel.
  - `idcolumn=` : id kolom yang ingin diperbaharui.
  - `values=` : nilai baru dari id kolom. (Pastikan jumlah dan urutan dari values sama dengan kolom database)
- `delete_data()` : menghapus kolom dari suatu tabel.
  - `table=` : nama tabel.
  - `id_column=` : id kolom yang akan dihapus.
 
## Build-In
- Windows 10 Pro 64-Bit 10.0.19045 Build 19045
- PostgreSQL 8.2
- Visual Studio Code 1.19.1
- Python 3.12.2

## About
"Seorang mahasiswa baru saja telah mempelajari Sistem Basis Data yang diimplementasikan melalui bahasa pemrograman Python. Ia merasa jika ingin melakukan operasi seperti CRUD pada database perlu menulis query secara manual dan berulang pada python. Lantas ia berfikir 'Mengapa aku tidak membuat template agar tidak mengulang kode dan bisa dipakai secara general?'. Dari situlah dirinya mencoba untuk membuat modul demi memudahkannya dan teamnya dalam project akhir semester."<br>
**Juni 2024**
