todo_list = []

def tambah_tugas():
    tugas = input("Masukkan tugas: ")

    data = {
        "nama":tugas,
        "selesai": False
    }

    todo_list.append(data)
    print("Tugas berhasil ditambahkan!")

def lihat_tugas():
    if len(todo_list) == 0:
        print("Belum ada tugas.")
    else:
        print("\n===== DAFTAR TUGAS =====")

        for i in range(len(todo_list)):
            status = "✓" if todo_list[i]["selesai"] else "x"

            print(f"{i + 1}. {todo_list[i]['nama']} ({status})")


def hapus_tugas():
    lihat_tugas()

    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))

    if nomor <= len(todo_list):
        todo_list.pop(nomor - 1)
        print("Tugas berhasil dihapus!")
    else:
        print("Nomor tidak valid!")


def tandai_selesai():
    lihat_tugas()

    nomor = int(input("Masukkan nomor tugas yang selesai: "))

    if nomor <= len(todo_list):
        todo_list[nomor - 1]["selesai"] = True
        print("Tugas selesai!")
    else:
        print("Nomor tidak valid!")


while True:
    print("\n===== TO DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Selesai")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        hapus_tugas()

    elif pilihan == "4":
        tandai_selesai()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak ada!")