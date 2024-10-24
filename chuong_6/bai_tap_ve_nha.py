
#b1 nhập h và r
#b2 xét điều kiện h và r 
   # nếu h > 0 hoặc r > 0 đúng 
     #chuyển sang b3
   # nếu  sai  chuyển sabg b6
#b3 pi = 3.14
#b4 tính dtxq dttp
#b5 in ra kết quả  dtxq dttp 
# b6 kết thúc 

import math
h = float(input("nhap vao chieu cao"))
r = float(input("nhap vao ban kinh"))
if r <0 or h <0:
    print("gia tri cua ban kinh va chieu cao phai la so duong")
    
else:
    pi = 3.14
    sxq = 2 * pi * r * h
    stp = sxq + ( 2 * pi * r**2)
    the_tich = pi * (r**2) * h
    
    print(f"dien tich xung quanh la: {sxq:.2f}")
    print(f"dien tich toan phan la: {stp:.2f}")
    print(f"the tich hinh tru la:{the_tich:.2f}")
    
    
#bai 8
import math
x = float(input("nhap gia tri cua x "))
x = float(x)
if x <0 or x == 1:
  print("ham so khong thoa man dieu kien cua ham log")
  
else:
  f_x = math.log(x, 4) + math.log(2, x)
  
  print(f" gia tri can tim f(x):{f_x:.2f}")
  
  
  
  
#bai 4
import math
t = float(input("nhap thoi gian su dung bong den(giay)vao"))
if t >0:

 hieu_dien_the = 220
 cuong_do_dong_dien = 2.7
 cong_suat = t*hieu_dien_the*cuong_do_dong_dien/(3600*1000)
 so_tien_phai_tra = cong_suat*7000
 print(f"so tien phai tra la:{so_tien_phai_tra:.2f}")
 
else:
  print("thoi gian su dung cua bong den phai lon 0")
  


    
 
