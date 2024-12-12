def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(is_integer("13899"))  
print(is_integer("-7"))  
print(is_integer("1.8767"))