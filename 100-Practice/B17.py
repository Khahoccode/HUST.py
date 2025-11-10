# Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
a = float(input("Nhap so :" + " "))
b = float(input("Nhap so b: " + " "))
c = float(input("Nhap so c: " + " "))
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print(a,b,c)
    
