# WHILE LOOP
# count = 0
# while count <=10 :
#   print(count, "urutan")
#   count += 1
# print("End")

# x = "FASILKOM"
# while x :
#   print(x, " ")
#   x = x[1:]

# var = int(input("Masukkan Nomor :"))
# g = ""
# if var == 1 :
#   while var <=20 :
#     if var % 2 == 0 :
#       g = "Genap"
#     else :
#       g = "Ganjil"
#     print(f"{var} Bilangan {g}")
#     var += 1

# FOR LOOP
# angka = [1,2,3,4,5]
# for x in angka :
#   print(x)

# # contoh pengulangan for
# buah = ["nanas", "apel", "jeruk"]
# for makanan  in buah :

#   print(f"Saya suka makan {makanan}")

# nama = ["budi", "andi", "rudi", "sandi"]
# usia = [20, 18, 22, 19]
# # for i in range(len(nama)) :
# #   print(f"{nama[i]} berusia {usia[i]} tahun")
# for nama, usia in zip(nama, usia) :
#   print(f"{nama} berusia {usia} tahun")

i = 2
while i <= 100 :
  j = 2
  while j <= (i/j) :
    if not (i%j) :
      break
    j += 1
  if j > i/j :
    print(f"{i} is prime")
  i += 1
print("GoodBye")

count = 1
while (count <= 10) :
  x = 1 
  while (x <= count) :
    print(x, " ", end = '')
    x += 1
  print(" ")
  count += 1