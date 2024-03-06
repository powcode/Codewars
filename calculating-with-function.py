
operators = {
    "+" : lambda x, y : int(x + y),
    "-" : lambda x, y : int(x - y),
    "*" : lambda x, y : int(x * y),
    "/" : lambda x, y : int(x / y),
}
def zero(operation = None): 
    if operation != None :
        return operators.get(operation[0])(0,operation[1])
    else : return 0
def one(operation = None): 
    if operation != None :
        return operators.get(operation[0])(1,operation[1])
    else : return 1
def two(operation = None): 
    if operation != None :
        return operators.get(operation[0])(2,operation[1])
    else : return 2
def three(operation = None):
    if operation != None :
        return operators.get(operation[0])(3,operation[1])
    else : return 3
def four(operation = None): 
    if operation != None :
        return operators.get(operation[0])(4,operation[1])
    else : return 4
def five(operation = None): 
    if operation != None :
        return operators.get(operation[0])(5,operation[1])
    else : return 5
def six(operation = None):
    if operation != None :
        return operators.get(operation[0])(6,operation[1])
    else : return 6
def seven(operation = None): 
    if operation != None :
        return operators.get(operation[0])(7,operation[1])
    else : return 7
def eight(operation = None): 
    if operation != None :
        return operators.get(operation[0])(8,operation[1])
    else : return 8
def nine(operation = None, *args): 
    if operation != None :
        return operators.get(operation[0])(9,operation[1])
    else : return 9
    
def plus(x): return ["+", x]
def minus(x): return ["-", x]
def times(x): return ["*", x]
def divided_by(x): return ["/", x]

print(eval("8" "*" "5") )