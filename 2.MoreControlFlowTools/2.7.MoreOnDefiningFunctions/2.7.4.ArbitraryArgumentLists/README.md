# 2.7.4. Arbitrary Argument Lists

Finally, the least frequently used option is to specify that a function can be called with an **arbitrary number of arguments**. _These arguments will be wrapped up in a tuple (see Tuples and Sequences)_. Before the variable number of arguments, zero or more normal arguments may occur.
```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

Normally, these **variadic** arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the __*args__ parameter are **‘keyword-only’** arguments, meaning that they can only be used as keywords rather than **positional arguments**.
```python
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

Output: earth/mars/venus

concat("earth", "mars", "venus", sep=".")

Output: earth.mars.venus

```
