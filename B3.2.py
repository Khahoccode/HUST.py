#Viết chương trình nhập vào mảng số nguyên gồm n phần tử, sau đó sắp xếp mảng theo thứ tự 
# #tăng dần và xuất ra màn hình
n = int(input("Moi nhap so phan tu cua mang: "))
a = []
for i in range(n):
    a.append(int(input("Phan tu thu %d: "%(i+1))))
for i in range (len(a)):
    for j in range (i):
        if a[i] < a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
for i in range (n):
    print(a[i], " ",end ="")