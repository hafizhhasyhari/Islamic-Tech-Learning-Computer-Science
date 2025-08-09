# 📚 Pertemuan 007 – Daftar Hadis Tematik

## 🎯 Tujuan Pembelajaran
- Mahasiswa memahami pentingnya hadis sebagai sumber ajaran Islam.
- Mahasiswa dapat mengelompokkan hadis berdasarkan tema.
- Mahasiswa mampu membuat program pencarian hadis sesuai tema.

## 📝 Ringkasan
Pada pertemuan ini, kita mempelajari bagaimana mengakses, menampilkan, dan mengelompokkan hadis berdasarkan tema tertentu.  
Sumber data diambil dari **API Sunnah.com** sehingga hasil yang ditampilkan **real-time** dan valid.  

## 📂 Daftar Kode Program

| No | Nama File | Deskripsi |
|----|-----------|-----------|
| 1  | **1_kode_dasar.py** | Contoh kode paling sederhana untuk mengambil dan menampilkan 1 hadis. Cocok untuk memahami struktur data API. |
| 2  | **2_project_main.py** | Program utama untuk mengambil daftar hadis tematik dari API berdasarkan pilihan pengguna. |
| 3  | **3_project_main_v2.py** | Versi tabel rapi dari project utama, menggunakan library `tabulate` agar hasil mudah dibaca. |
| 4  | **4_pengembangan_umum.py** | Pengembangan umum: pencarian hadis berdasarkan kata kunci bebas, tidak terbatas tema. |
| 5  | **5_kode_khusus.py** | Kode khusus: otomatis mendeteksi tema hadis berdasarkan kata kunci yang telah dipetakan. |
| 6  | **6_eksperimental.py** | Eksperimen: pencarian multi-tema sekaligus dengan penilaian skor relevansi sederhana. |

## ⚙️ Instalasi & Menjalankan Program

1. **Clone repository**
   ```bash
   git clone https://github.com/username/nama-repo.git
   cd nama-repo/pertemuan_007
   ```
2. Buat virtual environment (opsional, tapi disarankan)
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies
pip install -r requirements.txt

4. Siapkan API Key
   ```bash
- Daftar di Sunnah.com API untuk mendapatkan API key.
- Masukkan API key ke variabel API_KEY di setiap file Python.
   ```
5. Jalankan program
📦 Dependencies
   ```bash
   requests – untuk mengambil data dari API.
   tabulate – untuk menampilkan data dalam bentuk tabel.
   ```
Instal dengan:
   ```bash
   pip install requests tabulate
   ```
📌 Catatan
API Sunnah.com memiliki batasan jumlah request per hari. Gunakan secara bijak.

Tema dan kata kunci dapat disesuaikan di 5_kode_khusus.py dan 6_eksperimental.py.
