# MENCARI GANJIL GENAP
x = int(input("Inputkan bilangan yang akan dicetak: "))

if (x%2==0) :
        print(x, "merupakan bilangan genap")
else :
        print(x, "merupakan bilangan ganjil")

print("="*50)

# VALIDASI GRADE NILAI
nilai = int(input("Inputkan bilangan nilai :"))
if nilai > 90 :
    print("Grade: A")
elif nilai > 80 :
    print("Grade: B")
elif nilai > 70 :
    print("Grade: C")
elif nilai > 60 :
    print("Grade: D")
else :
    print("Grade: E")

print("="*50)

# VALIDASI KATEGORI USIA

usia = int(input("Berapa umur kamu :"))

if usia < 13:
    print("Kategori: Anak-anak")
elif usia < 18:
    print("Kategori: Remaja")
else:
    print("Kategori: Dewasa")

print("="*50)

# VALIDASI DISKON
total_belanja = int(input("Masukkan total belanja Anda: Rp. "))
diskon = 0

if total_belanja > 500000 :
    diskon = .2 #20%
elif total_belanja >= 200000 :
    diskon = .1 #10%

harga_akhir = total_belanja - (total_belanja * diskon)
print(f"Total belanja: Rp.{int(total_belanja)}")
print(f"Total diskon: {int(diskon * 100)}%")
print(f"Total yang harus dibayar: Rp.{int(harga_akhir)}")