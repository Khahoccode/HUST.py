# kiem tra xem mat khau co manh hay khong
chuoi = input("Nhap vao mot chuoi: ")
ktsokytu = len(chuoi) > 6
ktinhoa = ktthuong = ktso = ktdb = False
for i in chuoi:
    if i.isnumeric():
        ktso = True
    elif i.islower():
        ktthuong = True
    elif i.isupper():
        ktinhoa = True
    else:
        ktdb = True
if ktinhoa and ktthuong and ktdb and ktso and ktsokytu:
    print("Manh thíaa")
else:
    print("yeu lam")
