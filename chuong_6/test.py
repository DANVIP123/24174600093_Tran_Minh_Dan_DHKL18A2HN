import math
n = int(input("nhap so nguyen duong n:"))
k = 1
tich = 1
tong = 0
for i in range(1,n+1):
    for k in range(1,k+1):
        
        if k >=1:
    
          tich = tich*i
          continue
        
        else:
            print("ket thuc chuong trinh")
    tong = (tich*i)+1   
print(f"ket qua la:{tong}")     

    
    
    
 