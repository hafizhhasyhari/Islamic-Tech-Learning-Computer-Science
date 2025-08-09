# 1_kode_dasar.py
# Pertemuan 001 - Aplikasi Jadwal Sholat Dasar
# Versi dasar: Menampilkan jadwal sholat secara statis

# Jadwal sholat manual untuk kota Jakarta (contoh)
jadwal_sholat = {
    "Subuh": "04:37",
    "Dzuhur": "11:58",
    "Ashar": "15:21",
    "Maghrib": "17:54",
    "Isya": "19:07"
}

print("=== Jadwal Sholat Hari Ini (Jakarta) ===")
for nama_sholat, waktu in jadwal_sholat.items():
    print(f"{nama_sholat}: {waktu}")
