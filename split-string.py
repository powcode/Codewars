def solution(s):
    result = [s[i:i+2] for i in range(0, len(s), 2)]
    for i in result :
        last_index = len(result)-1
        last_value = len(result[last_index])
        
        
        if(last_value == 1) :
            result[last_index] = result[last_index] + "_" 
            
    return result

print(solution("asdfads"))

# print(len(seplit[2]))

