from task_1 import task_1
from task_2 import task_2

while True :
  tugas = input("Mau jalanin tugas berapa: ") or 1
  if tugas == "1":
    task_1(); break
  elif tugas == "2":
    task_2(); break
  else :
    print("Tugas tidak ditemukan"); continue
