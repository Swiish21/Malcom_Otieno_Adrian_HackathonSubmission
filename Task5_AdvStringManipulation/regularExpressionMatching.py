def is_match(text: str, pattern: str) -> bool:
    
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
print(is_match("mississippi", "mis*is*p*."))  # False
