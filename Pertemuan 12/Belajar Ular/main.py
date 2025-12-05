mahasiswa = []

def tambah_data():
    print("\n--- Tambah Data Mahasiswa ---")
    while True:
        try:
            try:
                nim = float(input("Masukkan NIM: "))
            except ValueError:
                print("Input nilai tidak valid. Harap masukkan angka.")
                return
            for m in mahasiswa:
                if m['nim'] == nim:
                    raise ValueError("\033[31mUser telah terdaftar.\033[0m")
            nama = input("Masukkan Nama: ")
            try:
                nilai = float(input("Masukkan Nilai: "))
            except ValueError:
                print("Input nilai tidak valid. Harap masukkan angka.")
                return

            data = {"nim": nim, "nama": nama, "nilai": nilai}
            mahasiswa.append(data)
            print("Data berhasil ditambahkan!")
            return data
        except ValueError:
            print("\033[31mUser telah terdaftar.\033[0m")

def tampilkan_data():
    print("\n--- Daftar Mahasiswa ---")
    if len(mahasiswa) == 0:
        print("Belum ada data.")
        return
    for index, m in enumerate(mahasiswa, start=1):
        print(f"{index}. NIM: {m['nim']}, Nama : {m['nama']}, Nilai: {m['nilai']}")

def cari_data():
    print("\n--- Cari Mahasiswa ---")
    nim_cari = input("Masukkan NIM yang dicari: ")

    for m in mahasiswa:
        if m['nim'] == nim_cari:
            print(f"Ditemukan: NIM: {m['nim']}, Nama: {m['nama']}, Nilai: {m['nilai']}")
            return
        print("Data tidak ditemukan.")

def hitung_statistik():
    print("\n--- Statistik Data ---")
    if len(mahasiswa)==0:
        print("Belum ada data.")
        return
    total=0
    nilai_tertinggi = mahasiswa[0]["nilai"]
    nilai_terendah = mahasiswa[0]["nilai"]
    for m in mahasiswa:
        nilai = m["nilai"]
        total += nilai

        if nilai>nilai_tertinggi:
            nilai_tertinggi = nilai
        if nilai<nilai_terendah:
            nilai_terendah = nilai
    rata = total / len(mahasiswa)
    print(f"Jumlah Mahasiswa : {len(mahasiswa)}")
    print(f"Rata-rata Nilai : {rata:.2f}")
    print(f"Nilai Tertinggi : {nilai_tertinggi}")
    print(f"Nilai Terendah : {nilai_terendah}")

def main():
    while True:
        print("\n===== SISTEM DATA MAHASISWA =====")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Semua Data")
        print("3. Cari Mahasiswa")
        print("4. Statistik")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih menu (1-5): "))

            if pilih == 1:
                tambah_data()
            elif pilih == 2:
                tampilkan_data()
            elif pilih == 3:
                cari_data()
            elif pilih == 4:
                hitung_statistik()
            elif pilih == 5:
                print("Program selesai. Terima kasih.")
                break
            else:
                print("\033[31mPilihan tidak valid. Silahkan Coba Lagi\033[0m")
        except:
            print("\033[31mPilihan tidak valid. Silahkan Coba Lagi\033[0m")

if __name__ == "__main__":
    main()