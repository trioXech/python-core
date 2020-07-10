# 2.7.3.4. Function Examples

Consider the following example function definitions paying close attention to the markers __/__ and __*__:
```python
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```
The first function definition, **standard_arg**, the most familiar form, places no restrictions on the calling convention and arguments may be passed by **position** or **keyword**:
```python
standard_arg(2)

standard_arg(arg=2)
```
The second function **pos_only_arg** is restricted to only use positional parameters as there is a **/** in the function definition:
```python
pos_only_arg(1)

Output: 1

pos_only_arg(arg=1)

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got an unexpected keyword argument 'arg'
```
The third function **kwd_only_args** only allows keyword arguments as indicated by a __*__ in the function definition:
```python
kwd_only_arg(3)

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

kwd_only_arg(arg=3)

Output: 3
```
And the last uses all three calling conventions in the same function definition:
```python
combined_example(1, 2, 3)

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given
```
```python
combined_example(1, 2, kwd_only=3)

Output: 1 2 3
```
```python
combined_example(1, standard=2, kwd_only=3)

Output: 1 2 3
```
```python
combined_example(pos_only=1, standard=2, kwd_only=3)

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got an unexpected keyword argument 'pos_only'
```

Finally, consider this function definition which has a potential collision between the positional argument **name** and __**kwds__ which has **name** as a **key**:
```python
def foo(name, **kwds):
    return 'name' in kwds
```
There is no possible call that will make it return **True** as the keyword **'name'** will always to bind to the first parameter. For example:
```python
foo(1, **{'name': 2})

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
```
But using **/** (positional only arguments), it is possible since it allows **name** as a positional argument and **'name'** as a key in the keyword arguments:
```python
def foo(name, /, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})

Output: True
```
In other words, the names of **positional-only** parameters can be used in \**kwds without ambiguity.
