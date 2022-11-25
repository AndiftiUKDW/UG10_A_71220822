soal1= int(input("Masukan nilai soal 1: "))
soal2= int(input("Masukan nilai soal 2: "))
soal3= int(input("Masukan nilai soal 3: "))
umur = int(input("Masukan umur Anda: "))

nilai = (soal1*50/100)+(soal2*30/100)+(soal3*20/100)
print(f"Rata-rata nilai Anda: {nilai}")
if(umur<=25 and nilai>=80):
    print("Selamat anda lulus!")
elif(umur>25 and nilai>=90):
    print("Selamat anda lulus!")
else:
    print("Coba lagi tahun depan!")