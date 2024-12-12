import math


def f(n):
    """
    Kiểm tra xem một số có phải là số chính phương hay không.
    True nếu num là số chính phương, False nếu không.
    """
    if n < 0:
        return False
    k = int(math.sqrt(n))
    return k * k == n

# Ví dụ 
print(f(16))  
print(f(20))  