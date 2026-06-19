#pengertian list

data1 = 1
data2 = 2
data3 = 3

#kumpulan angka 
angka = [1, 2, 3]
print (f"kumpulan data angka =\n{angka}")

string = ["durian", "apple", "orange"]
print (f"kumpulan data tulisan =\n{string}")

bolean = [True, False, True]
print (f"kumpulan data bolean =\n{bolean}")

cam = [3, 9, "durian", True, False]
print (f"kumpulan data campran =\n{cam}")

#cara alternatif membuat list 
data_range =range(0,10)
data_list = list(data_range)
print (f"data range:\n {data_list}")

#membuat list menggunakan for
list_for = [i**3 for i in range (0,10)]
print (f"data range pake for  : \n {list_for}")

#membuat list menggunakan for if
list_forif = [i for i in range (0,10)if i !=5]
print (f"data range pake for if : \n{list_forif}")

#membuat list menggunakan for
list_for = [i for i in range (0,10)if i%2 ==0]
print (f"data range pake for genap : \n{list_for}")

#membuat list menggunakan for
list_for = [i for i in range (0,10)if i%2 !=0]
print (f"data range pake for ganjil; : \n{list_for}")

hasil= 10%3
print(hasil)