def is_match(s: str, p: str) -> bool: # we define a function called is_match that returns a boolean value, we assign it 2 parametres s(string) and p(string)
    #s is for the string to be checked and p is for the regular expression to compare it to.

    if len(p) == 0: # here we deal with the case where the regular expression  and the string are empty,
        return len(s) == 0 #if they are both empty we return true, otherwise false


    if len(p) == 1: # here we deal with the case where the regular expression has only one character
        return len(s) == 1 and (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) #if the first character of the regular expression is the same as the first character of the string, we return true, otherwise false

    # here we deal with the case where the regular expression has more than one character
    if p[1] == '*': #if the second character of the regular expression is a star, we check if the first character of the string matches the regular expression
        return (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) and is_match(s, p[2:]) or (s != '' and (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) and is_match(s[1:], p))


    return (s != '' and (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) and is_match(s[1:], p[1:])) #if the first character of the regular expression is the same as the first character of the string, we return true, otherwise false

#test cases for our function
print(is_match("aa", "a"))  # Output: False , reason is the expression wants a single character, the string has two characters
print(is_match("aa", "a*"))  # Output: True , reason the expression has an asterisk, so it doesn't matter how many 'a's are in the string, it will match the condition
print(is_match("ab", ".*"))  # Output: True , reason is the expression has a dot and then an asterisk, meaning any character(s) are allowed,
print(is_match("mississippi", "mis*is*p*."))  # Output: False , reason is the input string has too many 'i' and 's', but the expression doesn't allow it to have all these 'i's and 's's, hence it will return false.