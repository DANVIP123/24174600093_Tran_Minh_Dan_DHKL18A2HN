n = int(input("Nhập một số: "))
def f(n):
  """Kiểm tra xem một số có phải là số nguyên tố hay không.

  Args:
    num: Số cần kiểm tra.

  Returns:
    True nếu num là số nguyên tố, False nếu không.
  """

  # Các số nhỏ hơn 2 không phải là số nguyên tố
  if n <= 1:
    return False

  # Kiểm tra từ 2 đến căn bậc hai của num
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

if f(n):
  print(n, "là số nguyên tố")
else:
  print(n, "không phải là số nguyên tố")