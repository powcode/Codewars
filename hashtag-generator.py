def generate_hashtag(s):
    print(len(s))
    if s == ""  :
        return False
    
    s_arr = s.split()
    to_capital = [word.capitalize() for word in s_arr]
    
    hashtag =  "#" + "".join(to_capital)
    if len(hashtag) > 140 :
        return False
    
    return hashtag



