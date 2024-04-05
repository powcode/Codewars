import math
def is_square(n):
    if n < 0 : return False
    if math.sqrt(n) == int(math.sqrt(n)) : return True
    else : return False

print(is_square(0))