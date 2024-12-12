def phan_tich_thua_so_nguyen_to(n):
    danh_sach_thua_so = []  # Khởi tạo danh sách chứa các thừa số nguyên tố
    so = 2  # Khởi tạo số nguyên tố đầu tiên
    while n > 1:
        while n % so == 0:  # Kiểm tra xem 'so' có phải là thừa số của 'n' không
            danh_sach_thua_so.append(so)  # Thêm thừa số 'so' vào danh sách
            n //= so  # Chia n cho 'so' để tiếp tục phân tích
        so += 1  # Tăng giá trị 'so' để kiểm tra các số nguyên tố tiếp theo
    return danh_sach_thua_so

# Ví dụ sử dụng
so = 56
thua_so = phan_tich_thua_so_nguyen_to(so)
print(f"Thừa số nguyên tố của {so} là: {thua_so}")