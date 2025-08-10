# Pertemuan 005 - Tafsir Ayat Tematik
# Versi utama: menampilkan ayat Al-Qur'an dan tafsir berdasarkan tema

ayat_tafsir = {
    "Sabar": {
        "Surat": "Al-Baqarah 2:153",
        "Ayat": "يَا أَيُّهَا الَّذِينَ آمَنُوا اسْتَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ",
        "Arti": "Wahai orang-orang yang beriman, mintalah pertolongan dengan sabar dan shalat; sesungguhnya Allah beserta orang-orang yang sabar.",
        "Tafsir": "Ayat ini menekankan pentingnya kesabaran dan shalat sebagai sarana memperoleh pertolongan Allah. Kesabaran meliputi kesabaran dalam ketaatan, meninggalkan maksiat, dan menghadapi ujian."
    },
    "Ikhlas": {
        "Surat": "Al-Ikhlas 112:1-4",
        "Ayat": "قُلْ هُوَ اللّٰهُ أَحَدٌۚ (١) اللّٰهُ الصَّمَدُۚ (٢) لَمْ يَلِدْ وَلَمْ يُوْلَدْۙ (٣) وَلَمْ يَكُنْ لَّهٗ كُفُوًا اَحَدٌࣖ (٤)",
        "Arti": "Katakanlah (Muhammad), 'Dialah Allah, Yang Maha Esa. Allah tempat meminta segala sesuatu. Dia tidak beranak dan tidak pula diperanakkan. Dan tidak ada sesuatu yang setara dengan Dia.'",
        "Tafsir": "Surat ini menegaskan keesaan Allah dan menolak segala bentuk penyekutuan. Keikhlasan dalam beribadah berarti memurnikan niat hanya untuk Allah semata."
    },
    "Syukur": {
        "Surat": "Ibrahim 14:7",
        "Ayat": "وَإِذْ تَأَذَّنَ رَبُّكُمْ لَئِنْ شَكَرْتُمْ لَأَزِيدَنَّكُمْ وَلَئِنْ كَفَرْتُمْ إِنَّ عَذَابِي لَشَدِيدٌ",
        "Arti": "Dan (ingatlah) ketika Tuhanmu memaklumkan, 'Sesungguhnya jika kamu bersyukur, pasti Kami akan menambah (nikmat) kepadamu, dan jika kamu mengingkari (nikmat-Ku), maka sesungguhnya azab-Ku sangat pedih.'",
        "Tafsir": "Ayat ini mengajarkan bahwa bersyukur akan mendatangkan tambahan nikmat, sedangkan kufur nikmat akan mengundang azab Allah."
    }
}

def tampilkan_menu():
    print("=== 📖 Tafsir Ayat Tematik ===")
    for i, tema in enumerate(ayat_tafsir.keys(), start=1):
        print(f"{i}. {tema}")
    print("0. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih tema ayat (angka): ").strip()

        if pilihan == "0":
            print("Terima kasih telah menggunakan Tafsir Ayat Tematik.")
            break

        try:
            index = int(pilihan) - 1
            tema = list(ayat_tafsir.keys())[index]
            data = ayat_tafsir[tema]
            print("\n=== 📜 Tafsir Ayat ===")
            print(f"Tema : {tema}")
            print(f"Surat: {data['Surat']}")
            print(f"Ayat : {data['Ayat']}")
            print(f"Arti : {data['Arti']}")
            print(f"Tafsir: {data['Tafsir']}\n")
        except (IndexError, ValueError):
            print("Pilihan tidak valid, silakan coba lagi.\n")

if __name__ == "__main__":
    main()
