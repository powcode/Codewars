def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    
    if array1 == [] or array2 == []:
        return False
   
    array1 = sorted([n**2 for n in array1])
    array2 = sorted(array2)
  
    
    
    
    if array1 == array2 :
        return True
    else :
        return False
    
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) #True