def f(s):
    """Kiểm tra chuỗi có phải là số nguyên dương không.

    Args:
        s: Chuỗi cần kiểm tra.

    Returns:
        True nếu s là số nguyên dương, False nếu không.
    """

    # Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ số không
    if not s.isdigit():
        return False

    # Kiểm tra xem chuỗi có khác rỗng và ký tự đầu tiên có phải là '0' không
    return s != '0'

# Ví dụ:
print(f("123"))  
print(f("-456"))  
print(f("3.14"))  
print(f("0"))  
print(f("abc")) 