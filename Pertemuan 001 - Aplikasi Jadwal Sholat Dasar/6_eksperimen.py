# 6_eksperimen.py
# Pertemuan 001 - Aplikasi Jadwal Sholat Dasar
# Eksperimen: Memutar suara adzan ketika waktu sholat tiba

import requests
from datetime import datetime, timedelta
from tabulate import tabulate
import time
import threading
import os
from playsound import playsound  # pip install playsound

# Lokasi default
kota = "Jakarta"
negara = "Indonesia"

# URL API Aladhan
url = f"http://api.aladhan.com/v1/timingsByCity?city={kota}&country={negara}&method=2"

# File audio adzan (pastikan file ini ada di folder project)
ADZAN_FILE = "adzan.mp3"

def ambil_jadwal():
    try:
        response = requests.get(url)
        data = response.json()
        if data["code"] == 200:
            return data["data"]["timings"]
        else:
            print("Gagal mengambil jadwal sholat.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def hitung_detik_menuju(waktu_str):
    sekarang = datetime.now()
    target = datetime.strptime(waktu_str, "%H:%M").replace(
        year=sekarang.year, month=sekarang.month, day=sekarang.day
    )
    if target < sekarang:
        target += timedelta(days=1)
    return int((target - sekarang).total_seconds())

def tunggu_dan_adzan(nama_sholat, waktu_str):
    detik = hitung_detik_menuju(waktu_str)
    print(f"⏳ Menunggu {nama_sholat} dalam {detik // 60} menit...")
    time.sleep(detik)
    print(f"🔊 Waktu {nama_sholat}! Memutar adzan...")
    if os.path.exists(ADZAN_FILE):
        playsound(ADZAN_FILE)
    else:
        print("[!] File adzan.mp3 tidak ditemukan.")

if __name__ == "__main__":
    timings = ambil_jadwal()
    if timings:
        today = datetime.now().strftime("%d-%m-%Y")
        jadwal_tabel = [
            ["Subuh", timings['Fajr']],
            ["Dzuhur", timings['Dhuhr']],
            ["Ashar", timings['Asr']],
            ["Maghrib", timings['Maghrib']],
            ["Isya", timings['Isha']]
        ]
        print(f"=== Jadwal Sholat ({kota}, {today}) ===")
        print(tabulate(jadwal_tabel, headers=["Sholat", "Waktu"], tablefmt="fancy_grid"))

        # Jalankan thread untuk setiap waktu sholat
        for nama, waktu in jadwal_tabel:
            threading.Thread(target=tunggu_dan_adzan, args=(nama, waktu)).start()
