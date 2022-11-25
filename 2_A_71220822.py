total = int(input("Total belanja :Rp."))
if(total<100000):
    print(f"Tidak ada diskon! Maka yang Anda bayarkan adalah: Rp. {total}")
elif(total>=1000000):
    diskon = (total - (total*10/100))
    print(f"Biaya yang harus dibayar setelah diskon adalah: Rp. {diskon}")
elif(total>=500000):
    diskon = (total - (total*5/100))
    print(f"Biaya yang harus dibayar setelah diskon adalah: Rp. {diskon}")
elif(total>=100000):
    diskon = (total - (total*2/100))
    print(f"Biaya yang harus dibayar setelah diskon adalah: Rp. {diskon}")
