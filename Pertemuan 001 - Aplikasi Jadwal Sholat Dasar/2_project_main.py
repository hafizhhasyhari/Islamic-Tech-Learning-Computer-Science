# 2_project_main.py
# Pertemuan 001 - Aplikasi Jadwal Sholat Dasar
# Project utama: Menampilkan jadwal sholat dari API

import requests
from datetime import datetime

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

        print(f"=== Jadwal Sholat ({kota}, {today}) ===")
        print(f"Subuh   : {timings['Fajr']}")
        print(f"Dzuhur  : {timings['Dhuhr']}")
        print(f"Ashar   : {timings['Asr']}")
        print(f"Maghrib : {timings['Maghrib']}")
        print(f"Isya    : {timings['Isha']}")
    else:
        print("Gagal mengambil jadwal sholat. Periksa API.")

except requests.exceptions.RequestException as e:
    print("Terjadi kesalahan saat menghubungi API:", e)
