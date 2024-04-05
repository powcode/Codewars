def to_jaden_case(string):
    return " ".join([i.capitalize() for i in string.split(" ")])

print(to_jaden_case("hello world"))