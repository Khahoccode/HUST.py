a = float(input("Nhap so nguyen a la: "))
b = float(input("Nhap so nguyen b la: "))
c = float(input("Nhap so nguyen c la: "))
delta = b*b - 4*a*c

if delta < 0: print("Phuong trinh vo nghiem")
elif delta == 0: print("Phuong trinh co nghiem kep:" , -b/(2*a))
else: 
    import math
    print("phuong trinh co 2 nghiem phan biet")
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("x1 = ", 1 , "x2 = ", x2)