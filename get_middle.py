def get_middle(s):
    if len(s) %2 == 1:
         
        return s[int(len(str)/2)]
    else :
        char = int(len(s)/2)
        return "".join([s[char-1], s[char]])

stri = "testing"
print("uhuy",get_middle(stri))


if len(stri) % 2 ==1 :
    char = int(len(stri)/2)
    print(stri[char])
else :
    char = int(len(stri)/2)
    anjay = stri[char-1], stri[char]
    print(anjay)
    print("".join(anjay))