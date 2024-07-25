# PostgresSQL Manager
Modul sederhana untuk memudahkan pengguna melakukan CRUD dalam database melalui python. Modul ini tidak sepenuhnya dapat melakukan semua CRUD di semua kondisi dalam PostgreSQL, karena keterbatasan pengetahuan dan keterampilan creator masih banyak terdapat celah dan batasan yang memuat modul sering tidak berjalan seperti semestinya.

**DISCLAIMER!**
Modul ini tidak diperuntukkan untuk penggunaan sehari-hari atau bahkan dalam project. Harap gunakan modul hanya untuk memenuhi rasa penasaran, mencoba atau ingin mengetahui cara kerja modul.

**NOTE:**
Creator merasa sangat terbuka dan senang apabila ada yang menyempurnakan atau mengembangkan modul ini dalam repo mereka. Mohon kabari creator apabila ada yang telah mengembangkan modul. Mohon maaf apabila dalam modul ini teradapat banyak kekurangan, Terimakasih :D

## 1.0 Batasan
- Nama column primary key dan foreign key harus sama
- Pengisian `values` pada list harus sesuai dengan urutan column pada tabel

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
- `version_pgsql()`: Mengecek versi dari PostgreSQL yang digunakan
- `connect()`: Menyambungkan database degan python secara manual
- `close()`: Menutup connection dari database
- `get_columnname()`: Mengembalikan nilai nama kolom dari sebuah tabel
