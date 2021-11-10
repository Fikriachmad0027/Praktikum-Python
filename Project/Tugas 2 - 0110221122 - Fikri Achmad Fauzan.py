print("-------------Tugas 2 DDP Fikri Achmad Fauzan-------------")
Nama_Pelanggan = str(input("Masukkan Nama Pelanggan\t: "))
Produk_Pilihan = input("Produk Pilihan\t\t: ")

if (Produk_Pilihan == "Kipas Angin"):
    harga = 1000000
    print("Harga Produk\t\t: %i" % (harga))

elif (Produk_Pilihan == "TV"):
    harga = 2000000
    print("Harga Produk\t\t: %i" % (harga))

elif (Produk_Pilihan == "Mesin Cuci"):
    harga = 3000000
    print("Harga Produk\t\t: %i" % (harga))

elif (Produk_Pilihan == "AC"):
    harga = 4000000
    print("Harga Produk\t\t: %i" % (harga))

else:
    (Produk_Pilihan == "Kulkas")
    harga = 5000000
    print("Harga Produk\t\t: %i" % (harga))

Jumlah_Barang = int(input("Jumlah Barang\t\t: "))
Harga_Kotor = harga * Jumlah_Barang
print("Harga Kotor\t\t: %i" % (Harga_Kotor))

if (Produk_Pilihan == "Kulkas" and Jumlah_Barang >= 5):
    dsc = 0.20 * Harga_Kotor
elif (Produk_Pilihan == "AC" and Jumlah_Barang >= 3):
    dsc = 0.10 * Harga_Kotor
else:
    dsc = 0.05 * Harga_Kotor

pajak = Harga_Kotor - dsc * 0.10
print("PPN\t\t\t: %i" % (pajak))

Harga_Bersih = Harga_Kotor - dsc + pajak
print("Harga Bersih\t\t: %i" % (Harga_Bersih))
