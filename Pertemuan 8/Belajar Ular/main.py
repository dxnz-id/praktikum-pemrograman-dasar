'''
Nama        : Muhammad La'azidannak Rusda
Nim         : 202551049
Kelas       : B 
Prodi       : Teknik Informatika
Persoalan   : Klasifikasi barang berdasarkan nilai barang
'''

nama_benda_049=input("Masukkan nama benda :")
str_validate_049=" ya[1] | tidak[0] : "

attempt = 3
def input_attempt_049(attempt):
    attempt -= 1
    print(f"sisa {attempt} kali percobaan input")
    if attempt == 0:
        print("Terlalu banyak kesalahan input")
        exit()
    return attempt

while True :    
    try :
        bukan_sampah_049 = int(input(f"Benda '{nama_benda_049}' bukanlah sampah.{str_validate_049}"))
        if bukan_sampah_049 not in (0,1):
            attempt=input_attempt_049(attempt)
            print("Masukkan nilai [1] untuk ya dan [0] untuk tidak")
            continue
        break
    except:
        attempt=input_attempt_049(attempt)
        print("Masukkan nilai [1] untuk ya dan [0] untuk tidak")

if bukan_sampah_049==1:
    while True :    
        try :
            masih_berfungsi_049=int(input(f"Apakah benda {nama_benda_049} berfungsi dengan baik?{str_validate_049}"))
            if masih_berfungsi_049 not in (0,1):
                attempt=input_attempt_049(attempt)
                print("Masukkan nilai [1] untuk ya dan [0] untuk tidak")
                continue
            break
        except:
            print("Masukkan nilai [1] untuk ya dan [0] untuk tidak")
            attempt=input_attempt_049(attempt)
    if masih_berfungsi_049==1:
        print(f"Benda {nama_benda_049} jangan dibuang")
    else:
        print(f"Kirim {nama_benda_049} ke tempat perbaikan")
else:
    while True :    
        try :
            apakah_anorganik_049=int(input(f"Apakah dalam kategori anorganik?{str_validate_049}"))
            if apakah_anorganik_049 not in (0,1):
                attempt=input_attempt_049(attempt)
                print("Masukkan nilai [1] untuk anorganik dan [0] untuk organik")
                continue
            break
        except:
                attempt=input_attempt_049(attempt)
                print("Masukkan nilai [1] untuk anorganik dan [0] untuk organik")
    if apakah_anorganik_049==1:
        while True :    
            try :
                dapat_didaur_ulang_049=int(input(f"Apakah {nama_benda_049} dapat didaur ulang?{str_validate_049}"))
                if dapat_didaur_ulang_049 not in (0,1):
                    attempt=input_attempt_049(attempt)
                    print("Masukkan nilai [1] untuk ya dan [0] untuk tidak")
                    continue
                break
            except:
                attempt=input_attempt_049(attempt)
                print("Masukkan nilai [1] untuk ya dan [0] untuk tidak")
        if dapat_didaur_ulang_049 == 1:
            print("Jual di tempat rongsok")
        else:
            print("Buang ditempat sampah")
    else:
        print(f"Benda {nama_benda_049} jadikan pupuk")

# apakahsampah
# tidak - berfungsi dengan baik?
#   ya - benda jangan dibuang
#   tidak - harus diperbaiki

# ya - apakah anorganik
    # tidak - jadikan pupuk
    # ya - dapat didaur ulang?
        # ya - jual di tempat rongsok
        # buang ke tempat sampah
