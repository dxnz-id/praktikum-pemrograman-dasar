# Contoh sederhana pembuatan list pada bahasa pemrograman python
list1 = ['sistem komputer', 'teknik informatika', 2008, 2020]
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d"]
print(list1)
print(list2)
print(list3)

# Cara mengakses nilai di dalam list python
list1 = ['sistem komputer','teknik informatika',2008,2020]
list2 = [1,2,3,4,5,6,7]
print(f"list1[0]: {list1[0]}")
print(f"list2[1:5]: {list2[1:5]}")

# Cara mengubah value pada list python
list = ['sistem komputer','teknik informatika',2008,2020]
list[2] = 2001
print(f" Nilai baru ada pada index 2: {list[2]}")

# Cara menghapus value di dalam list python
# Contoh 1
contoh_list = ['jeruk','mangga',"apel","nanas"]
print(contoh_list)
del contoh_list[2]
print(f"Setelah dihapus nilai pada index 2: {contoh_list}")

# Contoh 2
contoh_list = ['jeruk','mangga',"apel","nanas"]
print(contoh_list)
contoh_list.remove("mangga")
print(f"Setelah dihapus nilai pada list: {contoh_list}")

# Operasi pada list
list_terbaru = ["Sepeda","Motor","Mobil","Pesawat","Kapal"]
# Length
print(len(list_terbaru))
# Concatenation
list_new = ["Kereta Api","Jet"]
list_update = list_terbaru + list_new
print(list_update)
# Repetition
list_ulang = list_update*4
print(list_ulang)
# Membership
print("Motor" in list_ulang)

# Iteration
for x in list_ulang:
    print(x,end = '')
for x in list_ulang:
    print(f"list_ulang[{list_ulang.index(x)}]: {x}")

# Indexing, Slicing, dan Matrix Pada List Python
new_list = ["bebek","ayam","kambing","kerbau"]
# Indexing
print(new_list[2])
# Slicing
print(new_list[1:])
print(new_list[1:3])
# Matrix
print(new_list[-2])
# Operator
print(max(new_list))
print(min(new_list))
new_list = [1,2,3,4,5,6,7,8,9]
print(max(new_list))
print(min(new_list))

# Contoh sederhana pembuatan tuple pada bahasa pemrograman python
tup1 = ('sistem komputer', 'teknik informatika', 2008, 2020)
tup2 = (1,2,3,4,5)
tup3 = ("a","b","c","d")
print(tup1)
print(tup2)
print(tup3)