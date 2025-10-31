from multiprocessing import Pool, cpu_count
import itertools

# ANSI escape code buat warna hijau dan reset
GREEN = "\033[92m"
RESET = "\033[0m"

def cek_prima(a):
    j = 2
    is_prima = True

    while j < a:
        if a % j == 0:
            is_prima = False
            break
        j += 1

    # Print angka, kasih warna hijau kalau prima
    if is_prima:
        print(f"{GREEN}{a}{RESET}", flush=True)
    else:
        print(a, flush=True)

    return None


if __name__ == "__main__":
    with Pool(cpu_count()) as p:
        for _ in p.imap_unordered(cek_prima, itertools.count(1)):
            pass

# num = 0
# limit = 500
# while num <= limit :
#     if num == 0 or num == 1:
#         pass
#     elif num > 1 :
#         bil = 2
#         is_prime = True
#         while bil <= (num // 2) :
#             if num % bil == 0 :
#                 is_prime = False
#                 break
#             bil += 1
#         if is_prime :
#             print(num)

#     num += 1