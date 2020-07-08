# 1.2 Strings 

Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. \ can be used to escape quotes:
```python
print('spam eggs')  # single quotes

Output: spam eggs
```
```python
print('doesn\'t')  # use \' to escape the single quote...

Output: doesn't
```
```python
print("doesn't")  # ...or use double quotes instead

Output: doesn't
```
```python
print('"Yes," they said.')

Output: "Yes," they said.
```
```python
print("\"Yes,\" they said.")

Output: "Yes," they said.
```
```python
print('"Isn\'t," they said.')

Output: "Isn\'t," they said.
```
In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters.


If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
```Python
print('C:\some\name')  # here \n means newline!

Output: 
C:\some
ame
```
```Python
print(r'C:\some\name')  # note the r before the quote

Output: 
C:\some\name
```


String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:
```Python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
produces the following output (note that the initial newline is not included):
```python
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

Strings can be concatenated (glued together) with the + operator, and repeated with * :
```python
# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

Output: unununium
```

Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated. 

```python 
print('py' 'thon')

Output: Python 
```

This feature is particularly useful when you want to break long strings:
```python 
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

Output: Put several strings within parentheses to have them joined together.
```

This only works with two literals though, not with variables or expressions:
```Python
prefix = 'Py'
print(prefix 'thon')

Output: 
File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
```

If you want to concatenate variables or a variable and a literal, use **+**:
```python
prefix = 'Py'
print(prefix + 'thon')

Output: Python 
```

Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
```Python
word = 'Python'
print(word[0]) # Character in position 0

Output: P

print(word[5]) # Character in position 5

Output: n 
```

Indices may also be negative numbers, to start counting from the right:
```python
word = 'Python'
print(word[-1]) # last character 

Output: n 

print(word[-2]) # second-last character

Output: o 

print(word[-6]) 

Output: P
```
_**Note that since -0 is the same as 0, negative indices start from -1.**_ 

In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
```Python 
word = 'Python'

print(word[0:2]) # characters from position 0 (included) to 2 (excluded)

Output: Py 

print(word[2:5]) # characters from position 2 (included) to 5 (excluded)

Output: tho 
```

_**Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:**_ 
```python 
word = 'Python'
print(word[:2] + word[2:]) 

Output: Python 

print(word[:4] + word[4:])

Output: Python 
```

Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
```python 
Word = 'Python'
print(word[:2]) # character from the beginning to position 2 (excluded)

Output: Py

print(word[4:]) # characters from position 4 (included) to the end

Output: on

print(word[-2:]) # characters from the second-last (included) to the end

Output: on
```

One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example: 

```python 
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```
The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:
```python 
word = 'Python'
print(word[42]) # the word only has 6 characters

Output: 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
_However, out of range slice indexes are handled gracefully when used for slicing:_ 
```python
word = 'Python'
print(word[4:42])

Output: on 

print(word[42:])

Output: ''
```

Python strings cannot be changed — they are **immutable**. Therefore, assigning to an indexed position in the string results in an error:
```python 
word = 'Python'

word[0] = 'J'

Output: 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

word[2:] = 'py'

Output: 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you need a different string, you should create a new one: 
```python 
word = 'Python'
print('J' + word[1:])

Output: Jython 

print(word[:2] + 'py')

Output: pypy
```

**The built-in function len() returns the length of a string:** 
```python 
s = 'supercalifragilisticexpialidocious'
print(len(s))

Output: 34 
```