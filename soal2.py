print("========== PROGRAM PENGHITUNG PYTHAGORAS =========")
print ("")
bil1 = int(input("Masukan Bilangan Bulat Pertama >> "))
bil2 = int(input("Masukan Bilangan Bulat Kedua >> "))
bil3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
jumlah = ((bil1**2)+(bil2**2))
if jumlah == (bil3**2):
    print ("Merupakan Phytagoras")
else:
    print ("Bukan Merupakan Phytagoras")