# Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày

mm = int(input("Nhap thang: " + " "))
yy = int(input("Nhap nam: " + " " ))
if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 10 or mm == 12:
    dd = 31
elif mm == 4 or mm == 6 or mm == 8 or mm == 9 or mm == 11:
    dd = 30
else: 
    if yy % 4 == 0:
        dd = 29
    else:
        dd = 28
print("Thang" + " " + str(mm) + " " + "nam" + " " + str(yy) + " co so ngay la:", dd)