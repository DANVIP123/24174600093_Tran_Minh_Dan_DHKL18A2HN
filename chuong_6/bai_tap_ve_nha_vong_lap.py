#bai 1
for i in range(1, 100, 2):
    print(i)
    
#bai 2
n = int(input("Nhập giá trị n: "))
S1 = 0
for i in range(1, n+1):
    S1 += i
print("S1 =", S1)

# bai 3
def fibonacci(n):
#dieu kien cua fibonacci 
  if n <= 0:
    print("Incorrect input")
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2) 
for i in range(1, 51):
  print(fibonacci(i))

# bài 4
import math
n = int(input("Nhập một số nguyên dương n: "))
if n <= 1:
    print(n,"không phải số nguyên tố.")
if n <= 3:
    print(n,"là số nguyên tố.")
if n % 2 == 0 or n % 3 == 0:
    print(n, "không phải là số nguyên tố.")
i = 5
while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
        print(n, "không phải số nguyên tố")
    i += 6
print(n, "là số nguyên tố")
      
# bài 5
import math 
n = int(input("nhập 1 số vào đây: "))
k = 0
for i in range(1, n):
    if n % i == 0:
        k += 1
if k == n:
    print(n, "là số hoàn hảo.")
else:
    print(n, "không phải là số hoàn hảo.")

# bài 6
import math
n = int(input("nhập số nguyên dương n:"))
k = math.sqrt(n)
if int(k) ** 2 == n:
    print(n, "là số chính phương.")
else:
    print(n, "không phải là số chính phương.")    



# bài 8
n = int(input("Nhập một số nguyên dương: ")) 

so_hoan_hao = []
for n in range(1, n):
    k = 0
    for i in range(1, n):
      if n % i == 0:
        k += i
    if k == n:
     so_hoan_hao.append(n)

    print("Các số hoàn hảo nhỏ hơn", n, "là:", so_hoan_hao)

# bài 9
#bai 9
import math
n = int(input("Nhập một số nguyên dương: "))

for i in range(1, int(math.sqrt(n)) + 1):
    k = i * i
    if k < n:
      print(k, end=" ")


#bài 10
# bài 10
import math
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
while b != 0:
    a, b = b, a % b
print("Ước chung lớn nhất là:", a)

# bài 13 
import math

n = int(input("Nhập số cần phân tích: "))
i = 2
while n > 1:
    while n % i == 0:
        print(i, end=" * ")
        n //= i
    i += 1
print(f"là thừa số cần tìm : ", end=" * ")        
        
        
#bài 14
import math
n = int(input("Nhập số hàng của tam giác Pascal: "))
for i in range(n):
    C = 1
    for j in range(i+1):
      print(C, end=" ")
      C = C * (i - j) // (j + 1)
    print("")


import math
n = int(input("Nhập số hàng của tam giác Floyd: "))
k = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(k, end=" ")
        k += 1
    print(" ")    
    
# bài 7
# bài 7
import math
n = int(input("Nhập vào số nguyên dương n: "))
for n in range(2, n):
    c = 0
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        c += 1
        break
    if c == 0:
      print(n)

# bài 11
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
bcnn = max(a, b)
while True:
    if bcnn % a == 0 and bcnn % b == 0:
        break
    bcnn += 1

print("Bội chung nhỏ nhất là:", bcnn)


# bài 12
import math
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

# Tìm UCLN của phân số đã cho
ucln = mau_so
while tu_so % ucln != 0 or mau_so % ucln != 0:
    ucln -= 1

#phân số tối  giản
tu_so //= ucln
mau_so //= ucln

print(f"Phân số tối giản là: {tu_so}/{mau_so}")

# bài 15
import math
def dec_to_bin():# chuyển từ hệ 10 sang hệ 2
  num = int(input("Nhập số thập phân: "))
  res = ""
  while num > 0:
    res = str(num % 2) + res
    num //= 2
  print("Số nhị phân là:", res)

def bin_to_dec():# chuyển từ hệ 2 sang hệ 10
  num_str = input("Nhập số nhị phân: ")
  res = 0
  for i in range(len(num_str)):
    res += int(num_str[i]) * 2**(len(num_str) - i - 1)
  print("Số thập phân là:", res)
# Chọn kiểu chuyển đổi
choice = input("Chọn kiểu chuyển đổi (1: 10 -> 2, 2: 2 -> 10): ")

if choice == '1':
  dec_to_bin()
elif choice == '2':
  bin_to_dec()
else:
  print("Lựa chọn không hợp lệ")

