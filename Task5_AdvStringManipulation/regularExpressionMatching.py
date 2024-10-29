def is_match(text: str, pattern: str) -> bool: #we defined a function is_match that has two parameters, one for the string to be checked and one for the regex pattern, the function is supposed to return either true or false(boolean)

    #below here we deal with the case where if the pattern is empty, if it is , it means that our text must also be empty for it match, else it returns a false value. 
    if not pattern: 
        return not text
    #now we deal with the case where the first character of the text matches the first character of the pattern, also added a case where it will match if the first character is a (.) which stands for any character.
    first_match = bool(text) and (pattern[0] == text[0] or pattern[0] == '.')
    #here we use an if statement to check two conditions, if the length of the pattern is graeter than or equal to 2 and the second symbol in the pattern is (*)
    if len(pattern) >= 2 and pattern[1] == '*': #we'll have two scenarios below.
        return is_match(text, pattern[2:]) or first_match and is_match(text[1:], pattern) 
        #is_match(text, pattern[2:0]) covers the case where the wildcard matches zero occurences of the preceeding character and first_match and is_match(text[1:], pattern) covers the case where the wildcard matches one or more occurence of the preceeding charcter.
    else:
        return first_match and is_match(text[1:], pattern[1:]) #if the second character of the pattern is not a (*), its a normal character match and the 'first_match' condition ensures the first character match then it checks whether the remaining characters match with the pattern.
        
print(is_match("aa", "a"))  # False
print(is_match("aa", "a*"))  # True
print(is_match("ab", ".*"))  # True
