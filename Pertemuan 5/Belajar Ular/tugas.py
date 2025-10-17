hari_kuliah = ["senin", "rabu", "jumat", "jum'at"]
hari_kerja = ["selasa", "kamis", "sabtu"]
hari_libur = ["minggu"]

hari = input(str("Masukkan hari: ")).lower()

if hari in hari_kuliah:
    print(f"{hari.capitalize()} adalah hari kuliah")
elif hari in hari_kerja:
    print(f"{hari.capitalize()} adalah hari kerja")
elif hari in hari_libur:
    print(f"{hari.capitalize()} adalah hari libur")
else:
    print("Hari yang Anda masukkan tidak valid")