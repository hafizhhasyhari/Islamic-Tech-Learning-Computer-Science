# 3_project_main_v2.py
# Pertemuan 007 - Daftar Hadis Tematik
# Versi tabel rapi: Menampilkan beberapa hadis dari API Sunnah.com

import requests
from tabulate import tabulate

API_KEY = "MASUKKAN_API_KEY_ANDA"  # Daftar di https://api.sunnah.com/ untuk dapat API key
BASE_URL = "https://api.sunnah.com/v1"

def get_hadiths(collection, start, end):
    """Mengambil beberapa hadis dari koleksi tertentu"""
    headers = {"X-API-Key": API_KEY}
    url = f"{BASE_URL}/collections/{collection}/hadiths"
    params = {"page": 1, "limit": end}  # Ambil lebih banyak lalu filter
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            hadith_list = []
            for h in data['data'][start-1:end]:
                hadith_list.append([
                    h['hadithNumber'],
                    h['body'].replace("\n", " ").strip()
                ])
            return hadith_list
        else:
            return []
    except Exception as e:
        print("[ERROR]", str(e))
        return []

def main():
    print("=== Daftar Hadis Tematik (Tabel Rapi) ===")
    tema_map = {
        "akhlak": ("bukhari", 1, 3),
        "ilmu": ("ibnmajah", 220, 222),
        "shalat": ("bukhari", 500, 502)
    }

    print("Tema tersedia:", ", ".join(tema_map.keys()))
    tema = input("Masukkan tema: ").strip().lower()

    if tema in tema_map:
        collection, start, end = tema_map[tema]
        hadiths = get_hadiths(collection, start, end)
        if hadiths:
            print(tabulate(hadiths, headers=["No", "Teks Hadis"], tablefmt="fancy_grid"))
        else:
            print("Tidak ada data hadis ditemukan.")
    else:
        print("Tema tidak ditemukan.")

if __name__ == "__main__":
    main()
