# Practice Problems
__Guidelines:__
1. Try to solve the problem on your own, with no help.
2. If you need to, look at a couple hints for the problem.
3. If you solve it, compare your answer with mine. If you still can't solve it after hints, try understanding what I did in my solution.

__Note:__ Keep in mind that my answers are not necessarily the only way to implement these problems. Many problems have multiple solutions that are equally as correct and stylistically good. Of course, there are certain optimizations that can be made that set apart some solutions from others, but for now we are only worrying about correctness, so all solutions are correct. Also, in each section the problems generally increase in difficulty.
## Familiarizing yourself with the Python environment
1. Create a program that prints the words "Hello World" to the terminal.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that the print function accepts one parameter, the thing you want to print.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    To input a string in python, use double quotes or single quotes.
  </details>
* [Answer](answers/python/python_1.py)
2. Create a program that reads a single value (either word or number) and prints it out.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that python has the input function, which reads input from the user. You can give a description of what you want inputted by passing in a string as a parameter like this: input('description here')
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that the print function accepts one parameter, the thing you want to print.
  </details>
* [Answer](answers/python/python_2.py)
3. Create a program that reads 3 values and prints them in the reverse order they were entered (e.g. an input of 4 5 6 should print "6 5 4").
* <details>
    <summary>Click to reveal hint #1</summary>
    Try storing the 3 values into variables.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    To store a value into a variable, do something like this: variable_name = value
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Remember that python has the input function, which reads input from the user. You can give a description of what you want inputted by passing in a string as a parameter like this: input('description here')
  </details>
* [Answer](answers/python/python_3.py)
4. Create a program that reads a value from the user and prints the type of the value.
* <details>
    <summary>Click to reveal hint #1</summary>
    Look at previous hints for how to use the input function.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that python has a type function that takes in a value as its parameter and returns the type of that value.
  </details>
* [Answer](answers/python/python_4.py)

## Using Expressions and Operators
Note: When I say number I usually expect a float. When I'm expecting an integer I usually specify "integer".
1. Write a program that reads 2 numbers from the user and prints out their sum.
* <details>
    <summary>Click to reveal hint #1</summary>
    A good idea for starting off would be store the numbers into variables.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that the input() function returns everything as a string. To convert the string into a number (in this case you want float), use float() like this: float(input())
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Remember your math operators, like +.
  </details>
* [Answer](answers/exop/exop_1.py)
2. Write a program that prints out the volume of a sphere, with the radius given by the user.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that to raise a value to the power of another value, use the ** operator.
  </details>
* [Answer](answers/exop/exop_2.py)
3. Write a program to find the average of 2 numbers inputted by the user.
* <details>
    <summary>Click to reveal hint #1</summary>
    Try storing the 2 values into variables.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that the average of 2 numbers is their sum divided by 2.
  </details>
* [Answer](answers/exop/exop_3.py)
4. Write a program that will accept the base and height of a triangle and compute the area.
* <details>
    <summary>Click to reveal hint #1</summary>
    Try storing the values into variables. Refer to an earlier hint for how to do this.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Try googling the formula for area of a triangle.
  </details>
* [Answer](answers/exop/exop_4.py)
5. Write a program that accepts an integer n as input (no need to clean the input) and prints the value of n+nn+nnn.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that the input() function returns everything as a string. To convert the string into an integer, use int() like this: int(input())
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Try calculating the values for n, nn, and nnn first. Store them into variables.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    nn can be calculated by adding n to n*10. nnn should be calculated in a similar way.
  </details>
* [Answer](answers/exop/exop_5.py)
6. Write a program that reads 2 numbers from the user, a and b, and prints out a raised to the b power.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that to raise a value to the power of another value, use the ** operator.
  </details>
* [Answer](answers/exop/exop_6.py)
7. Write a program that reads 2 numbers from the user, x and y, and prints out the remainder of x/y.
* <details>
    <summary>Click to reveal hint #1</summary>
    Look up what the modulo operator does.
  </details>
* [Answer](answers/exop/exop_7.py)

## Conditionals and Control Flow
1. Write a program that reads 1 integer from the user and prints out whether the number is even or odd (e.g. 2 should print out "even", 3 should print out "odd").
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that when you need to execute code based on a condition, use if-else statements.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that the format of an if statement looks like this: if [expression]: (where [expression] should be substituted with an expression that evaluates to True or False)
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Remember that the mod operator % can be used to test for divisibility.
  </details>
* [Answer](answers/cond/cond_1.py)
2. Write a program that reads a number n and prints "Hooray" if n is greater than 10, and "Darn it" otherwise.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember how to use an if statement (see above hints).
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that comparison operators exist.
  </details>
* [Answer](answers/cond/cond_2.py)
3. Write a program to print the sum of two given integers. However, if the sum is between 15 to 20 (inclusive) it will print 20.
* <details>
    <summary>Click to reveal hint #1</summary>
    Try storing the 2 integers into variables first and calculating the sum and storing the sum into another variable.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that the input() function returns everything as a string. To convert the string into a number (in this case you want float), use float() like this: float(input())
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Use an if statement to test if the sum statisfies the condition.
  </details>
* [Answer](answers/cond/cond_3.py)

## Loops + Conditionals
1. Write a program to print all integers from 1 to 100, inclusive (do not hardcode this).
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that you can use a for loop to loop over structures returned by range(). For the format of a for loop, look at your past code.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that the range function takes 3 parameters, start, stop, and step.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Remember that the stop parameter in range does not include the actual value, it always stops BEFORE that value.
  </details>
* [Answer](answers/loops/loops_1.py)
2. Write a program that prints all the integers from 0 to 6 (inclusive) except 3 and 5 (you may hardcode the 3 and 5 but use a loop to iterate from 0 to 6).
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that to have a range include a certain integer n, you need to stop the range at n+1. For example, range(0, 10, 1) gives 0-9.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Use an if statement inside the loop to omit printing out 3 and 5.
  </details>
* [Answer](answers/loops/loops_2.py)
3. Write a program to print 30 "*" characters.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that to execute something 30 times, you can just iterate over a range that counts from 0 to 29.
  </details>
* [Answer](answers/loops/loops_3.py)
4. Write a program that reads an integer n and prints that integer n times (e.g. 3 would print "333").
* <details>
    <summary>Click to reveal hint #1</summary>
    Try storing n into a variable first and converting it into an integer. To convert into an integer, look at previous hints.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that to execute something n times, you can just iterate over a range that counts from 0 to n.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    To print something without a newline at the end, add an extra parameter to print like this: print(value, end='')
  </details>
* <details>
    <summary>Click to reveal hint #4</summary>
    To print only a newline, do this: print('')
  </details>
* [Answer](answers/loops/loops_4.py)
5. Write a program that reads an integer n and prints out all integers greater than or equal to 2 and less than n that are divisible by 5 and 7.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that you can use n as one of the parameters in the range() function.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    You want to use an if statement inside of your loop, like in fizz-buzz.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Remember your 'and' and 'or' keywords, which allow you to link together 2 or more conditions.
  </details>
* [Answer](answers/loops/loops_5.py)
6. Write a program that reads a integer n and prints out all integers greater than or equal to 2 and less than n that are divisible by 5 or 7.
* <details>
    <summary>Click to reveal hint #1</summary>
    This answer is exactly like the previous one with one modification.
  </details>
* [Answer](answers/loops/loops_6.py)
7. Write a program that prints out the following pattern for any given integer n:
```
n=3
*
**
***

n=5
*
**
***
****
*****
```
* <details>
    <summary>Click to reveal hint #1</summary>
    First read n from the user and convert it to an integer. For how to do this, refer to previous hints.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Realize that you need n rows, which means a for loop that executes n times.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Realize that in each row, you need to print a star row number of times, depending on which row you're on. This means use another for loop, but this for loop should be inside of the for loop that manages rows (a nested for loop).
  </details>
* <details>
    <summary>Click to reveal hint #4</summary>
    To print something without a newline at the end, add an extra parameter to print like this: print(value, end='')
  </details>
* <details>
    <summary>Click to reveal hint #5</summary>
    To print only a newline, do this: print('')
  </details>
* [Answer](answers/loops/loops_7.py)
8. Write a program that first reads an integer n. Then read n number of numbers from the user, and calculate (and print) their average.
* <details>
    <summary>Click to reveal hint #1</summary>
    This problem is very similar to a previous problem. As you are reading the numbers, add them to a cumulative sum (using a variable that you initialize before you starting reading numbers from the user).
  </details>
* [Answer](answers/loops/loops_8.py)
9. Write a program to calculate and print a dog's age in dog years, given the age of the dog in human years. Take the age as an integer input. For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years. (Note: This can also be solved without a loop, and I think both solutions are interesting so I'll say both are correct).
* <details>
    <summary>Click to reveal hint #1</summary>
    Consider using a for loop that iterates over each human year of the dog.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Intialize a float variable before your loop that represents total dog years. Then, for each human year, add the appropriate amount of dog years to that total.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Use an if statement to determine how many dog years to add during each human year.
  </details>
* [Answer](answers/loops_9.py)

## Functions
1. Write a function that calculates and returns the square of the length of the hypotenuse of a right triangle, given the two other side lengths as parameters. Then call this function with lengths 5 and 12 and print the result.
* <details>
    <summary>Click to reveal hint #1</summary>
    Remember that you define a function by using def and then the function name. For an example, look at our list searching code that we wrote.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember that function should return the answer, not necessarily print it. Return answers with the keyword 'return'.
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    Use the pythagorean theorem to calculate the square of the hypotenuse.
  </details>
* <details>
    <summary>Click to reveal hint #4</summary>
    To call a function, simply use the function name and pass in the parameters. Refer to the end of our searching code for an example of this.
  </details>
* [Answer](answers/functions/functions_1.py)
2. Write a function that takes in a string as a parameter, representing the name of a person. The function should return the given name with the word "san" appended to the end (e.g. "Smith" turns into "Smithsan"). Then call this function once with the name "David" and another time with the name "Charles" and print the results.
* <details>
    <summary>Click to reveal hint #1</summary>
    Refer to previous question's hints for how to define and call a function.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    To append a string to another string, use the + operator like this: str1 + str2
  </details>
* [Answer](answers/functions/functions_2.py)

## Lists
1. Write a program that reads an integer n from the user and removes the element at index n from the hardcoded list [34, 5, 68, 2456, 245, 47, 23, 4, 2, 9, 45]. Print the resulting list.
* <details>
    <summary>Click to reveal hint #1</summary>
    Start by initializing the list into a variable.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember or look up the list modification functions, in particular the pop() function. To call a function on a list, do something like this: l.pop()
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    To print a list, simply pass it into print like this: print(l)
  </details>
* [Answer](answers/lists/lists_1.py)
2. Write a program that reads an integer n from the user and removes the first element equivalent to n from the hardcoded list [34, 5, 68, 2456, 245, 47, 23, 4, 2, 9, 45]. Assume that n exists in the list (e.g. Don't test using values that aren't in the list). Print the resulting list.
* <details>
    <summary>Click to reveal hint #1</summary>
    Start by initializing the list into a variable.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Remember or look up the list modification functions, in particular the remove() function. To call a function on a list, do something like this: l.remove()
  </details>
* <details>
    <summary>Click to reveal hint #3</summary>
    To print a list, simply pass it into print like this: print(l)
  </details>
* [Answer](answers/lists/lists_2.py)
3. Write a program that reads an integer n from the user first. The program should then read in n more numbers and add those numbers to a list. Print the resulting list.
* <details>
    <summary>Click to reveal hint #1</summary>
    Start by initializing an empty list into a variable.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    Use a for loop to read n numbers and append each number to the list that you initialized. To append, use the list append function.
  </details>
* [Answer](answers/lists/lists_3.py)


## Challenge
1. Write a function that takes in a list l and target t and finds the second occurrence of t in l. If t does not occur at least twice, return -1. Otherwise, return the index of the second occurrence. Call this function with the list [1, 2, 3, 4, 4, 5, 6, 7, 4], with target = 4, and print the result. Call this function again with the same list and target = 2. Print the result.
* <details>
    <summary>Click to reveal hint #1</summary>
    This problem requires a modified version of the linear search function that we covered.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    To find a value twice, try setting a boolean variable that marks if the value is already found once. That way, you can check if it was already found once when you find it again.
  </details>
* [Answer](answers/challenge/challenge_1.py)
2. Write a function that takes in a list l of numbers and returns a new list where the number at index i is the sum of the number at index i in l multiplied by all of the numbers in l. Call this function with the list [1, 2, 3, 4, 5] and print the result.
* <details>
    <summary>Click to reveal hint #1</summary>
    Your function should create a new list. I suggest making an empty list and adding values to it.
  </details>
* <details>
    <summary>Click to reveal hint #2</summary>
    This will require nested for loops. You want to perform a calculation for each number in the list using every number in the list.
  </details>
* [Answer](answers/challenge/challenge_2.py)