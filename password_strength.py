import re
import os

def load_password_blacklist(filepath):  
    if not os.path.exists(filepath):
        return None
    else:
        with open(filepath,'r', encoding='utf-8') as file_blacklist:
            blacklist = file_blacklist.read().split("\n") 
            return blacklist


def check_in_blacklist(password,filepath):
    blacklist = load_password_blacklist(filepath)
    if password in blacklist:
        return True
    else:
        return False


def check_numbers(password):
    return re.findall('\d',password)


def check_symbols(password):
    return re.findall('\W',password)


def get_password_strength(password):
    strength=0
    if password.upper() or password.lower():
        strength+=1
        print("Password have lower case/upper case")
    if check_numbers(password):
        strength+=2
        print("Password have digits")
    if len(password)>=9:
        strength+=1
        print("Password length > 8 symbols")
    if check_symbols(password):
        strength+=3
        print("Password have special symbols")
    return strength


if __name__ == '__main__':
    password = "vjht1051#"
    file_blacklist = "blacklist_password.txt"
    blacklist = list()
    if check_in_blacklist(password,file_blacklist) == False:
        print(get_password_strength(password))
    else:
        print("Password was found in blacklist. Please, choose another password")