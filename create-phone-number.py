import re
def create_phone_number(n):
    toStr = [str(num) for num in n]
    toStr = "".join(toStr)
    pattern = re.compile(r"(\d{3})(\d{3})(\d{4})")
    groups = pattern.search(toStr)
    stringGroups = f"({groups[1]}) {groups[2]}-{groups[3]}"
    
    result = stringGroups
    
    return result

