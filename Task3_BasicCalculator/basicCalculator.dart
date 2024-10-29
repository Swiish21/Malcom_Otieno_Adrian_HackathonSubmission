class Calculator { // defined a class called Calculator which will hold our method
  int calculate(int num1, int num2, String operator) { // defined a method called calculate, which takes 3 arguents, two integers and one string(the operator)

    switch (operator) { // we move on to the switch statement which chooses the math operation based on the operator string arguement
      case '+': // if the operator is + we return the sum of num1 and num2
        return num1 + num2;
      case '-': // if the operator is - we return the minus of num1 and num2
        return num1 - num2;
      case '*': // if the operator is * we return the product of num1 and num2
        return num1 * num2;
      case '/': // if the operator is / we return the quotient of num1 and num2
        if (num2 == 0) { // if num2 is 0 we throw an error
          throw ArgumentError('Cannot divide by zero');
        }
        return num1 ~/ num2; // here we return the quotient of num1 and num2
      default: // if the operator is not one of the above we throw an error
        throw UnsupportedError('Invalid operator');
    }
  }
}

void main() {
  //test cases for our program for every scenario
  Calculator calculator = Calculator();
  print(calculator.calculate(10, 5, '+')); // Output: 15
  print(calculator.calculate(11, 3, '-')); // Output: 8
  print(calculator.calculate(20, 7, '*')); // Output: 140
  print(calculator.calculate(100, 5, '/')); // Output: 20
  print(calculator.calculate(18, 0, '/')); // Output: ArgumentError: Cannot divide by zero
  print(calculator.calculate(1, 5, 'x')); // Output: UnsupportedError: Invalid operator
  print(calculator.calculate(15, 3, '')); //Output: ArgumentError: Operator cannot be null
}