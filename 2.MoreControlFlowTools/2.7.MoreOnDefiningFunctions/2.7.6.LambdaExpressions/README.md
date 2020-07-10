# 2.7.6. Lambda Expressions

Small anonymous functions can be created with the **lambda** keyword. This function returns the sum of its two arguments: **lambda a, b: a+b**. Lambda functions can be used wherever function objects are required. They are _syntactically restricted to a single expression_. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:
```python
def make_incrementor(n):
  return lambda x: x + n

f = make_incrementor(42)
f(0)

Output: 42

f(1)

Output: 43
```
The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:
```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

Output:
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
