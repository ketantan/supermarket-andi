from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Transaksi:
    cart = [["item", "jumlah item", "harga/item", "harga total"]]
    
    '''
    function untuk mengecek isi keranjang belanja.
    '''
    def check_order(self):
        print("--- isi keranjang anda " + "-" * 37)
        print(tabulate(self.cart, headers = "firstrow", tablefmt = "fancy_grid"))
        print("-" * 60 + "\n")

    '''
    function untuk mengisi keranjang belanja dengan mencantumkan...
    (1) nama barang, (2) jumlah yang ingin dibeli, dan (3) harga per barang...
    total harga barang akan dikalkulasikan secara otomatis.
    '''
    def add_item(self, nama_item, jumlah_item, harga_item):        
        try:
            int(jumlah_item)
            int(harga_item)
        except:
            print("input jumlah barang dan harga per barang harus berupa angka.")
        else:
            if jumlah_item < 0 or harga_item < 0:
                print("input jumlah barang dan harga per barang harus lebih besar dari 0.")
            else:
                total_harga = jumlah_item * harga_item
                self.cart.append([nama_item, jumlah_item, harga_item, total_harga])
                print(f"{nama_item} sejumlah {jumlah_item} dimasukkan ke keranjang.")
                self.check_order()

    '''
    function untuk menghapus salah satu barang di dalam keranjang belanja.
    '''
    def delete_item(self, nama_item):
        found = False
        for row in self.cart:
            if nama_item in row:
                self.cart.pop(self.cart.index(row))
                print(f"{nama_item} dikeluarkan dari keranjang.")
                self.check_order()
                found = True
            
        if found == False:
            print("barang yang ingin dihapus tidak ditemukan di dalam keranjang.")
        
    '''
    function untuk menghapus seluruh isi keranjang belanja.
    '''
    def reset_transaction(self):
        self.cart.clear()
        self.cart.append(["item", "jumlah item", "harga/item", "harga total"])
        print("keranjang dikosongkan.")
        self.check_order()
    
    '''
    function untuk mengecek total belanja di dalam keranjang.
    pelanggan berhak mendapatkan diskon 5%, 8%, dan 10% jika berbelanja lebih dari 200,000, 300,000, dan 500,000.
    '''
    def total_price(self):
        total = 0
        for i in range (1, len(self.cart)):
            total = total + self.cart[i][3]
        
        if total > 500_000:
            self.check_order()
            print(f"total belanja adalah Rp. {total}.")
            print("_" * 60)
            print(f"total belanja di atas Rp. 500,000. anda berhak mendapatkan diskon 10%!")
            print(f"potongan harga: {total * 0.1}")
            print("_" * 60)
            print(f"total belanja menjadi Rp. {total * 0.9}.")
        elif total > 300_000:
            self.check_order()
            print(f"total belanja adalah Rp. {total}.")
            print("_" * 60)
            print(f"total belanja di atas Rp. 300,000. anda berhak mendapatkan diskon 8%!")
            print(f"potongan harga: {total * 0.08}")
            print("_" * 60)
            print(f"total belanja menjadi Rp. {total * 0.92}.")
        elif total > 200_000:
            self.check_order()
            print(f"total belanja adalah Rp. {total}.")
            print("_" * 60)
            print(f"total belanja di atas Rp. 200,000. anda berhak mendapatkan diskon 5%!")
            print(f"potongan harga: {total * 0.05}")
            print("_" * 60)
            print(f"total belanja menjadi Rp. {total * 0.95}.")
        else:
            self.check_order()
            print(f"total belanja adalah Rp. {total}.")
    
    '''
    function untuk mengubah nama barang di dalam keranjang.
    '''
    def update_item_name(self, nama_item, update_nama_item):
        found = False
        for row in self.cart:
            if nama_item in row:
                self.cart[self.cart.index(row)][0] = update_nama_item
                print(f"{nama_item} diganti dengan {update_nama_item}")
                self.check_order()
                found = True
        
        if found == False:
            print("barang yang ingin diganti tidak ditemukan di dalam keranjang.")
    
    '''
    function untuk mengubah jumlah yang ingin dibeli dari sebuah barang di dalam keranjang.
    '''
    def update_item_qty(self, nama_item, update_item_qty):
        try:
            int(update_item_qty)
        except:
            print("input jumlah barang harus berupa angka.")
        else:
            if update_item_qty < 0:
                print("input jumlah barang harus lebih besar dari 0.")
            else:
                found = False
                for row in self.cart:
                    if nama_item in row:
                        self.cart[self.cart.index(row)][1] = update_item_qty
                        print(f"jumlah {nama_item} diubah menjadi {update_item_qty}")
                        self.check_order()
                        found = True

                if found == False:
                    print("barang yang ingin diganti tidak ditemukan di dalam keranjang.")
    
    '''
    function untuk mengubah harga satuan dari sebuah barang di dalam keranjang.
    '''
    def update_item_price(self, nama_item, update_item_price):
        try:
            int(update_item_qty)
        except:
            print("input jumlah barang harus berupa angka.")
        else:
            if update_item_qty < 0:
                print("input jumlah barang harus lebih besar dari 0.")
            else:
                found = False
                for row in self.cart:
                    if nama_item in row:
                        self.cart[self.cart.index(row)][2] = update_item_price
                        print(f"harga {nama_item} diubah menjadi {update_item_price}")
                        self.check_order()
                        found = True

                if found == False:
                    print("barang yang ingin diganti tidak ditemukan di dalam keranjang.")