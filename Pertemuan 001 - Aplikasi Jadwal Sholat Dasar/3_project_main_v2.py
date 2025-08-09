# 3_project_main_v2.py
# Pertemuan 001 - Aplikasi Jadwal Sholat Dasar
# Versi 2: Menampilkan jadwal sholat dalam bentuk tabel rapi

import requests
from datetime import datetime
from tabulate import tabulate  # pip install tabulate

# Lokasi
kota = "Jakarta"
negara = "Indonesia"

# Tanggal hari ini
today = datetime.now().strftime("%d-%m-%Y")

# URL API Aladhan
url = f"http://api.aladhan.com/v1/timingsByCity?city={kota}&country={negara}&method=2"

try:
    # Ambil data dari API
    response = requests.get(url)
    data = response.json()

    if data["code"] == 200:
        timings = data["data"]["timings"]

        # Data untuk tabel
        jadwal_tabel = [
            ["Subuh", timings['Fajr']],
            ["Dzuhur", timings['Dhuhr']],
            ["Ashar", timings['Asr']],
            ["Maghrib", timings['Maghrib']],
            ["Isya", timings['Isha']]
        ]

        print(f"=== Jadwal Sholat ({kota}, {today}) ===")
        print(tabulate(jadwal_tabel, headers=["Sholat", "Waktu"], tablefmt="fancy_grid"))
    else:
        print("Gagal mengambil jadwal sholat. Periksa API.")

except requests.exceptions.RequestException as e:
    print("Terjadi kesalahan saat menghubungi API:", e)
