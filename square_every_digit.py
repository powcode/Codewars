def square_digits(num):
    
    return int("".join(map(str, [int(i)**2 for i in str(num) ])))

print(square_digits(9119))

