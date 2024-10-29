#below is a function which finds the length of the longest substring without repeating characters
def length_of_longest_substring(s: str) -> int: #we define the function and assign it a name and parameter s(string), the function is supposed to return an int value

    char_set = set() #we create an empty set that will hold the substring
    left = 0 #left represents the starting index of the substring
    max_length = 0 #max_length represents the length of the longest substring, initially set to 0

    for right in range(len(s)): #we iterate through the string to find the substring
        while s[right] in char_set: #this nested while loop checks if the current character is already in the substring
            char_set.remove(s[left]) #if it is, we remove it from the substring (no repeating characters allowed)
            left += 1 #we move the left pointer to the next index(avoiding repeating characters)
        char_set.add(s[right]) #if the current character is not in the substring, we add it to the substring
        max_length = max(max_length, right - left + 1) # we then add(update) the length of the substring to the max_length

    return max_length #once finished, we return the length of the longest substring

str = input('Enter a string to be checked, (E.g "pwwkew", "abcabcbb", "bbbbb", "tmmzuxt"):') #test case for the function
print('The length of the longest substring without repeating characters is:', length_of_longest_substring(str))