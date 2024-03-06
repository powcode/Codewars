def descending_order(num):
    
    num_arr = [char for char in str(num)]
    
    num = sorted(num_arr, reverse=True)
    result = "".join([str(i) for i in num])
    result = int(result)
    
    
    return result


print(descending_order(123456789))

