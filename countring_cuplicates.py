def duplicate_count(text):
    count = 0
    
    for i in text :
        
        if text.count(i.lower()) > 1 :
            count += 1
            text = text.replace(i, "")
    return count

text = "anjay"
text.replace("a", "")
print(text)
