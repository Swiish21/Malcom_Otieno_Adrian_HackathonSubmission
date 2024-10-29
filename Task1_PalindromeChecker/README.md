# Task1_PalindromeChecker

A palindrome is a word that can be read the same from first character to last and reversed

This is a dart program palindrome checker, the program takes a given string, makes it all lowercase, ignores all or any special character.

We define a bool function 'isPalindromeNum' which has a single parameter 'input' whic is a string, this string input will be used to input the strings to be checked is they are parametres, we begin the algorithm by tackling the first case that is when the input string is empty, if it is , it means it's a palindrome as empty strings are technically considered palindromes, the alg returns true. If not we continue to normalisation, normalisation is at the point where we convert the input string in all lowercase and remove all or any special characters, we utilise darts inbuilt tolowercase and Regex fuctions to remove all special characters and make all the characters in the string lowercase. In order to check the input string after normalisation we need a while loop, but for the while loop to work we first need to create a range with which it will iterate,to do this we define two variables left(for the left pointer) and right (for the right pointer), the while loop has a condition(While left < right) this is to ensure we go through all the characters of the input string. The loop is going to run through each character of the string then we'll use an if statement to compare if the all characters from left to right match with all the characters from right to left, if they do that means the string is palindrome and the function returns true, else it returns false. We finish by presenting some test cases for our algorithm to test its functionality.

Challenges solved:
1. An algorithm that checks if a given string is an input.
2. Extend the function to check for palindrome properties for numeric inputs.