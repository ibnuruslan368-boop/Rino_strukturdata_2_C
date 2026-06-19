#NAMA:kevin christian alexander
#NIM:25241088
#KELAS:PTI c

# manipulasi pada list
angka = [1,2,3,4,1,2,3,4,9,8,7,6,9,8,7,6,5]
print(angka)

# menghitung jumlah
data_1 = angka.count(1)
print(f"jumlah data 1 : {data_1}")

# mengetahui posisi
nama = ["keke", "amrina", "fadel", "wisnu"]
pos_fadel = nama.index("fadel")
print(f"posisi index fadel : {pos_fadel}")

# mengurutkan data
print(f"angka pegel: \n{angka}")
angka.sort()
print(f"angka setelah diurutkan : \n{angka}")

angka.reverse()
print(f"angka setelah diurutkan dr terbesar : \n{angka}")