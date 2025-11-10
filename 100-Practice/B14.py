# Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, 
# ngược lại in ra đây là số lẻ
a = int(input("Nhap vao so nguyen a: " + " "))
if a%2 == 0: 
    print(str(a) + " la mot so chan")
else:
    print(str(a) + " la mot so le")
