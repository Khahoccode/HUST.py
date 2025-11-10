#Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, 
# nếu có thì in ra True, ngược lại in ra False
import math
a = float(input("Nhap vao so a: " + " "))
b = round(math.sqrt(a))

print(math.sqrt(a) == b)