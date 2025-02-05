def is_palindrome(word):
    if word == word[::-1]:
        return "The word is palindrome"

    return "The word is not palindrome"

