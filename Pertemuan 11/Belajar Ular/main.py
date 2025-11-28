"""
Fungsi (Function) adalah blok kode terorganisir dan dapat digunakan kembali yang digunakan untuk melakukan sebuah tindakan/action. Fungsi memberikan modularitas yang lebih baik untuk aplikasi Anda dan tingkat penggunaan kode yang tinggi.

Mendefinisikan Fungsi: Dimulai dengan kata kunci 'def', diikuti nama fungsi, tanda kurung '()', dan titik dua ':'.
Memanggil fungsi: Cukup tulis nama fungsi diikuti tanda kurung '()'
"""

print("Contoh Konsep Fungsi")
def nama_fungsi():
    print("Hello World1")
nama_fungsi()

def nama_fungsi(pesan):
    print(pesan)
nama_fungsi("Hello world2")

print("Contoh Parameter dan Argumen Fungsi")
def sapa(nama):
    print("halo", nama)
sapa("Sahroni")
sapa("Bahlil")

def tambah_dua_angka(angka1, angka2):
    jumlah = angka1 + angka2
    print("Jumlahnya adalah:", jumlah)
tambah_dua_angka(5,3)

print("Contoh Return")
def hitung_luas(sisi):
    luas = sisi * sisi
    return luas # Mengembalikan nilai dari 'luas'
# Memanggil fungsi dan menyimpan nilai yang dikembalikan
area = hitung_luas(7)
print("Luas persegi:", area)

def bagi_dan_sisa(angka,pembagi):
    hasil = angka//pembagi
    sisa = angka%pembagi
    return hasil, sisa
hasil, sisa = bagi_dan_sisa(10,3)
print(f"Hasil Bagi: {hasil}, Sisa: {sisa}") # Output = Hasil bagi: 3, Sisa: 1

print("Contoh Gabungan Percabangan")
def cek_ganjil_genap(angka):
    if angka&2==0:
        print("genap")
    else:
        print("ganjil")
cek_ganjil_genap(5)

print("Contoh Argumen Kata Kunci")
def info_mobil(model,tahun,warna):
    print(f"Model: {model}, Tahun: {tahun}, Warna: {warna}.")
info_mobil("CRV",2015,"Putih")