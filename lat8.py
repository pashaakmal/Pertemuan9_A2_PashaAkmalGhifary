# Pendeklarasian array
buku = []

# Fungsi ShowData
def show_data():
    if len(buku) <= 0:
        print("Belum Ada Data")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

# Fungsi InsertData
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

# Fungsi EditData
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku) or indeks < 0:
        print("ID Salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# Fungsi DeleteData
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku) or indeks < 0:
        print("ID salah")
    else:
        buku.pop(indeks)

# Fungsi ShowMenu
def show_menu():
    print("\n======Menu=====")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = int(input("Pilih Menu : "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Input yang Anda masukkan salah")

if __name__ == "__main__":
    while True:
        show_menu()
