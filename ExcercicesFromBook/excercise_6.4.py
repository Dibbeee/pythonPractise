

def is_power(a, b):
    if a == b:
        return True
    elif a%b == 0:
        return is_power(a/b, b)
    else:
        return False
    
print(is_power(10, 2))
print(is_power(2, 2))
print(is_power(20, 5))
print(is_power(100, 8))