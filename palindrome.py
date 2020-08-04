#test
import string

def check_palindrome(string1):
    print("input: " + string1)
    stripped1 = [ s for s in string1.lower() if s.isalpha()]
    rev = stripped1[::-1]
    return rev == stripped1


string1 = """Go Hang a Salami! I'm a Lasagna Ho!"""
print(check_palindrome(string1))
