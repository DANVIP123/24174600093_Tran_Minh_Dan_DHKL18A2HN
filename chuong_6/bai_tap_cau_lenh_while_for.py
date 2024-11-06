# k = 10
# tong_l = 0
# for l in range(1 , k):
#     tong_l = tong_l + (l + 1)
    
    
    
# n = int(input(" nhap gia tri nguyen duong"))
# tong_n = 0 
# for k in range(1 , n + 1):
#     tong_l = 0
#     for l in range(l , k):
#         tong_l = tong_l + (l + 1)
    
#     tong_n = tong_n + (tong_l/k)
# print(f"ket qua: {tong_n}")    


k = 10 
# tong_k = 0
# for l in range(1,k+1):
#     tong_l = tong_l +(l + 1)
    
    
# giai_thua_k = 1
# for i in range(1, k+1):
#     giai_thua_k = giai_thua_k*i
    
n = int(input("nhap gia tri nguyen duong"))   
n = 10
tong_n = 0
for k in range(1 , n+ 1):
    tong_k = 0
    for l in range(1,k+1):
        tong_l = tong_l + (l + 1)
    giai_thua_k = 1
    for i in range(1, k+1):
        giai_thua_k = giai_thua_k*i
    tong_n = tong_l/giai_thua_k
print(f"ket qua: {tong_n}")