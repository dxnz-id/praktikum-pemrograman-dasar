# Experiment

# =================================================
# ========== SISTEM PERPUSTAKAAN DIGITAL ==========
# =================================================

# Data pengguna
user_data = {
    "U1": {"username": "arvia21", "password": "arvi1234", "role": "admin"},
    "U2": {"username": "pakril45", "password": "udin123", "rols": "user"},
}

# Daftar buku
buku = []

# Sesi login
session = ""

def login():
    print("===== Login =====")
    username = input("Masukkan username anda: ")
    password = input("Masukkan sandi anda: ")

# Main function
def main():
    while True:
        print("========== Sistem Perpustakaan ==========")
        if session == "" :
            print("0. Exit")
            print("1. Login")
        else:
            print("0. Exit")
            print("1. Logout")
            print("2. Lihat Buku")
        try:
            choice = int(input("Pilih menu (1,2,..)"))
            if session == "":
                if session == "" :
                    if choice == 0 :
                        break
        except ValueError:
            print("\033[31mPilihan tidak valid. Silahkan Coba Lagi\033[0m")