import re
def to_camel_case(text) :
    words = re.split(r'[-_]', text)
    toUpper = [words[0]] + [word.capitalize() for word in words[1:]]  
    result = ''.join(toUpper)
    return result



