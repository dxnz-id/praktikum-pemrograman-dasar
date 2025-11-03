##################################################
##################### Task 1 #####################
##################################################
def tugas1() :
  while True :
    try :
      nilai1 =  int(input("Masukkan nilai 1: "))

      if nilai1 > 100 or nilai1 < 0:
        print("Masukkan nilai antara 0-100")
        continue
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
      break
    except ValueError :
      print("Input tidak valid, silakan masukkan nilai yang benar.")

  
##################################################
##################### Task 2 #####################
##################################################
def tugas2() :
  # Currency Format
  def currency_format(amount):
    return f"Rp. {amount:,}".replace(",", ".")
  
  print("LIBURANYUK | Menjual tiket murah dengan tujuan LabuanBajo\n[A] MaskapaiSupreme  : Rp. 1.000.000/ticket\n[B] MaskapaiKuda     : Rp. 800.000/ticket\n[C] MaskapaiMacan    : Rp. 500.000/ticket")

  # Ticket
  while True:
    maskapai = input("Pilih maskapai [A/B/C]: ").lower()
    if maskapai in ("a", "b", "c"):
      break
    print("Maskapai tidak valid, silakan masukkan nilai yang benar.")
  while True :
    try :
      ticket = int(input("jumlah ticket: "))
      if ticket <= 0 :
        print("Masukkan nilai lebih besar dari 0")
        continue
      break
    except :
      print("Jumlah tiket tidak valid, silakan masukkan nilai yang benar.")

  total = 0
  if maskapai == "a" :
    total = (1000000 * ticket)
  elif maskapai == "b" :
    total = (800000 * ticket)
  elif maskapai == "c" :
    total = 500000 * ticket

  # Is Online / Discount
  while True :
    isOnline = input("Beli secara online [Y/n]: ").lower() or "y"
    if isOnline == "y" :
      disc = int(total - total * .1)
      print("="*100, "\nSelamat, anda mendapat diskon 10%\nHarga sebelum diskon :", currency_format(total), "\nTotal pembelian anda :", currency_format(disc))
      break
    elif isOnline == "n" :
      print("="*100, "\nTotal pembelian anda :", currency_format(total))
      break
    else :
      print("Input tidak valid, silakan masukkan nilai yang benar.")
      continue

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
def select_task() :
  while True :
    tugas = int(input("Mau jalanin tugas berapa: "))
    if tugas == 1:
      tugas1(); break
    elif tugas == 2:
      tugas2(); break
    else :
      print("Tugas tidak ditemukan"); continue

select_task()