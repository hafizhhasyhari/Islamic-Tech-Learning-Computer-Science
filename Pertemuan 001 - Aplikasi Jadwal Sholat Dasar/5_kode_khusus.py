# 5_kode_khusus.py
# Pertemuan 001 - Aplikasi Jadwal Sholat Dasar
# Kode khusus: Menambahkan fitur hitung waktu menuju sholat berikutnya

import requests
from datetime import datetime, timedelta
from tabulate import tabulate  # pip install tabulate

# Lokasi default
kota = "Jakarta"
negara = "Indonesia"

# Tanggal hari ini
today = datetime.now().strftime("%d-%m-%Y")

# URL API Aladhan
url = f"http://api.aladhan.com/v1/timingsByCity?city={kota}&country={negara}&method=2"

def waktu_menuju_sholat(timings):
    sekarang = datetime.now()
    urutan_sholat = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

    for nama in urutan_sholat:
        waktu_str = timings[nama]
        waktu_sholat = datetime.strptime(waktu_str, "%H:%M").replace(
            year=sekarang.year, month=sekarang.month, day=sekarang.day
        )
        if waktu_sholat > sekarang:
            selisih = waktu_sholat - sekarang
            jam, sisa_detik = divmod(selisih.seconds, 3600)
            menit, _ = divmod(sisa_detik, 60)
            return nama, f"{jam} jam {menit} menit lagi"

    # Jika semua sudah lewat, sholat berikutnya adalah Subuh besok
    waktu_subuh_besok = datetime.strptime(timings["Fajr"], "%H:%M") + timedelta(days=1)
    selisih = waktu_subuh_besok - sekarang
    jam, sisa_detik = divmod(selisih.seconds, 3600)
    menit, _ = divmod(sisa_detik, 60)
    return "Fajr", f"{jam} jam {menit} menit lagi (besok)"

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

        # Hitung waktu menuju sholat berikutnya
        nama_next, countdown = waktu_menuju_sholat(timings)
        print(f"\n⏳ Sholat berikutnya: {nama_next} dalam {countdown}")
    else:
        print("Gagal mengambil jadwal sholat. Periksa API.")

except requests.exceptions.RequestException as e:
    print("Terjadi kesalahan saat menghubungi API:", e)
