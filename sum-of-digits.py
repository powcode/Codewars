def digital_root(n):
    while(True):
        result = 0
        to_int = [x for x in str(n)]
        for n in to_int :
            result += int(n)
        n = result
        if len([x for x in str(n) ]) == 1 :
            return result
            break
        

    
print(digital_root(493193))
print(digital_root(942))


