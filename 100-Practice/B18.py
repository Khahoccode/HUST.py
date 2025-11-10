# Giải và biện luận phương trình ax + b = 0
a = float(input("Nhap a: " + " "))
b = float(input("Nhap b: " + " "))
if a == 0 and b == 0:
    print("Phuong trinh co VSN")
if b != 0:
    print("Phuong trinh VN")
if a != 0: 
    x = -b/a
    print("Phuong trinh co nghiem: " + " " + str(x) )
