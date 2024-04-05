def high_and_low(numbers):
    return " ".join([str(i) for i in [max([int(n) for n in numbers.split(" ")]),min([int(n) for n in numbers.split(" ")])]])
    
    


anjay ="1 2 -3 4 5"
print(high_and_low(anjay))
# nums = [int(n) for n in anjay.split(" ")]
# high = [max(nums),min(nums)]
# highlow = [str(i) for i in high] 


# print(" ".join(highlow))