# 2_project_main.py
# Pertemuan 007 - Daftar Hadis Tematik
# Project utama: Mengambil data hadis tematik dari API Sunnah.com

import requests

API_KEY = "MASUKKAN_API_KEY_ANDA"  # Daftar di https://api.sunnah.com/ untuk dapat API key
BASE_URL = "https://api.sunnah.com/v1"

def get_hadith_by_collection(collection, number):
    """Mengambil hadis berdasarkan koleksi dan nomor hadis"""
    headers = {"X-API-Key": API_KEY}
    url = f"{BASE_URL}/collections/{collection}/hadiths/{number}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['hadith'][0]['body']
        else:
            return f"[ERROR] Gagal mengambil data: {response.status_code}"
    except Exception as e:
        return f"[ERROR] {str(e)}"

def main():
    print("=== Pencarian Hadis Tematik (Real-Time) ===")
    print("Tema tersedia: Akhlak, Ilmu, Shalat")
    tema = input("Masukkan tema: ").strip().lower()

    if tema == "akhlak":
        print(get_hadith_by_collection("bukhari", 8))
    elif tema == "ilmu":
        print(get_hadith_by_collection("ibnmajah", 224))
    elif tema == "shalat":
        print(get_hadith_by_collection("bukhari", 520))
    else:
        print("Tema tidak ditemukan.")

if __name__ == "__main__":
    main()
