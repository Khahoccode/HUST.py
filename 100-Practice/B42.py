# Bai toan: Nhap A vao, in ra so lon nhat trong chuoi fibonacci ma be hon A
A =int(input("Nhap vao A:"))
a = 1 
b = 1
c = a + b
while c <= A:
    a = b
    b = c
    c = a + b
print(b)