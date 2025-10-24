# TUGAS PERTEMUAN 6

harga = int(input("Total Belanja :"))
member = str(input("Jenis kartu member |platinum|gold|silver| :")).lower()

member_list = ["platinum", "gold", "silver"]

diskon = 0

# Konversi input
if member == "1" :
    member = member_list[0]
if member == "2" :
    member = member_list[1]
if member == "3" :
    member = member_list[2]

# Validasi diskon
if member in member_list:
    if member == member_list[0] :
        diskon = .15
    elif member == member_list[1] :
        diskon = .10
    elif member == member_list[2] :
        diskon = .05
        
    total_harga = harga - (harga * diskon)
    print(f"\033[32mHarga: Rp.{int(harga)}")
    print(f"Total diskon member {str(member).upper()}: {int(diskon * 100)}%")
    print(f"Total Harga: Rp.{int(total_harga)}")
else :
    print("invalid member")