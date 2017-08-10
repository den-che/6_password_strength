import re

def upper_case(password):
    return re.search('[A-Z]', password)

def lower_case(password):
    return re.search('[a-z]',password)

def check_special_symbols(password):
    return re.search('\d',password)

def get_password_strength(password):
    strength=0
    if upper_case(password):
        strength+=1
    if lower_case(password):
        strength+=1
    if check_special_symbols(password):
        strength+=1
    return strength


if __name__ == '__main__':
    print(get_password_strength("Pass"))
