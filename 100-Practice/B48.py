# Nhap vao chuoi, tinh tong cac ky tu so trong chuoi
chuoi = input("Nhap vao mot chuoi: ")
tong = 0
for i in chuoi:
    if i.isnumeric():
        tong += int(i)
print (tong)
