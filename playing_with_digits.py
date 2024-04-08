def dig_pow(n, p):
    n = str(n)
    x = 0
    for i in range(len(n)) :
        x += int(n[i])**(p+i)
    
    p = int(x/int(n))
    if x == int(n) * p :
        return p
    else : 
        return -1
     
    

print(dig_pow(92, 1))

