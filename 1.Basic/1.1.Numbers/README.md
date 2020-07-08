# 1.1 Numbers

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses (()) can be used for grouping. For example:
```
print(2 + 2)
output: 4
```
```
print(50 - 5*6)
output: 20
```
```
print((50 - 5*6) / 4)
output: 5.0
```
```
print(8 / 5)  # division always returns a floating point number
output: 1.6
```

The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.


Division (**/**) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the **//** operator; to calculate the remainder you can use %:
```
print(17 / 3)  # classic division returns a float
output: 5.666666666666667
```
```
print(17 // 3)  # floor division discards the fractional part
output: 5
```
```
print(17 % 3)  # the % operator returns the remainder of the division
output: 2
```
```
print(5 * 3 + 2)  # result * divisor + remainder
output: 17
```

With Python, it is possible to use the ** operator to calculate powers:
```
print(5 ** 2)  # 5 squared
output: 25
```
```
print(2 ** 7)  # 2 to the power of 7
output: 128
```

The equal sign (**=**) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:
```
width = 20
height = 5 * 9
print(width * height)

output: 900
```

If a variable is not “defined” (assigned a value), trying to use it will give you an error:
```
print(n)  # try to access an undefined variable

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:
```
print(4 * 3.75 - 1)

Output: 14.0
```

**In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).**
