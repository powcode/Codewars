def likes(names):
    count = 0
    if len(names) == 0 :
        return f"no one likes this"
    if len(names) == 1 :
        return f"{names[0]} like this"
    if len(names) == 2  :
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3  :
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    
    for i in range(len(names)) :
        count += 1
        names.pop()
        if len(names) == 2 :
            break
        
    return f"{names[0]}, {names[1]} and {count} others like this"
        

anjay = ["Dimas", "Anjay", "Mabar"]
print(likes(anjay))