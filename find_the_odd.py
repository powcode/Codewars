def find_it(seq):
    for i in seq :
        count = 0 
        print(seq.count(i))
        count = seq.count(i)
        if count % 2 == 1 :
            return i
        

anjay = [1,1,1,1,1,1,10,1,1,1,1]

print(find_it(anjay))
    