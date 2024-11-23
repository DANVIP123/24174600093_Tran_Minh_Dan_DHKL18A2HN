# cau 1
chuoi = input("Nhập vào chuỗi ký tự: ")
danh_sach_tu = chuoi.split()
so_tu = len(danh_sach_tu)
print("Số lượng từ trong chuỗi là:", so_tu)
#cau 2
chuoi = input("Nhập vào chuỗi ký tự: ")
danh_sach_tu = chuoi.split()
chuoi_sau_khi_loai_bo = " ".join(danh_sach_tu)
print("Chuỗi sau khi loại bỏ dấu cách thừa là:", chuoi_sau_khi_loai_bo)

#cau 3
ho_ten = input("Nhập vào họ tên đầy đủ: ")
danh_sach_tu = ho_ten.split()
ho = danh_sach_tu[0]    
ten = danh_sach_tu[-1]  
print(f"Ho: {ho}, Ten: {ten}")

#cau 4

chuoi = input("Nhập vào chuỗi ký tự: ")
so_chu = 0
so_so = 0
so_ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.isalpha():  
        so_chu += 1
    elif ky_tu.isdigit():  
        so_so += 1
    else:  
        so_ky_tu_dac_biet += 1

print(f"Số ký tự là chữ: {so_chu}")
print(f"Số ký tự là số: {so_so}")
print(f"Số ký tự là ký tự đặc biệt: {so_ky_tu_dac_biet}")

#cau 5
chuoi = input("Nhập vào chuỗi ký tự: ")
so_chu_hoa = 0
so_chu_thuong = 0
for ky_tu in chuoi:
    if ky_tu.isupper(): 
        so_chu_hoa += 1
    elif ky_tu.islower():  
        so_chu_thuong += 1

print(f"Số chữ cái viết hoa: {so_chu_hoa}")
print(f"Số chữ cái viết thường: {so_chu_thuong}")

#cau6
chuoi = input("Nhập vào chuỗi ký tự: ")
if chuoi.startswith('-') and chuoi[1:].isdigit():
    print("Chuỗi là số âm.")
else:
    print("Chuỗi không phải là số âm.")
    
#cau 8

str_1 = input("Nhập vào xâu ký tự str_1: ")
str_2 = input("Nhập vào xâu ký tự str_2: ")

if str_2 in str_1:
    print(f"'{str_2}' có nằm trong '{str_1}'.")
else:
    print(f"'{str_2}' không nằm trong '{str_1}'.")

if str_1 in str_2:
    print(f"'{str_1}' có nằm trong '{str_2}'.")
else:
    print(f"'{str_1}' không nằm trong '{str_2}'.")


# cau9
chuoi = input("Nhập vào chuỗi nhị phân: ")

if all(ky_tu in '01' for ky_tu in chuoi):
    
    so_thap_phan = int(chuoi, 2)
    print(f"'{chuoi}' là số nhị phân, chuyển sang thập phân: {so_thap_phan}")
else:
    print("Chuỗi không phải là số nhị phân hợp lệ.")
    
#cau 10
