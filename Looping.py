while True:
    print("=== MENU SEDERHANA ===")
    print("1. Tampilkan 10 bilangan pertama")
    print("2. Tampilkan bilangan genap 1-20")
    print("3. Hitung jumlah 1-100")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("10 bilangan pertama:")
        for i in range(1, 11):
            print(i, end=" ")
        print("\n")

    elif pilihan == "2":
        print("Bilangan genap 1-20:")
        for i in range(2, 21, 2):
            print(i, end=" ")
        print("\n")

    elif pilihan == "3":
        total = sum(range(1, 101))
        print("Jumlah 1-100 adalah:", total)
        print()

    elif pilihan == "4":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!\n")
