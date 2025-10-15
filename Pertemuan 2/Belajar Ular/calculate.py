# INPUT & VARIABLE
print("penjumlahan  : 1")
print("pengurangan  : 2")
print("perkalian    : 3")
print("pembagian    : 4")
operation = int(input("operasi yang anda inginkan: "))
a1 = int(input("masukkan angka pertama: "))
a2 = int(input("masukkan angka kedua: "))

# OPERASI
if (operation == 1):
    result = a1 + a2
if (operation == 2):
    result = a1 - a2
if (operation == 3):
    result = a1 * a2
if (operation == 4):
    result = a1 / a2

print(result)