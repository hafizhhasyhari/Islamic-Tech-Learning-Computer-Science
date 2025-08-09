# 5_kode_khusus.py
# Pertemuan 007 - Daftar Hadis Tematik
# Kode khusus: filter otomatis hadis ke dalam tema berdasarkan kata kunci
# Oleh : Hafizh Kartunis @hafizhhasyhari
# Circle : Scrivener's Presenter Asia
# Year : 2023

import requests
from tabulate import tabulate

API_KEY = "MASUKKAN_API_KEY_ANDA"  # Daftar di https://api.sunnah.com/
BASE_URL = "https://api.sunnah.com/v1"

# Pemetaan kata kunci -> tema
tema_keywords = {
    "Akhlak": ["jujur", "amanah", "akhlak", "sopan", "baik"],
    "Ilmu": ["ilmu", "belajar", "menuntut", "mengajar"],
    "Shalat": ["shalat", "sholat", "salat", "sujud", "ruku"],
}

def detect_theme(text):
    """Mendeteksi tema dari teks hadis"""
    for tema, keywords in tema_keywords.items():
        for kw in keywords:
            if kw.lower() in text.lower():
                return tema
    return "Lainnya"

def get_hadiths(collection, limit=10):
    """Mengambil beberapa hadis dari koleksi"""
    headers = {"X-API-Key": API_KEY}
    url = f"{BASE_URL}/collections/{collection}/hadiths"
    params = {"page": 1, "limit": limit}
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            hasil = []
            for h in data['data']:
                teks = h['body'].replace("\n", " ").strip()
                tema = detect_theme(teks)
                hasil.append([h['hadithNumber'], tema, teks])
            return hasil
        else:
            print("[ERROR] Gagal mengambil data:", response.status_code)
            return []
    except Exception as e:
        print("[ERROR]", str(e))
        return []

def main():
    print("=== Filter Hadis ke Tema Otomatis ===")
    print("Contoh koleksi: bukhari, muslim, tirmidhi, ibnmajah")
    collection = input("Masukkan koleksi hadis: ").strip().lower()

    hasil = get_hadiths(collection)
    if hasil:
        print(tabulate(hasil, headers=["No", "Tema", "Teks Hadis"], tablefmt="fancy_grid"))
    else:
        print("Tidak ada data hadis ditemukan.")

if __name__ == "__main__":
    main()
