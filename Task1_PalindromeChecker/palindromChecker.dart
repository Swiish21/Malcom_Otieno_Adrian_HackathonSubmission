// This is a Dart program that checks whether a given string and numeric inputs is a palindrome
void main() {
  //below is a function delacred with a boolean as it is only required to return a true or false value
  bool isPalindromeNum(String input) {//the parameter input is a string
    if (input.isEmpty) { 
      print('This is an empty string, which technically is a palindrome');// Check if the input string is empty, if empty it resturns true
      return true; // Empty strings are considered palindromes
    }

    // the line below makes the palindrome case insesitive, it takes the string and converts it to lower case and removes all non-alphanumeric characters(normalize)
    // it ignores spaces, punctuation and any special characters in the string
    final normalizedInput = input.toLowerCase().replaceAll(RegExp(r'[^a-zA-Z0-9]'), '');// the final key word is used to declare a constant variable(a variable that cannot be changed)

    // here we declare two variables left and right that are used  to iterate through the normalized input string
    // it creates an approach where the left pointer is at the beginning of the string and the right pointer is at the end of the string
    int left = 0;
    int right = normalizedInput.length - 1;

    //below is a while loop that we use to iterate through the string and compare the characters at the left and right pointers
    while (left < right) { // here the condition state that the loop will continue as long as the left pointer is less than the right pointer,to ensure we go through the entire string
      if (normalizedInput[left] != normalizedInput[right]) { // here we compare the characters of the string if they are not equal it returns false(not a palindrome)
        print('The input string is not a palindrome');
        return false; // returns false if the characters are not equal
      }
      left++;// here we increment the left pointer to move to the next character in the string(moving in forward direction)
      right--; // here we decrement the right pointer to move to the previous character in the string(moving in reverse direction)
    }
    print('The input string is a palindrome');
    return true; // returns true if the characters are equal on both the left and right sides
    
  }

  // below are some test cases for this program where we input different strings and check if they are palindromes
  String str = "racecar"; //case1
  String str2 = "Madam, I'm Adam!"; //case2
  String str3 = "hello"; //case3
  String str4 = ""; //case4
  String str5 = "12321"; //case5

  print(isPalindromeNum(str)); // Output: true
  print(isPalindromeNum(str2)); // Output: true
  print(isPalindromeNum(str3)); // Output: false
  print(isPalindromeNum(str4)); // Output: true
  print(isPalindromeNum(str5)); // Output: true
}