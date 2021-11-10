#deklarsi dan inisialisasi
pelanggan = "Budi Santoso"
totalBelanja = 150000

#stuktur kendali if
if(totalBelanja > 100000):
    keterangan = "Selamat Anda Mendapat Hadiah"
else:
    keterangan = "Terima Kasih Sudah Berbelanja"

#cetak data
print("Pelanggan",pelanggan,
"\nTotal Belanja Anda Rp.",totalBelanja,
"\n",keterangan)