nama = input("Masukan nama mahasiswa :")
nim = str(input("Masukan NIM-nya : "))
prodi = str(nim[0]+nim[1])
angkatan = int(nim[2]+nim[3])
if(prodi=="71"):
    if(angkatan >= 20 and angkatan <= 22):
        print(f"{nama} merupakan mahasiswa informatika angkatan 20 hingga 22")
    else:
            print(f"{nama} bukan mahasiswa informatika angkatan 20 hingga 22")
else:
    print(f"{nama} bukan mahasiswa informatika angkatan 20 hingga 22")
    