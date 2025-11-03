##################################################
##################### Task 1 #####################
##################################################
def tugas1() :
  nilai1 =  int(input("Masukkan nilai 1: "))

  if nilai1 > 100 or nilai1 < 0:
    print("Nilai tidak valid")
  elif nilai1 >= 90 :
    print("Nilai A")
  elif nilai1 >= 75 :
    print("Nilai B")
  elif nilai1 >= 60 :
    print("Nilai BC")
  elif nilai1 <= 50 :
    print("Nilai C")
    nilai2 = int(input("Masukkan nilai 2: "))
    if nilai2 > 90 :
      print("Pertahankan")
    else :
      print("Belajar lebih giat")

##################################################
##################### Task 2 #####################
##################################################
def tugas2() :
  print("LIBURANYUK | Menjual tiket murah dengan tujuan LabuanBajo")
  print("[A] MaskapaiSupreme  : Rp. 1.000.000/ticket")
  print("[B] MaskapaiKuda     : Rp. 800.000/ticket")
  print("[C] MaskapaiMacan    : Rp. 500.000/ticket")

  # Input
  maskapai = input("Pilih maskapai [A/B/C]: ").lower()
  if maskapai != "a" and maskapai != "b" and maskapai != "c":
    print("Invalid maskapai")
    exit()
  ticket = int(input("jumlah ticket: "))
  isOnline = input("Beli secara online [Y/n]: ").lower() or "y"

  # Total
  total = 0
  if maskapai == "a" :
    total = (1000000 * ticket)
  elif maskapai == "b" :
    total = (800000 * ticket)
  elif maskapai == "c" :
    total = 500000 * ticket

  print("="*100)

  # Discount
  if isOnline == "y" :
    print("Selamat, anda mendapat diskon 10%")
    print("Harga sebelum diskon :", f"{total:,}")
    disc = int(total - total * .1)
    print("Total pembelian anda :", f"{disc:,}")
  elif isOnline == "n" :
    print("Total pembelian anda :", f"{total:,}")

  # Bonus
  if total > 10000000 :
    print("Anda mendapat voucher belanja")
  elif total > 5000000 :
    print("Anda mendapat kaos")
  else :
    print("Anda mendapat topi")


##################################################
################# Task Selection #################
##################################################
tugas = int(input("Mau jalanin tugas berapa: "))
if tugas == 1:
  tugas1()
elif tugas == 2:
  tugas2()