#in dãy số các số lẻ nhỏ hơn n
n = int(input("nhập vào các số nguyên dương"))
for i in range(n): #-> chuỗi chạy từ 0 đến n-1
    if i%2 == 1:
        print(i)
        
#in ra các số fibonacci
a = 0
b = 1
n = int(input("nhập vào các số nguyên dương n:"))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b
    
# tính tổng các số hạng từ 1 đến n

# s = 1 + 2 +3 +...+n
# nhập vào số n , tinh tổng n số hạng dựa theo S
# S 1 - 1/2 + 1/3 - 1/4 + 1/5 - ....
# 1/1 + (-1)* 1/2 + (1)*1/3 - (-1)*1/4 +....
#((-1)**n)*(1/n)
#E((-1)**n)*(1/n))
tong_s = 0
n = int(input("nhập giá trị nguyên dương n:"))
for i in range(n+1):
    tong_s = tong_s + i
    print(f"tong_s lan lap {i} = {tong_s}")
print(f"tong cac so tu 1 den n {tong_s}")
# tính giai thừa của số n (n!)
tich_p = 1
n = int(input("nhập giá trị nguyên dương n:"))
for i in range(n+1):
    if i == 0:
        continue
    tich_p = tich_p*i
print(f"tich giai thừa của số n {tich_p}")


# nhập 2 số a,b tìm ước chung lớn nhất của 2 số này
a = int(input(" nhap vào so nguyen duong a:"))
b = int(input(" nhap vào so nguyen duong b:"))
so_nho_nhat = a
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
        break
    k = k - 1
    

# kiểm tra số n có phải số nguyên tố hay không
# số nguyên tố là số nguyên dương lớn hơn 1 và chỉ chia hết cho nó và 1


n = int(input("nhap vao so nguyen duong can kiem tra:"))
if n <= 1:
    print("so nay khong phai la so nguyen to")
    
else:
    k = n
    for i in range(n):
        if n % k == 0 and k !=n and k != 1:
            print("so nay khong phai la so nguyen to")
            break
        k = k - 1
    else:
        print("day la so nguyen to")
        
            