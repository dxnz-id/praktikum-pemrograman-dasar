import matplotlib.pyplot as plt

def grafik_batang():
    band = [".Feast","Hindia","Wali Band"]
    penjualan = [10,15,8]

    plt.bar(band,penjualan)
    plt.title("Grafik Penjualan Tiket Konser")
    plt.xlabel("Daftar Band")
    plt.ylabel("Jumah Tiket Terjual")
    plt.show()

def grafik_garis():
    x=[1,3,6]
    y=[1,2,5]

    plt.plot(x,y)   # Garis
    plt.scatter(x,y)      # Titik
    plt.show()

def main():
    while True:
        print("===== Grafik dalam Python =====")
        print("0. Keluar")
        print("1. Grafik batang")
        print("2. Grafik garis")
        try:
            choice=int(input("Pilih opsi (1,2,...): "))
            if choice == 0:
                break
            elif choice == 1:
                grafik_batang()
            elif choice == 2:
                grafik_garis()
            else:
                print("\033[31mPilihan tidak valid. Silahkan Coba Lagi\033[0m")
        except ValueError:
            print("\033[31mMasukkan nilai bertipe integer/angka.\033[0m")

if __name__ == "__main__":
    main()