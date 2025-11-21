import random
import time

# --------------------------
# Fungsi Utility
# --------------------------

def clear_screen():
    print("\033[H\033[J", end="")

def warna(teks, kode):
    return f"\033[{kode}m{teks}\033[0m"

def goodbye_screen():
    clear_screen()
    print(warna("╔══════════════════════════════════════╗", "31"))
    print(warna("║                                      ║", "31"))
    print(warna("║        S A M P A I   J U M P A       ║", "31"))
    print(warna("║                                      ║", "31"))
    print(warna("╚══════════════════════════════════════╝", "31"))
    time.sleep(1.8)

def splash_screen():
    clear_screen()
    print(warna("╔════════════════════════════════════════╗", "36"))
    print(warna("║                                        ║", "36"))
    print(warna("║      T E B A K   K A T A   J A W A     ║", "36"))
    print(warna("║                                        ║", "36"))
    print(warna("╚════════════════════════════════════════╝", "36"))

    print("\nMemuat", end="")
    for _ in range(5):
        print(warna(".", "33"), end="", flush=True)
        time.sleep(0.4)
    print("\n")
    time.sleep(0.5)

def tampil_panel_soal(soal_no, kata):
    print(warna("\n" + "-" * 60, "33"))
    print(warna(f"        SOAL {soal_no}        ", "33"))
    print(f" Apa Bahasa Jawa dari '{kata}'?")
    print(warna("-" * 60, "33"))

def tampil_hasil(username, skor, jumlah_soal):
    nilai = skor / jumlah_soal * 100

    kategori_text = (
        "Bagus" if nilai >= 80 else
        "Sedang" if nilai >= 50 else
        "Kurang"
    )

    baris = [
        f"Username : {username}",
        f"Benar    : {skor}/{jumlah_soal}",
        f"Nilai    : {nilai:.0f}%",
        f"Kategori : {kategori_text}"
    ]

    panjang = max(len(b) for b in baris) + 6
    garis_atas = "╔" + "═" * panjang + "╗"
    garis_bawah = "╚" + "═" * panjang + "╝"

    print(warna(garis_atas, "96"))
    print(warna("║" + " HASIL AKHIR ".center(panjang) + "║", "96"))
    print(warna("╠" + "═" * panjang + "╣", "96"))

    for isi in baris:
        print(warna("║ " + isi.ljust(panjang - 1) + "║", "96"))

    print(warna(garis_bawah, "96"))

# --------------------------
# Kamus Kata
# --------------------------

kamus = {
    "aku": "kula",
    "makan": "mangan",
    "minum": "ngombe",
    "tidur": "turu",
    "rumah": "omah",
    "pergi": "lunga",
    "kamu": "kowe",
    "baca": "maca",
    "beli": "tuku",
    "kambing": "wedhus",
    "kuda": "jaran",
    "semua": "kabeh",
    "mau": "arep",
    "mandi": "adus",
    "biar": "yen",
    "orang": "wong",
    "pulang": "mulih",
    "berdiri": "ngadeg",
    "duduk": "lungguh",
    "menyuruh": "ngongkon",
    "membuat": "gawe",
    "berani": "wani",
    "marah": "nesu",
    "takut": "wedi",
    "senang": "bungah",
    "permisi": "kula nuwun",
    "terima kasih": "matur nuwun",
    "selamat pagi": "sugeng enjing",
    "selamat malam": "sugeng dalu",
    "jari": "driji",
    "kaki": "sikil",
    "muka": "rai",
    "badan": "awak",
    "mata": "mripat",
    "mulut": "lambe",
    "hujan": "udan"
}

# --------------------------
# Fungsi Permainan
# --------------------------

def jalankan_permainan(username):
    clear_screen()

    # Input jumlah soal
    while True:
        try:
            jumlah_soal = int(input("Masukkan jumlah soal 5-25: "))

            if jumlah_soal < 5:
                print(warna("Minimal jumlah soal adalah 5!", "31"))
                continue
            if jumlah_soal > 25:
                print(warna("Jumlah soal maksimal 25!", "31"))
                continue
            break

        except ValueError:
            print(warna("Masukkan angka yang valid!", "31"))

    clear_screen()
    skor = 0
    soal_list = random.sample(list(kamus.keys()), jumlah_soal)

    for i, kata in enumerate(soal_list, start=1):
        tampil_panel_soal(i, kata)
        jawab = input("Jawabanmu: ").lower()

        if jawab == kamus[kata]:
            print(warna("\n✅ Benar!\n", "32"))
            skor += 1
        else:
            print(warna(f"\n❌ Salah! Jawaban benar: {kamus[kata]}\n", "31"))

        print(warna(f"Skor sementara: {skor}/{i}\n", "36"))
        time.sleep(0.7)

    # Jarak sebelum menampilkan skor akhir
    print("\n" * 5)
    time.sleep(0.3)

    # Tampilkan hasil akhir tanpa clear screen
    tampil_hasil(username, skor, jumlah_soal)
    print("\n" * 2)

# --------------------------
# Main Program
# --------------------------

splash_screen()

username = input("Halo! Masukkan username kamu: ").strip().title()

while True:
    clear_screen()
    print(warna(f"Selamat datang, {username}!", "32"))
    print(warna("\nCatatan:", "33"))
    print("• Soal acak, maksimal 25.")
    print("• Jawab dalam Bahasa Jawa Ngoko.")
    print("• Kata bisa berupa kerja, sifat, hewan, bagian tubuh.\n")

    ready = input("Ketik 'iya' untuk mulai atau 'tidak' untuk keluar: ").lower()

    if ready == "iya":
        print(warna("Ayo kita mulai!\n", "32"))
        time.sleep(1)

        jalankan_permainan(username)

        # Menu main lagi
        while True:
            print("\nApa kamu ingin bermain lagi?")
            lagi = input("Ketik 'iya' untuk main lagi atau 'tidak' untuk keluar: ").lower()

            if lagi == "iya":
                clear_screen()
                print(warna("Ayo kita mulai!\n", "32"))
                time.sleep(1)
                jalankan_permainan(username)

            elif lagi == "tidak":
                goodbye_screen()
                exit()

            else:
                print(warna("Input tidak valid!", "31"))
                time.sleep(1)

    elif ready == "tidak":
        goodbye_screen()
        exit()

    else:
        print(warna("Input tidak valid! Masukkan 'iya' atau 'tidak'.", "33"))
        time.sleep(1)
