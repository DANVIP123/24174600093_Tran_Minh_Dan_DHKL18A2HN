def is_float(s):
    """Kiểm tra xem một chuỗi có phải là số thực hay không.

    Args:
        s: Chuỗi cần kiểm tra.

    Returns:
        True nếu s là số thực, False nếu không.
    """

    try:
        float(s)
        return True
    except ValueError:
        return False

# Ví dụ sử dụng:
print(is_float("3.14"))  
print(is_float("-2.5")) 
print(is_float("123"))  
print(is_float("abc"))  
print(is_float("3.14abc"))  