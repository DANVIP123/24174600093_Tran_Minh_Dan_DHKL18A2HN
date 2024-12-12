def f(n):
    """
    Hàm kiểm tra một số có phải là số hoàn hảo hay không.
        n (int): Số cần kiểm tra.
      True nếu n là số hoàn hảo, False nếu không.
    """
    if n <= 1:
        return False

    # Tìm tổng các ước của n (không bao gồm chính n)
    tong_cac_uoc  = 1  # 1 luôn là ước của mọi số
    for i in range(2, int(n**0.5) + 1):  # Chạy từ 2 đến căn bậc hai của n
        if n % i == 0:
            tong_cac_uoc += i
            if i != n // i:  # Nếu i và n//i khác nhau thì cộng cả hai
                tong_cac_uoc += n // i

    return tong_cac_uoc == n

# Ví dụ sử dụng
print(f(6))   
print(f(28))  
print(f(12))  