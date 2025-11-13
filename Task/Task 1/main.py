from InquirerPy import inquirer

data = {
  "NIM": "202551049",
  "Full Name": "Muhammad La'azidannak Rusda",
  "Nickname": "Zidan",
  "Age": 18,
  "Address": "Suryo Kusumo Street, Mejobo, Kudus, Central Java",
  "Phone Number": "085728644127"
}

option = inquirer.select(
    message="Pilih apa yang akan ditampilkan:",
    choices=data.keys()
).execute()

print(f"{option} : {data[option]}")