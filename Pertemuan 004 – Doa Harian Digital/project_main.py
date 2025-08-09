# Pertemuan 004 - Doa Harian Digital
# Versi utama: menampilkan doa harian sesuai pilihan

doa_harian = {
    "Bangun Tidur": {
        "Arab": "الْـحَمْدُ لِلّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ",
        "Latin": "Alhamdu lillahil-ladzi ahyana ba’da ma amatana wa ilaihin-nusyur",
        "Arti": "Segala puji bagi Allah yang telah menghidupkan kami setelah mematikan kami, dan kepada-Nya kami akan kembali."
    },
    "Sebelum Makan": {
        "Arab": "بِسْمِ اللَّهِ",
        "Latin": "Bismillah",
        "Arti": "Dengan menyebut nama Allah."
    },
    "Sesudah Makan": {
        "Arab": "الْـحَمْدُ لِلّهِ الَّذِي أَطْعَمَنَا وَسَقَانَا وَجَعَلَنَا مُسْلِمِينَ",
        "Latin": "Alhamdu lillahil-ladzi ath’amana wa saqana wa ja’alana muslimin",
        "Arti": "Segala puji bagi Allah yang telah memberi kami makan dan minum serta menjadikan kami sebagai seorang muslim."
    },
    "Masuk Rumah": {
        "Arab": "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى اللَّهِ رَبِّنَا تَوَكَّلْنَا",
        "Latin": "Bismillahi walajna, wa bismillahi kharajna, wa ‘alallahi rabbina tawakkalna",
        "Arti": "Dengan nama Allah kami masuk, dengan nama Allah kami keluar, dan kepada Allah Tuhan kami, kami bertawakal."
    }
}

def tampilkan_menu():
    print("=== 📖 Doa Harian Digital ===")
    for i, doa in enumerate(doa_harian.keys(), start=1):
        print(f"{i}. {doa}")
    print("0. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih doa (angka): ").strip()

        if pilihan == "0":
            print("Terima kasih telah menggunakan Doa Harian Digital.")
            break

        try:
            index = int(pilihan) - 1
            nama_doa = list(doa_harian.keys())[index]
            data = doa_harian[nama_doa]
            print("\n=== 📜 Doa Harian ===")
            print(f"Doa: {nama_doa}")
            print(f"Arab : {data['Arab']}")
            print(f"Latin: {data['Latin']}")
            print(f"Arti : {data['Arti']}\n")
        except (IndexError, ValueError):
            print("Pilihan tidak valid, silakan coba lagi.\n")

if __name__ == "__main__":
    main()
