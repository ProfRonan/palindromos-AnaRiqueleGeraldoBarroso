"""Main functions"""
import re
def is_palindrome(string: str) -> bool:
    if string==string[::-1]:
        return True
    return False

string= input("Digite uma palavra: ").upper().strip().replace(' ', '')
string= re.sub(r'[.,"\'-?:!;]', '', string)
print(is_palindrome(string))