#Giải và biện luận phương trình ax^2 + bx + c = 0
import math
a = float(input("Nhap a =" + " "))
b = float(input("Nhap b =" + " "))
c = float(input("Nhap c =" + " "))
print("Phuong trinh" + " " +str(a) + "x^2 +" + str(b) + "x +" + " " + str(c))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co VSN")  #0 1 2
        else:
            print("Phuong trinh VN") #0 0 1
    else:  
        print("Phuong trinh co nghiem: ", -c/b) #0 2 0
else: 
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet: ", x1, x2) #1 3 2
    elif delta == 0:
        x = -c/a
        print("Phuong trinh co nghiem kep: ", x) #1 2 1
    else:
        print("Phuong trinh VN") # 1 2 4
