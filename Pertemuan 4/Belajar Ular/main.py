#################
####Functioni####
#################

# Validasi Input
def FloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("\033[31mMohon Masukkan Data Tipe Data Yang Sesuai\033[0m")

# Print Hasil
def PrintResult(result):
    print("\033[32mHasilnya adalah : ", result, "\033[0m")

##########################################################################

# Inputan Dinamis

print("Mencari Luas Segitiga Siku-Siku")
print("="*50)
a = FloatInput("Nnputkan Nilai a :")
t = FloatInput("Inputkan Nilai t :")
L = .5 * a * t
PrintResult(L)

##########################################################################
print("="*50)

print("Mencari Luas Persegi Panjang")
print("="*50)
p = FloatInput("Inputkan Panjang :")
l = FloatInput("Inputkan Lebar :")

Persegi_Panjang = p * l
PrintResult(Persegi_Panjang)

##########################################################################
print("="*50)

phi = 3.14
print("Mencari Luas Lingkaran")
print("="*50)
r = FloatInput("Masukkan Jaring-Jaring a :")
Lingkaran = phi * r ** 2
PrintResult(Lingkaran)

##########################################################################
print("="*50)

print("Mencari Luas Layang-Layang")
d1 = FloatInput("Masukkan Diagonal 1 :")
d2 = FloatInput("Masukkan Diagonal 2 :")
layang = 1/2 *d1 * d2
PrintResult(layang)