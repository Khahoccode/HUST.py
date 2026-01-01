chuoi = input("Nhap vao chuoi: ")
demhoa = demthuong = demso = 0

for i in chuoi:
    if i.isupper():
        demhoa += 1
    elif i.islower():
        demthuong += 1
    elif i.isnumeric():
        demso += 1
print("So ky tu in hoa: ", demhoa)
print("So ky tu in thuong: ", demthuong)
print("So ky tu la so: ", demso)

    