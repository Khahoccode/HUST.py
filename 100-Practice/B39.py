# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
n = int(input("Nhap vao so nguyen n: " + " "))
num_le = 0
num_chan = 0
h = n
while h > 0:
    a = h%10
    if a%2 != 0:
        num_le += 1
    else:
        num_chan += 1
    h = h//10
print(str(n) + " co " + str(num_chan) + " chu so chan")
print(str(n) + " co " + str(num_le) + " chu so le")