# Pertemuan 006 - Audio Al-Qur'an Player
# Versi utama: menampilkan daftar surat dan memutar audio dari internet

import os
import requests
from playsound import playsound

# Daftar contoh surat (ID dan Nama)
surat_list = {
    1: "Al-Fatihah",
    112: "Al-Ikhlas",
    113: "Al-Falaq",
    114: "An-Nas"
}

def tampilkan_menu():
    print("=== 🎧 Audio Al-Qur'an Player ===")
    for nomor, nama in surat_list.items():
        print(f"{nomor}. {nama}")
    print("0. Keluar")

def unduh_dan_putar_audio(surat_id):
    try:
        print(f"Mengunduh audio surat {surat_list[surat_id]}...")
        url = f"https://verses.quran.com/{surat_id}/ar.alafasy.mp3"  # contoh endpoint audio
        response = requests.get(url)

        if response.status_code == 200:
            file_path = f"surat_{surat_id}.mp3"
            with open(file_path, "wb") as file:
                file.write(response.content)
            print("Memutar audio...")
            playsound(file_path)
            os.remove(file_path)  # hapus file setelah diputar
        else:
            print("Gagal mengunduh audio. Periksa koneksi atau URL.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih nomor surat: ").strip()

        if pilihan == "0":
            print("Terima kasih telah menggunakan Audio Al-Qur'an Player.")
            break

        try:
            surat_id = int(pilihan)
            if surat_id in surat_list:
                unduh_dan_putar_audio(surat_id)
            else:
                print("Nomor surat tidak tersedia.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()

# By : Hafizh Kartunis @hafizhhasyhari
# Tahun : 2025
# Indonesia
