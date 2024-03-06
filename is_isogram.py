def is_isogram(string):
    
    string = [i for i in string.lower()]
    isogram =  set(string)
    
    if len(string) == len(isogram):
        return True
    else :
        return False

