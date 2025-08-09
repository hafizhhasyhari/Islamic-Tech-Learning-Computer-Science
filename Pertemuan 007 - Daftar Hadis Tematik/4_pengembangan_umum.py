# 4_pengembangan_umum.py
# Pertemuan 007 - Daftar Hadis Tematik
# Pengembangan umum: pencarian hadis berdasarkan kata kunci bebas dari API Sunnah.com

import requests
from tabulate import tabulate

API_KEY = "MASUKKAN_API_KEY_ANDA"  # Daftar di https://api.sunnah.com/ untuk dapat API key
BASE_URL = "https://api.sunnah.com/v1"

def search_hadith(collection, keyword, limit=5):
    """Mencari hadis berdasarkan kata kunci di koleksi tertentu"""
    headers = {"X-API-Key": API_KEY}
    url = f"{BASE_URL}/collections/{collection}/hadiths"
    params = {"page": 1, "limit": 300}  # Ambil banyak, filter manual
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            filtered = []
            for h in data['data']:
                teks = h['body'].replace("\n", " ").strip()
                if keyword.lower() in teks.lower():
                    filtered.append([h['hadithNumber'], teks])
                if len(filtered) >= limit:
                    break
            return filtered
        else:
            print("[ERROR] Gagal mengambil data:", response.status_code)
            return []
    except Exception as e:
        print("[ERROR]", str(e))
        return []

def main():
    print("=== Pencarian Hadis Berdasarkan Kata Kunci ===")
    print("Contoh koleksi: bukhari, muslim, tirmidhi, ibnmajah")
    collection = input("Masukkan koleksi hadis: ").strip().lower()
    keyword = input("Masukkan kata kunci pencarian: ").strip()

    hasil = search_hadith(collection, keyword)
    if hasil:
        print(tabulate(hasil, headers=["No", "Teks Hadis"], tablefmt="fancy_grid"))
    else:
        print("Tidak ada hadis yang cocok dengan kata kunci tersebut.")

if __name__ == "__main__":
    main()
