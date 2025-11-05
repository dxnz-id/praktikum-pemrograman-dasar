def task_2() :
  # Currency Format
  def currency_format(amount):
    return f"Rp. {amount:,}".replace(",", ".")
  
  print("LIBURANYUK | Menjual tiket murah dengan tujuan LabuanBajo\n[A] MaskapaiSupreme  : Rp. 1.000.000/ticket\n[B] MaskapaiKuda     : Rp. 800.000/ticket\n[C] MaskapaiMacan    : Rp. 500.000/ticket")

  # Ticket
  while True:
    maskapai = input("Pilih maskapai [A/B/C]: ").lower()
    if maskapai in ("a", "b", "c", "1", "2", "3"):
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
  if maskapai in ("a", "1"):
    total = (1000000 * ticket)
  elif maskapai in ("b", "2") :
    total = (800000 * ticket)
  elif maskapai in ("c", "3") :
    total = 500000 * ticket

  # Is Online / Discount
  while True :
    is_online = input("Beli secara online [Y/n]: ").lower() or "y"
    if is_online == "y" :
      disc = int(total - total * .1)
      print("="*100, "\nSelamat, anda mendapat diskon 10%\nHarga sebelum diskon :", currency_format(total), "\nTotal pembelian anda :", currency_format(disc))
      break
    elif is_online == "n" :
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