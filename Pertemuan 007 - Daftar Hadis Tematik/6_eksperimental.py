# 6_eksperimental.py
# Pertemuan 007 - Daftar Hadis Tematik
# Eksperimental: pencarian multi-tema + skor relevansi

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

def relevance_score(text, keywords):
    """Hitung skor relevansi berdasarkan jumlah kata kunci yang cocok"""
    score = sum(1 for kw in keywords if kw.lower() in text.lower())
    return score

def detect_themes(text):
    """Mendeteksi semua tema yang relevan dengan skor"""
    detected = []
    for tema, keywords in tema_keywords.items():
        score = relevance_score(text, keywords)
        if score > 0:
            detected.append((tema, score))
    return sorted(detected, key=lambda x: x[1], reverse=True)

def get_hadiths(collection, limit=15):
    """Mengambil hadis dari API dan memberi penilaian multi-tema"""
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
                themes_with_scores = detect_themes(teks)
                tema_str = ", ".join([f"{t} ({s})" for t, s in themes_with_scores]) if themes_with_scores else "Lainnya"
                hasil.append([h['hadithNumber'], tema_str, teks])
            return hasil
        else:
            print("[ERROR] Gagal mengambil data:", response.status_code)
            return []
    except Exception as e:
        print("[ERROR]", str(e))
        return []

def main():
    print("=== Eksperimen: Multi-Tema + Skor Relevansi ===")
    print("Contoh koleksi: bukhari, muslim, tirmidhi, ibnmajah")
    collection = input("Masukkan koleksi hadis: ").strip().lower()

    hasil = get_hadiths(collection)
    if hasil:
        print(tabulate(hasil, headers=["No", "Tema (Skor)", "Teks Hadis"], tablefmt="fancy_grid"))
    else:
        print("Tidak ada data hadis ditemukan.")

if __name__ == "__main__":
    main()
