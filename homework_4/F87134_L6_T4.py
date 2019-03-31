import sys
import string

user_input = sys.argv[1:]
text = user_input[0].translate(string.maketrans("",""), string.whitespace + string.punctuation).lower()


def check_palindrome(text_start, text_end):
    if text[text_start] != text[text_end]:
        return False
    
    if text_end == 0:
        return True
    else:
        return check_palindrome(text_start + 1, text_end - 1)


print check_palindrome(0, len(text) - 1)
