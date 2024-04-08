def duplicate_encode(word):
    word = [i.lower() for i in word]
    encode = []
    for i in word :
        if word.count(i) > 1 :
            encode.append(")")
        else :
            encode.append("(")
    return "".join(encode)

anjay = "Success"
print(duplicate_encode(anjay))

