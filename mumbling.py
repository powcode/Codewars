def accum(st):
    
    return "-".join([(st[i]*(i+1)).capitalize() for i in range(len(st))])
print(accum("aDcd"))    