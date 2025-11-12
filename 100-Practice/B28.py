# Tính S = 1 + 2 + 3 + 4 + … + n

n = int(input("Nhap vao so nguyen n: " + " "))
S = 0
for i in range (1, n+1):
    S += i
print (S)