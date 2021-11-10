nama = 'Ahmad'
agama = 'Islam'
gaji = 4000000
anak = 2
tunjanganJ = gaji * (20/100) 
if (anak <= 2): tunjanganK = gaji * (10/100)
elif (anak >=2): tunjanganK = gaji * (20/100)
else: anak = 0
gajik = gaji + tunjanganJ + tunjanganK
Zakat = (0, 0.025) [agama == 'Islam' and gajik >=6000000] *gajik
gajib = gajik - Zakat
print("\nSLIP GAJI PT. XYZ",
    "\n------------------",
    "\nNama Pegawai \t\t :",nama,
    "\nAgama \t\t\t :",agama,
    "\nJumlah anak \t\t :",anak,
    "\nGaji Pokok \t\t : Rp.",gaji,
    "\nTunjangan Jabatan \t : Rp.",tunjanganJ,
    "\nTunjangan Keluarga \t : Rp.",tunjanganK,
    "\nGaji Kotor \t\t : Rp.",gajik,
    "\nZakat Profesi\t\t : Rp.",Zakat,
    "\nTake Home Pay\t\t : Rp.",gajib)

nama = 'Alex'
agama = 'Kristen Protestan'
gaji = 6000000
anak = 5
tunjanganJ = gaji * (20/100) 
if (anak <= 2): tunjanganK = gaji * (10/100)
elif (anak >=2): tunjanganK = gaji * (20/100)
else: anak = 0
gajik = gaji + tunjanganJ + tunjanganK
Zakat = (0, 0.025) [agama == 'Islam' and gajik >=6000000] *gajik
gajib = gajik - Zakat
print("\nSLIP GAJI PT. XYZ",
    "\n------------------",
    "\nNama Pegawai \t\t :",nama,
    "\nAgama \t\t\t :",agama,
    "\nJumlah anak \t\t :",anak,
    "\nGaji Pokok \t\t : Rp.",gaji,
    "\nTunjangan Jabatan \t : Rp.",tunjanganJ,
    "\nTunjangan Keluarga \t : Rp.",tunjanganK,
    "\nGaji Kotor \t\t : Rp.",gajik,
    "\nZakat Profesi\t\t : Rp.",Zakat,
    "\nTake Home Pay\t\t : Rp.",gajib)