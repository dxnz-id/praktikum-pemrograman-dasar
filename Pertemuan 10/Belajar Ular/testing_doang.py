user = {
    1 : {
        "nama" : "Arvia Faustina Ardhan",
        "kelas" : "B",
        "buku_dipinjam" : {
            1 : {
                "judul" : "Java Basics",
                "issn" : 123456,
                "due_date" : "12/06/2025"
            }
        }
    }
}

print(user[1].items().mapping["buku_dipinjam"].items().mapping[1].items().mapping["judul"])