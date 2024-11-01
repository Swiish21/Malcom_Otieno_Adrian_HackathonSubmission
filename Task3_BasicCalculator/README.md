# Task3_BasicCalculator

Basic Calculator, We begin by creating a class 'calculator', we define an int function 'calculate', this function has 3 parameters, two integers 'num1' and 'num2' and a string 'operator', these two integers will be used to pass the integers to be implemented in the math operation, whereas the 'operator' string is used to pass the operator which selects which math operation to be done, for the main body of the algorithm we'll use a switch operator, the switch operator will switch to the specified math operation based on it's argument 'operator'. The first case of the switch is '+' which will perform an sum operation of the two numbers ('num1' and 'num2'), this will be the same case for the other operators (-,/,*). But what if we have a case where the user decides to divide by zero, in the divide case we throw an error where 'num2' is 0, but also added in more functionality, what if the user input an invalid operator, we use the default function to throw another error to show the user an unsupported error. We finish by defining a variable to hold the result of the algorithm and present test cases for the various operators and errors in place and print the result.

Problems Solved:
1. Create a basic calculator that takes in an operator and two integers and does the respective math operation.

2. Error handling for division by zero.

3. Error handling for an invalid operator(not in the test, but felt important)

Problem Not Solved:
1. Extend the function to handle multi-step operations, extending the function to handle these kind of operations led to a rise in new problems that rendered the whole program nonfunctional, hence the choice not to include it.

Github repo: https://github.com/Swiish21/Task3_BasicCalculator