chuoi = input("Nhap vao chuoi 3 so nguyen: ")
a = chuoi.find(",")
b = chuoi.rfind(",")
so1 = int(chuoi[:a])
so2 = int(chuoi[a+1:b])
so3 = int(chuoi[b+1:])
tong = so1 + so2 + so3
print (tong)
