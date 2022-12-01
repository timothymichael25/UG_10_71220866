print("Selamat datang di Program Pengurutan Bilangan")
print ("Silahkan Pilih Metode Yang Akan Dipakai")
print ("1. Ascending")
print ("2. Descending")
print ("")
p1 = int(input(">> "))
print ("")
if p1 == 1:
    print ("Urutan angka anda ", sorted(list1))
    option1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    option2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    option3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    option4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    list1 = [option1 , option2 , option3 , option4]
    print ("Urutan angka anda ", sorted(list1,reverse=True))
elif pil1 == 2:
    option1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    option2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    option3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    option4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    list1 = [option1 , option2 , option3 , option4]
    print ("Urutan angka anda ", sorted(list1,reverse=True))
else:
    print ("Input salah")