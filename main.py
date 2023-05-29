"""Main functions"""
import re
def is_palindrome(string: str) -> bool:
    string = string.upper().strip().replace(' ', '')
    string = re.sub(r'[.,"\'-?:!;]', '', string)
    if string==string[::-1]:
        return True
    return False

if __name__ == "__main__":
    string = input("Digite uma palavra: ")
    print(is_palindrome(string))