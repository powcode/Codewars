def to_underscore(string):
    if str(string).isdigit() == True :
        return str(string)
    string = [str(i) for i in string]
    temp = []
    arr = []
    n = ""
    for i in range(len(string)-1):
        if(string[i+1]).isupper() == True :
            n = "".join(temp)
            arr.append(n)
            temp = []
        temp.append(string[i+1])
        
        if i == len(string)-2:
            n = "".join(temp)
            arr.append(n)
    return (string[0] + "_".join(arr)).lower()
    
    
    
    
# print("App7Test".isdigit())

print(to_underscore("App7Test"))
print(to_underscore(1))