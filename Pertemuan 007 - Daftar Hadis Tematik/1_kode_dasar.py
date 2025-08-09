# 1_kode_dasar.py
# Pertemuan 007 - Daftar Hadis Tematik
# Versi dasar: Menampilkan hadis berdasarkan tema dari data statis

hadis_tematik = {
    "Akhlak": [
        "Sesungguhnya orang mukmin yang paling sempurna imannya adalah yang paling baik akhlaknya. (HR. Tirmidzi)",
    ],
    "Ilmu": [
        "Menuntut ilmu itu wajib bagi setiap muslim. (HR. Ibnu Majah)",
    ],
    "Shalat": [
        "Shalat adalah tiang agama, barangsiapa mendirikannya maka ia menegakkan agama. (HR. Baihaqi)",
    ]
}

print("=== Daftar Tema Hadis ===")
for tema in hadis_tematik:
    print(f"- {tema}")

tema_input = input("Pilih tema: ").strip().title()

if tema_input in hadis_tematik:
    print(f"\nHadis tentang {tema_input}:")
    for hadis in hadis_tematik[tema_input]:
        print(f"- {hadis}")
else:
    print("Tema tidak ditemukan.")
