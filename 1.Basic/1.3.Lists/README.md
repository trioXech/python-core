# 1.3 Lists

Python knows a number of _**compound**_ data types, used to group together other values. The most versatile is the _**list**_, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

```python
squares = [1, 4, 9, 16, 25]

print(squares)

Output: [1, 4, 9, 16, 25]
```

Like strings (and all other built-in sequence types), lists can be indexed and sliced:

```python
squares = [1, 4, 9, 16, 25]

print(squares[0])

Output: 1

print(squares[-1])

Output: 25

print(squares[-3:])

Output: [9, 16, 25]
```

All slice operations return a new list containing the requested elements. This means that the following slice returns a **shallow copy** of the list:

```python
squares = [1, 4, 9, 16, 25]

print(squares[:])

Output: [1, 4, 9, 16, 25]
```

Lists also support operations like concatenation:
```python
squares = [1, 4, 9, 16, 25]

print(squares + [36, 49, 64, 81, 100])

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
```python
cubes = [1, 8, 27, 65, 125]  # something's wrong here
# the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)

Output: [1, 8, 27, 64, 125]
```

You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
```python
cubes = [1, 8, 27, 64, 125]
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # add the cube of 7

print(cubes)

Output: [1, 8, 27, 64, 125, 216, 343]
```
Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

Output: ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
print(letters)

Output: ['a', 'b', 'f', 'g']

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

Output: []
```

The built-in function **len()** also applies to lists:
```python
letters = ['a', 'b', 'c', 'd']
print(len(letters))

Output: 4
```

It is possible to nest lists (create lists containing other lists), for example:
```python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

Output: [['a', 'b', 'c'], [1, 2, 3]]

print(x[0])

Output: ['a', 'b', 'c']

print(x[0][1])

Output: b
```

## Solve Some Problems

1. [Find the Runner-Up Score](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)
2. [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem)
3. [NestedLists](https://www.hackerrank.com/challenges/nested-list/problem)
4. [Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem)
5. [List](https://www.hackerrank.com/challenges/python-lists/problem)
