def find_outlier(integers):
    odd = 0
    even =0 
    for i in integers : 
        if i % 2 == 0 :
            even += 1
        else :
            odd += 1
    if odd > even :
        for i in integers :
            if i % 2 == 0:
                return i
    if odd < even :
        for i in integers :
            if i % 2 == 1:
                return i
angka = [2, 4, 6, 8, 10, 3]
print(find_outlier(angka))
print(angka.count(2))
