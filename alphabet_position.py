def alphabet_position(text):
    position = []
    text = "".join([i.lower() for i in text.split(" ")])
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # alphabet = [i for i in enumerate(alphabet, 1)]
    # alphabet = [i for i, _ in alphabet]
    for i in text :
        if i not in alphabet :
            continue
        position.append(alphabet.find(i)+1)
        
    
    return " ".join(map(str, position))
    
x =alphabet_position("The narwhal bacons at midnight.")
print(x)