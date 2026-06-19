# ============================================
#   APLIKASI MANAJEMEN NILAI MAHASISWA
#   Menggunakan Konsep List dalam Python
# ============================================

# Data awal mahasiswa (menggunakan list)
data_mahasiswa = [
    ["yadin", 85],
    ["Subhan", 78],
    ["imam", 90],
    ["Juhrin", 72],
    ["Abil", 88]
]


def tampilkan_header():
    """Menampilkan header program."""
    print("\n" + "=" * 44)
    print("   APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("=" * 44)


def tampilkan_menu():
    """Menampilkan menu pilihan."""
    tampilkan_header()
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("-" * 44)


def tampilkan_data():
    """Menampilkan seluruh data mahasiswa."""
    print("\n" + "=" * 44)
    print("         DAFTAR DATA MAHASISWA")
    print("=" * 44)

    if len(data_mahasiswa) == 0:
        print("  (Belum ada data mahasiswa)")
    else:
        print(f"  {'No.':<5} {'Nama Mahasiswa':<20} {'Nilai':>6}")
        print("  " + "-" * 35)
        for i in range(len(data_mahasiswa)):
            nama  = data_mahasiswa[i][0]
            nilai = data_mahasiswa[i][1]
            print(f"  {i+1:<5} {nama:<20} {nilai:>6}")

    print("=" * 44)
    input("\nTekan Enter untuk kembali ke menu...")


def tambah_data():
    """Menambahkan data mahasiswa baru."""
    print("\n" + "=" * 44)
    print("          TAMBAH DATA MAHASISWA")
    print("=" * 44)

    nama = input("  Masukkan nama mahasiswa : ").strip()

    if nama == "":
        print("  [!] Nama tidak boleh kosong.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    # Cek duplikasi nama (tidak case-sensitive)
    for mhs in data_mahasiswa:
        if mhs[0].lower() == nama.lower():
            print(f"  [!] Mahasiswa '{nama}' sudah ada dalam data.")
            input("\nTekan Enter untuk kembali ke menu...")
            return

    try:
        nilai = float(input("  Masukkan nilai mahasiswa (0-100) : "))
        if nilai < 0 or nilai > 100:
            print("  [!] Nilai harus berada di antara 0 dan 100.")
            input("\nTekan Enter untuk kembali ke menu...")
            return
    except ValueError:
        print("  [!] Input nilai tidak valid. Harus berupa angka.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    data_mahasiswa.append([nama, nilai])
    print(f"\n  [✓] Data '{nama}' berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali ke menu...")


def ubah_data():
    """Mengubah data mahasiswa yang sudah ada."""
    print("\n" + "=" * 44)
    print("           UBAH DATA MAHASISWA")
    print("=" * 44)

    if len(data_mahasiswa) == 0:
        print("  [!] Belum ada data mahasiswa.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    nama_cari = input("  Masukkan nama yang ingin diubah : ").strip()
    indeks = -1

    for i in range(len(data_mahasiswa)):
        if data_mahasiswa[i][0].lower() == nama_cari.lower():
            indeks = i
            break

    if indeks == -1:
        print(f"  [!] Mahasiswa '{nama_cari}' tidak ditemukan.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    print(f"\n  Data saat ini:")
    print(f"    Nama  : {data_mahasiswa[indeks][0]}")
    print(f"    Nilai : {data_mahasiswa[indeks][1]}")

    nama_baru = input("\n  Nama baru (Enter untuk tidak mengubah) : ").strip()
    if nama_baru == "":
        nama_baru = data_mahasiswa[indeks][0]

    nilai_input = input("  Nilai baru (Enter untuk tidak mengubah) : ").strip()
    if nilai_input == "":
        nilai_baru = data_mahasiswa[indeks][1]
    else:
        try:
            nilai_baru = float(nilai_input)
            if nilai_baru < 0 or nilai_baru > 100:
                print("  [!] Nilai harus berada di antara 0 dan 100.")
                input("\nTekan Enter untuk kembali ke menu...")
                return
        except ValueError:
            print("  [!] Input nilai tidak valid.")
            input("\nTekan Enter untuk kembali ke menu...")
            return

    data_mahasiswa[indeks][0] = nama_baru
    data_mahasiswa[indeks][1] = nilai_baru
    print(f"\n  [✓] Data berhasil diubah menjadi: [{nama_baru}, {nilai_baru}]")
    input("\nTekan Enter untuk kembali ke menu...")


def hapus_data():
    """Menghapus data mahasiswa berdasarkan nama."""
    print("\n" + "=" * 44)
    print("          HAPUS DATA MAHASISWA")
    print("=" * 44)

    if len(data_mahasiswa) == 0:
        print("  [!] Belum ada data mahasiswa.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    nama_hapus = input("  Masukkan nama yang ingin dihapus : ").strip()
    indeks = -1

    for i in range(len(data_mahasiswa)):
        if data_mahasiswa[i][0].lower() == nama_hapus.lower():
            indeks = i
            break

    if indeks == -1:
        print(f"  [!] Mahasiswa '{nama_hapus}' tidak ditemukan.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    print(f"\n  Data yang akan dihapus:")
    print(f"    Nama  : {data_mahasiswa[indeks][0]}")
    print(f"    Nilai : {data_mahasiswa[indeks][1]}")

    konfirmasi = input("\n  Yakin ingin menghapus? (y/n) : ").strip().lower()
    if konfirmasi == "y":
        nama_terhapus = data_mahasiswa[indeks][0]
        data_mahasiswa.pop(indeks)
        print(f"\n  [✓] Data '{nama_terhapus}' berhasil dihapus!")
    else:
        print("  [i] Penghapusan dibatalkan.")

    input("\nTekan Enter untuk kembali ke menu...")


def cari_data():
    """Mencari data mahasiswa berdasarkan nama."""
    print("\n" + "=" * 44)
    print("           CARI DATA MAHASISWA")
    print("=" * 44)

    kata_kunci = input("  Masukkan nama yang dicari : ").strip()
    hasil = []

    for mhs in data_mahasiswa:
        if kata_kunci.lower() in mhs[0].lower():
            hasil.append(mhs)

    if len(hasil) == 0:
        print(f"\n  [!] Tidak ada mahasiswa dengan nama '{kata_kunci}'.")
    else:
        print(f"\n  Ditemukan {len(hasil)} data:\n")
        print(f"  {'No.':<5} {'Nama Mahasiswa':<20} {'Nilai':>6}")
        print("  " + "-" * 35)
        for i in range(len(hasil)):
            print(f"  {i+1:<5} {hasil[i][0]:<20} {hasil[i][1]:>6}")

    input("\nTekan Enter untuk kembali ke menu...")


def urutkan_data():
    """Mengurutkan data mahasiswa berdasarkan nilai tertinggi (descending)."""
    print("\n" + "=" * 44)
    print("    DATA DIURUTKAN BERDASARKAN NILAI")
    print("=" * 44)

    if len(data_mahasiswa) == 0:
        print("  [!] Belum ada data mahasiswa.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    # Bubble sort manual (descending) — tanpa fungsi sort bawaan
    data_urut = [mhs[:] for mhs in data_mahasiswa]  # salin data agar asli tidak berubah

    n = len(data_urut)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data_urut[j][1] < data_urut[j + 1][1]:
                data_urut[j], data_urut[j + 1] = data_urut[j + 1], data_urut[j]

    print(f"  {'Rank':<6} {'Nama Mahasiswa':<20} {'Nilai':>6}")
    print("  " + "-" * 35)
    for i in range(len(data_urut)):
        print(f"  {i+1:<6} {data_urut[i][0]:<20} {data_urut[i][1]:>6}")

    print("=" * 44)
    input("\nTekan Enter untuk kembali ke menu...")


def hitung_rata_rata():
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    print("\n" + "=" * 44)
    print("       RATA-RATA NILAI MAHASISWA")
    print("=" * 44)

    if len(data_mahasiswa) == 0:
        print("  [!] Belum ada data mahasiswa.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    total = 0
    nilai_tertinggi = data_mahasiswa[0][1]
    nama_tertinggi  = data_mahasiswa[0][0]
    nilai_terendah  = data_mahasiswa[0][1]
    nama_terendah   = data_mahasiswa[0][0]

    for mhs in data_mahasiswa:
        total += mhs[1]
        if mhs[1] > nilai_tertinggi:
            nilai_tertinggi = mhs[1]
            nama_tertinggi  = mhs[0]
        if mhs[1] < nilai_terendah:
            nilai_terendah = mhs[1]
            nama_terendah  = mhs[0]

    rata_rata = total / len(data_mahasiswa)

    print(f"  Jumlah Mahasiswa  : {len(data_mahasiswa)} orang")
    print(f"  Total Nilai       : {total}")
    print(f"  Rata-rata Nilai   : {rata_rata:.2f}")
    print(f"  Nilai Tertinggi   : {nilai_tertinggi} ({nama_tertinggi})")
    print(f"  Nilai Terendah    : {nilai_terendah} ({nama_terendah})")
    print("=" * 44)
    input("\nTekan Enter untuk kembali ke menu...")


# ============================================
#   PROGRAM UTAMA
# ============================================

def main():
    while True:
        tampilkan_menu()
        pilihan = input("  Pilih menu 1-8 : ").strip()

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            cari_data()
        elif pilihan == "6":
            urutkan_data()
        elif pilihan == "7":
            hitung_rata_rata()
        elif pilihan == "8":
            print("\n  Terima kasih! Program selesai.\n")
            break
        else:
            print("\n  [!] Pilihan tidak valid. Masukkan angka 1-8.")
            input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()