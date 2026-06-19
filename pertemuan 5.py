# index 0(-4)       1(-3)    2(-2)    3(-1)
nama = ["tiara", "amrina", "ratin", "noer",]
dosen= ["edy", "jarir", "iman", "fuad", "indri"]
# mengambil data dari list:
data_pertama = nama[-2]
print(f"data terakhir : {data_pertama}")

#  mengambil data terkhir
data_terakhir = nama[-1]
print(f"data terakhir : {data_terakhir}")

# menambahkan data :
# nama.insert(posisi,item)
nama.insert (1,"dika")
print(f"data setelah ditambah : {nama}")

#menambah data di paling akhir
# nama.insert/append(-1,"zulfikar")
nama.append ("zulfikar")
print(f"data setelah ditambah di akhir : {nama}")


# menggabungkan list 
nama.extend(dosen)
print(f"data list gabungan : {nama}")

# menggabungkan nama dosen di tengah-tengah
nama[2:2] = dosen 
print(f"data list gabung dosen di tengah : \n{nama}")

# merubah data
nama[0] = "up to you"
print(f"data yang telah di edit : {nama}")

# menghapus data
nama.extend("iman")
print(f"data yang telah di hapus : \n{nama}")

# menghapus data paling akhir
nama.pop()
print(f"data paling akhir di hapus : \n{nama}")