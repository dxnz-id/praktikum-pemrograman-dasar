def task_1() :
  while True :
    try :
      nilai_1 =  int(input("Masukkan nilai 1: "))

      if nilai_1 > 100 or nilai_1 < 0:
        print("Masukkan nilai antara 0-100")
        continue
      elif nilai_1 >= 90 :
        print("Nilai A")
      elif nilai_1 >= 75 :
        print("Nilai B")
      elif nilai_1 >= 60 :
        print("Nilai BC")
      elif nilai_1 <= 50 :
        print("Nilai C")
        nilai_2 = int(input("Masukkan nilai 2: "))
        if nilai_2 > 90 :
          print("Pertahankan")
        else :
          print("Belajar lebih giat")
      break
    except ValueError :
      print("Input tidak valid, silakan masukkan nilai yang benar.")