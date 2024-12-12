def la_so_nguyen_to(so):
    """
    Kiểm tra xem một số có phải là số nguyên tố không.
    """
    if so < 2:
        return False
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            return False
    return True

def tinh_trung_binh_so_nguyen_to(day_so):
    """
    Tính giá trị trung bình của một dãy số nguyên tố nếu tất cả các số đều là số nguyên tố.
    """
    # Kiểm tra tất cả các số có phải là số nguyên tố
    if not all(la_so_nguyen_to(so) for so in day_so):
        return "Dãy số không chỉ chứa số nguyên tố."

    # Tính giá trị trung bình
    return sum(day_so) / len(day_so)

# Ví dụ sử dụng
danh_sach_so = [2, 3, 5, 7, 11]
kq = tinh_trung_binh_so_nguyen_to(danh_sach_so)
print("Giá trị trung bình:", kq)