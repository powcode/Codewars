def solution(number):
    x= 0
    
    if number <= 3 :
        return 0
    for i in range(3, number, 1):
        if i % 3 == 0 or i % 5 == 0 :
            x += i
    return x
    
    
    
    
  


