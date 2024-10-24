import math
x = input("nhap gia tri x:")
x = float(x)
f_x = math.log(x, 4) + math.log(2, x)
print(f"gia tri can tim f(x) = {f_x:.2f}")


#bai 1()
#ban kinh = r
#chieu cao = h
#dtxq 2*pi*r*h
#dttp = dtxq + 2*pi*r**2
r = float(input("nhap vao ban kinh"))
h = float(input("nhap vao chieu cao"))
if h>0 and r > 0:
pi = 3.14
dtxq = 2 * pi * r * h
dttp = dtxq + 2 * pi * r ** 2
print(f"dien tich xung quanh: {dtxq:.2f}")
print(f"dien tich toan phan: {dttp:.2f}")

#b1 nhập h và r
#b2 xét điều kiện h và r 
   # nếu h > 0 hoặc r > 0 đúng 
     #chuyển sang b3
   # nếu  sai  chuyển sabg b6
#b3 pi = 3.14
#b4 tính dtxq dttp
#b5 in ra kết quả  dtxq dttp 
# b6 kết thúc 









#bai 2
#tu so = -x + (x**2 + 4)**(1/2)
#mau so = (x**4 + 1)**(1/7)
#f_x = ( -x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7))
x = float(input("nhap gia tri cua x:"))
f_x = (( -x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7)))
print(f"gia tri cua f(x) = {f_x:.2f}")


#bai 4
# hieu-dien_the = 220
# cuong_do_dong_dien = 2.7
# cong_suat = hieu_dien_the*cuong_do_dong_dien/(3600*1000)
#tien_phai_tra = cong_suat * 7000

t = float(input("nhap thoi gia su dung bong den(S)"))

# cau lenh dieu kien 
# 3 kieu viet cau lenh diều kiện 
# câu lệnh if ..( sử dụng 1 điều kiện để xét)
# câu lệnh if ... else..(sử dụng 1 điều kiện để xét và có điều kiện khác)
# câu lệnh if ....else ...else (sử dụng mhieeuf điều kiện còn xét)

# xử lý xoay quanh bôlean (true false)
1 > 2
1 < 2

1 <= 2
1 == 2
1 != 2
"abc" == "123"
#=> trả về kết quả true hoặc false
# đói với if thì xét điều kiện 
# - nếu điều kiện đúng (true) thì câu lệnh if sẽ hoạt động 
# - nếu điều kiện sai (false) thì câu lệnh if sẽ bị bỏ qua
a = 10
if a > 5:
    print("gia tri a thoa man dieu kien")
    b = a + 1
    
print("ket thuc chuong trinh")