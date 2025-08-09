# 4_pengembangan_umum.py
# Pertemuan 001 - Aplikasi Jadwal Sholat Dasar
# Pengembangan umum: Menentukan kota & negara otomatis dari IP pengguna
# by : hafizhhasyhari
# Year : 2023
# Indonesia 

import requests
from datetime import datetime
from tabulate import tabulate  # pip install tabulate

# Fungsi untuk mendeteksi lokasi pengguna dari IP
def get_location_from_ip():
    try:
        ip_info = requests.get("https://ipapi.co/json/").json()
        return ip_info.get("city"), ip_info.get("country_name")
    except Exception:
        return None, None

# Dapatkan lokasi otomatis
kota, negara = get_location_from_ip()

if not kota or not negara:
    print("Gagal mendeteksi lokasi otomatis. Menggunakan lokasi default (Jakarta, Indonesia).")
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
