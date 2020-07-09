# The range() Function

If you do need to iterate over a sequence of numbers, the built-in function **range()** comes in handy. It generates **arithmetic progressions**:
```python
for i in range(5):
  print(i)

Output:
0
1
2
3
4
```

_The given end point is never part of the generated sequence;_
**range(10)** generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the **‘step’**):
```Python
range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70
```

To iterate over the indices of a sequence, you can combine **range()** and **len()** as follows:
```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
  print(i, a[i])

Output:
0 Mary
1 had
2 a
3 little
4 lamb
```
In most such cases, however, it is convenient to use the **enumerate()** function, see Looping Techniques.

A strange thing happens if you just print a range:
```python
print(range(10))

Output: range(0, 10)
```
In many ways the object returned by **range()** behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, **thus saving space**.

We say such an object is **iterable**, that is, suitable as a target for **functions** and **constructs** that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the **for** statement is such a construct, while an example of a **function** that takes an **iterable** is **sum()**:
```python
print(sum(range(4))) # 0 + 1 + 2 + 3

Output: 6
```
Later we will see more functions that return iterables and take iterables as arguments. Lastly, maybe you are curious about how to get a list from a range. Here is the solution:
```python
print(list(range(4)))

Output:
[0, 1, 2, 3]
```
