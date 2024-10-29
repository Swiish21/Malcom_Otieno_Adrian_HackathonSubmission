def is_match(text: str, pattern: str) -> bool: #we defined a function is_match that has two parameters, one for the string to be checked and one for the regex pattern, the function is supposed to return either true or false(boolean)

    #below here we deal with the case where if the pattern is empty, if it is , it means that our text must also be empty for it match, else it returns a false value. 
    if not pattern: 
        return not text

    first_match = bool(text) and (pattern[0] == text[0] or pattern[0] == '.')

    if len(pattern) >= 2 and pattern[1] == '*':
        return is_match(text, pattern[2:]) or first_match and is_match(text[1:], pattern)
    else:
        return first_match and is_match(text[1:], pattern[1:])
        
print(is_match("aa", "a"))  # False
print(is_match("aa", "a*"))  # True
print(is_match("ab", ".*"))  # True
