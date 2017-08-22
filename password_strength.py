import re

def check_numbers(password):
    return re.findall('\d',password)

def check_symbols(password):
    return re.findall('\W',password)

def get_password_strength(password):
    strength=0
    if password.upper() or password.lower():
        strength+=1
    if check_numbers(password):
        strength+=2
    if len(password)>=9:
        strength+=1
    if check_symbols(password):
        strength+=3
    return strength


if __name__ == '__main__':
    print(get_password_strength("Антон34234"))