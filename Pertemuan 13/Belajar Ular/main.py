# ========================================
# SISTEM KASIR MINI (DENGAN DISKON & PAJAK)
# ========================================

TAX_RATE = .10 #10% pajak

#Daftar barang di toko (kode: {nama, kategori, harga})
barang_toko = {
    "A1": {"nama": "Indomie Goreng",        "kategori": "Makanan", "harga": 3500},
    "A2": {"nama": "Indomie Rebus",         "kategori": "Makanan", "harga": 3000},
    "A3": {"nama": "Telur Ayam (butir)",    "kategori": "Telur",   "harga": 2500},
    "A4": {"nama": "Air Mineral 600ml",     "kategori": "Minuman", "harga": 4000},
    "A5": {"nama": "Teh Botol",             "kategori": "Minuman", "harga": 5000},
}

# Keranjang belanja berupa list of directory

keranjang = []

def tampilkan_daftar_barang():
    """Menampilkan daftar barang yang tersedia di toko."""
    print("\n\033[32m--- DAFTAR BARANG TOKO ---\033[0m")
    print("{:<5} {:<20} {:<10} {:>10}".format("Kode", "Nama", "Kategori", "Harga"))
    print("-"*55)
    for kode, info in barang_toko.items():
        print("{:<5} {:<20} {:<10} {:>10}".format(
            kode,
            info["nama"],
            info["kategori"],
            info["harga"],
        ))

def tambah_ke_keranjang():
    """Menambahkan barang ke keranjang berdasarkan kode dan jumlah."""
    tampilkan_daftar_barang()
    kode = input("\nMasukkan kode barang (misal A1): ").upper()
    if kode not in barang_toko:
        print("\033[31mKode barang tidak ditemukan.\033[0m")
        return
    try:
        qty = int(input("Masukkan jumlah: "))
    except ValueError:
        print("\033[31mJumlah harus berupa angka.\033[30m")
        return

    if qty <= 0:
        print("\033[31mJumlah harus lebih dari 0.\033[0m")
        return

    barang = barang_toko[kode]
    subtotal = barang["harga"]*qty
    item_keranjang = {
        "kode": kode,
        "nama": barang["nama"],
        "kategori": barang["kategori"],
        "harga": barang["harga"],
        "qty": qty,
        "subtotal": subtotal,
    }

    keranjang.append(item_keranjang)
    print(f"{qty} x {barang['nama']} berhasil ditambahkan ke keranjang.")

def tampilkan_keranjang():
    """Menampilkan isi keranjang belanja dan total sementara."""
    print("\n\033[32m--- KERANJANG BELANJA ---\033[0m")

    if len(keranjang) == 0:
        print("\033[31mKeranjang masih kosong.\033[0m")
        return

    print("{:<5} {:<20} {:<10} {:>6} {:>10} {:>12}".format(
        "No", "Nama", "Kategori", "Qty", "Harga", "Subtotal"
    ))
    print("-"*75)

    total=0
    for i, item in enumerate(keranjang, start=1):
        total += item["subtotal"]
        print("{:<5} {:<20} {:<10} {:>6} {:>10} {:>12}".format(
            i,
            item["nama"],
            item["kategori"],
            item["qty"],
            item["harga"],
            item["subtotal"],
        ))

    print("-"*75)
    print(f"TOTAL SEMENTARA: {total}")

def hitung_total():
    """Menghitung total belanja dari keranjang (sebelum diskon & pajak)."""
    total = 0
    for item in keranjang:
        total += item["subtotal"]
        return total

def proses_pembayaran():
    """
    Melakikan proses pembayaran:
    - Hitung total kotor
    - Minta persentase diskon (jika ada)
    - Hitung pajak setelah diskon
    - Minta input uang bayar
    - Hitung kembalian
    """
    if len(keranjang)==0:
        print("\n\033[31mKeranjang kosong, tidak ada yang dibayar\033[0m")
        return

    # Total sebelum diskon & pajak
    total_kotor = hitung_total()
    print("\n\033[32m--- PEMBAYARAN ---\033[0m")
    print(f"Total belanja (sebelum diskon & pajak): {total_kotor}")

    # Diskon (persentase)
    diskon_persen = 0.0
    jawab_diskon = input("Apakah ada diskon? (Y/N): ").lower()
    if jawab_diskon == "y":
        try:
            diskon_persen = float(input("Masukkan persen diskon (misal 10 untuk 10%): "))
            if diskon_persen < 0:
                print("\033[31mDiskon tidak boleh negatif. Dianggap 0%.\033[0m")
                diskon_persen = .0
        except ValueError:
            print("\033[31mInput diskon tidak valid. Dianggap 0%.\033[0m")
            diskon_persen = .0

    jumlah_diskon = total_kotor * (diskon_persen / 100.0)
    total_setelah_diskon = total_kotor - jumlah_diskon

    # Pajak setelah diskon
    pajak = total_setelah_diskon * TAX_RATE
    grand_total = total_setelah_diskon + pajak

    print("\nRINCIAN TAGIHAN:")
    print(f"Total kotor          : {total_kotor}")
    print(f"Diskon ({diskon_persen:.1f}%)         : -{jumlah_diskon:.2f}")
    print(f"Total setelah diskon : {total_setelah_diskon:.2f}")
    print(f"Pajak                : +{pajak:.2f}")
    print(f"TOTAL AKHIR          : {grand_total:.2f}")

    # Input pembayaran
    try:
        bayar = float(input("\nMasukkan jumlah uang bayar: "))
    except ValueError:
        print("\033[31mInput tidak valid. Pembayaran dibatalkan.\033[0m")
        return

    if bayar < grand_total:
        print("\033[31mUang tidak cukup. Pembayaran dibatalkan.\033[0m")
        return

    kembalian = bayar - grand_total
    print(f"Pembayaran berhasil. Kembalian: {kembalian:.2f}")

    # Setelah transaksi selesai, kosongkan keranjang
    keranjang.clear()
    print("\033[32mKeranjang telah dikosongkan. Transaksi selesai.\033[0m")

def main():
    """Fungsi utama yang menjalankan menu kasir."""
    while True:
        print("\n\033[32m===== SISTEM KASIR MINI =====\033[0m")
        print("1. Tampilkan Daftar Barang")
        print("2. Tambah Barang ke Keranjang")
        print("3. Lihat Keranjang")
        print("4. Pembayaran")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih menu (1-5): "))
            if pilih == 1:
                tampilkan_daftar_barang()
            elif pilih == 2:
                tambah_ke_keranjang()
            elif pilih == 3:
                tampilkan_keranjang()
            elif pilih == 4:
                proses_pembayaran()
            elif pilih == 5:
                print("Program selesai. Terima kasih.")
                break
            else:
                print("\033[31mPilihan tidak valid. Silahkan Coba Lagi\033[0m")
        except ValueError:
            print("\033[31mPilihan tidak valid. Silahkan Coba Lagi\033[0m")

if __name__ == "__main__":
    main()