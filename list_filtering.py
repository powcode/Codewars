def filter_list(l):
    return [i for i in l if type(i) == int]


a = [1,2,'a','b']
print(filter_list(a))
