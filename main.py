print("selamat datang di supermarket andi")
input("enter untuk memulai berbelanja")
transaksi1 = Transaksi()
print("\n")

pay = "n"
while pay == "n":
    print("--- menu " + "-" * 51)
    print("1. menambah item")
    print("2. menghapus item")
    print("3. menghapus semua isi keranjang")
    print("4. mengganti nama item")
    print("5. mengganti jumlah item")
    print("6. mengganti harga item")
    print("7. mengecek isi keranjang")
    print("8. menghitung total harga dan membayar\n")
    menu = 0

    while menu == 0:
        try:
            menu = int(input("apa yang ingin anda lakukan? "))
            print(" ")
        except:
            print("\n--- input tidak dikenal " + "-" * 36)
            print("input menu harus di antara 1-8.")
            print("-" * 60 + "\n")
        else:
            if menu < 1 or menu > 8:
                print("\n--- input tidak dikenal " + "-" * 36)
                print("input menu harus di antara 1-8.")
                print("-" * 60 + "\n")
                menu = 0

    if menu == 1:
        '''
        menu untuk menambah item baru yang ingin dibeli.
        membutuhkan input: (1) nama item; (2) jumlah item; (3) harga per piece
        '''
        isi = "y"
        while isi == "y":
            nama_item = input("masukkan nama item yang ingin dibeli: ")

            loop = True
            while loop == True:
                try:
                    jumlah_item = int(input("masukkan jumlah item yang ingin dibeli: "))
                except:
                    print("\n--- input tidak dikenal " + "-" * 36)
                    print("input jumlah harus berupa angka.")
                    print("-" * 60 + "\n")
                else:
                    loop = False

            loop = True
            while loop == True:
                try:
                    harga_item = int(input("masukkan harga per piece-nya: "))
                except:
                    print("\n--- input tidak dikenal " + "-" * 36)
                    print("input harga per piece harus berupa angka.")
                    print("-" * 60 + "\n")
                else:
                    loop = False

            print("")
            transaksi1.add_item(nama_item, jumlah_item, harga_item)

            loop = True
            while loop == True:
                isi = str(input("apakah masih ada item lain yang ingin dimasukkan? (y/n) "))
                print("")
                if isi != "y" and isi != "n":
                    print("\n--- input tidak dikenal " + "-" * 36)
                    print("input harus antara y atau n.")
                    print("-" * 60 + "\n")
                else:
                    loop = False

    elif menu == 2:
        '''
        menu untuk menghapus item yang sudah ada di dalam keranjang
        '''
        nama_item = input("masukkan nama item yang ingin dihapus: ")
        print("\n")
        transaksi1.delete_item(nama_item)

    elif menu == 3:
        '''
        menu untuk menghapus SEMUA item yang ada di dalam keranjang
        '''
        transaksi1.reset_transaction()

    elif menu == 4:
        '''
        menu untuk mengganti salah satu item yang ada di dalam keranjang dengan item baru
        '''
        nama_item = input("masukkan nama item yang ingin diganti: ")
        update_nama_item = input("masukkan nama item yang baru: ")
        transaksi1.update_item_name(nama_item, update_nama_item)

    elif menu == 5:
        '''
        menu untuk mengganti jumlah item yang ingin di beli dari dalam keranjang
        '''
        nama_item = input("masukkan nama item yang ingin diganti jumlahnya: ")

        loop = True
        while loop == True:
            try:
                update_item_qty = input("masukkan nama item yang baru: ")
            except:
                print("\n--- input tidak dikenal " + "-" * 36 + "\n")
                print("input jumlah harus berupa angka.\n")
                print("-" * 60 + "\n")
            else:
                loop = False

        transaksi1.update_item_qty(nama_item, update_item_qty)

    elif menu == 6:
        '''
        menu untuk mengganti harga per piece dari item yang ingin dibeli di dalam keranjang
        '''
        nama_item = input("masukkan nama item yang ingin diganti harga per piece-nya: ")

        loop = True
        while loop == True:
            try:
                update_item_price = input("masukkan harga per piece yang baru: ")
            except:
                print("\n--- input tidak dikenal " + "-" * 36 + "\n")
                print("input harga harus berupa angka.\n")
                print("-" * 60 + "\n")
            else:
                loop = False

        transaksi1.update_item_price(nama_item, update_item_price)

    elif menu == 7:
        '''
        menu untuk mengecek isi keranjang
        '''
        transaksi1.check_order()

    else:
        '''
        menu untuk mengecek isi keranjang dan menghitung total harga yang harus dibayarkan
        '''
        transaksi1.total_price()

        loop = True
        while loop == True:
            pay = input("apakah anda ingin membayar dan menyelesaikan transaksi? (y/n) ")
            if pay != "y" and pay != "n":
                print("\n--- input tidak dikenal " + "-" * 36 + "\n")
                print("input harus antara y atau n.\n")
                print("-" * 60 + "\n")
            else:
                loop = False

        if pay == "y":
            print("terima kasih telah berbelanja di supermarket andi.")
            print("sampai bertemu di lain kesempatan.")

