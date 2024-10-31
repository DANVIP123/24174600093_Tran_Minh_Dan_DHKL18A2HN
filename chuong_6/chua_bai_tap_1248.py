#Bài 1:
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nhap vao chieu cao: "))
pi = 3.14
dtxq = 2*pi*r*h
dttp = dtxq + 2*pi*r**2
print(f"Dien tich xung quanh: {dtxq:.2f}")
print(f"Dien tich toan phan: {dttp:.2f}")

#Bài 2:
x = float(input("Nhap gia tri cua x: "))
f_x = (-x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7))
print(f"Gia tri cua f(x) = {f_x:.2f}")

#Bài 4:
t = int(input("Nhap thoi gian su dung bong den (s): "))
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
cong_suat = t*hieu_dien_the*cuong_do_dong_dien/3600*1000
tien_phai_tra = cong_suat * 7000
print(f"Tien dien phai tra: {tien_phai_tra}")

#Bài 8
import math
x = input("Nhap gia tri x: ")
x = float(x)
f_x = math.log(x, 4) + math.log(2, x)
print(f"Gia tri can tim f(x) = {f_x:.2f}")