def array_diff(a, b):
    for i in range(len(a)-1, -1, -1) :
        if a[i] in b :
            a.remove(a[i])
    return a
        
                    
    



print(array_diff([1,2,2], [2]))