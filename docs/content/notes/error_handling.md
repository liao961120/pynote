---
title: Error Handling
weight: 5
---

## Try, Except, Finally


```python
try:
    print("=== Try block ===")
    if "10" > 10:
        print("Content in try block after error encountered")
except:
    print("=== Except block ===")
```

    === Try block ===
    === Except block ===


### Capture Exception Type


```python
try:
    print("=== Try block ===")
    if "10" > 10:
        print("Content in try block after error encountered")
except Exception as exp:
    print("=== Except block ===")
    print(type(exp), "encountered:")   # Exception type
    print("   ", exp)                  # Exception message
```

    === Try block ===
    === Except block ===
    <class 'TypeError'> encountered:
        '>' not supported between instances of 'str' and 'int'


### Deal With Different Kinds of Exception


```python
a = 10
b = "10"

try:
    print("=== Try block ===")
    if a > int(b):
        print("Content in try block after error encountered")
except TypeError:
    print("=== Except block 1 ===")
    print("TypeError encountered, check input of a")
except ValueError:
    print("=== Except block 2 ===")
    print("ValueError encountered, check input of b")
```

    === Try block ===



```python
a = "10"
b = "10"

try:
    print("=== Try block ===")
    if a > int(b):
        print("Content in try block after error encountered")
except TypeError:
    print("=== Except block 1 ===")
    print("TypeError encountered, check input of a")
except ValueError:
    print("=== Except block 2 ===")
    print("ValueError encountered, check input of b")
```

    === Try block ===
    === Except block 1 ===
    TypeError encountered, check input of a



```python
a = 10
b = "k"

try:
    print("=== Try block ===")
    if a > int(b):
        print("Content in try block after error encountered")
except TypeError:
    print("=== Except block 1 ===")
    print("TypeError encountered, check input of a")
except ValueError:
    print("=== Except block 2 ===")
    print("ValueError encountered, check input of b")
```

    === Try block ===
    === Except block 2 ===
    ValueError encountered, check input of b


### Clean up with `finally`

If we return early (e.g in try-except blocks), the rest of the code won't be excecuted.


```python
def fun(a, b):
    try:
        print("=== Try block ===")
        if a > int(b):
            print("Content in try block after error encountered")
    except TypeError:
        print("=== Except block 1 ===")
        print("TypeError encountered, check input of a")
        return 1
    except ValueError:
        print("=== Except block 2 ===")
        print("ValueError encountered, check input of b")
        return 2
    
    print("This will not be printed if exception encounterd")
    return 0
```


```python
fun(10, "k")
```

    === Try block ===
    === Except block 2 ===
    ValueError encountered, check input of b





    2



If you some code **must be run** after the try-except blocks, a better way is to use the `finally` block.

`finally` block is a good way to clean up code (such as closing the file).


```python
def fun(a, b):
    try:
        print("=== Try block ===")
        if a > int(b):
            print("Content in try block after error encountered")
    except TypeError:
        print("=== Except block 1 ===")
        print("TypeError encountered, check input of a")
        return 1
    except ValueError:
        print("=== Except block 2 ===")
        print("ValueError encountered, check input of b")
        return 2
    # Code here is executed no matter whether except block that was executed
    finally:  
        print("This is always printed")
        
    return 0
```


```python
fun(10, "k")
```

    === Try block ===
    === Except block 2 ===
    ValueError encountered, check input of b
    This is always printed





    2



## Raising Exception

To raise a (self-defined) exception in a function, use the expression `raise Exception("exception-name")`.


```python
def fun(prob):
    if not 0 <= prob <= 1:
        raise Exception("InvalidProb")
    return prob
```


```python
fun(1.5)
```


    -------------------------------------------------------------------------

    Exception                               Traceback (most recent call last)

    <ipython-input-35-0dd1cabf5a55> in <module>
    ----> 1 fun(1.5)
    

    <ipython-input-31-98ccab9d5d44> in fun(prob)
          1 def fun(prob):
          2     if not 0 <= prob <= 1:
    ----> 3         raise Exception("InvalidProb")
          4     return prob


    Exception: InvalidProb


You can then capture this exception with an `except` block:


```python
def safeFun(prob):
    try:
        prob = fun(prob)
    except Exception as exp:
        print('Exception encountered: %s' % str(exp))
        prob = 0
    
    return prob
```


```python
safeFun(1.5)
```

    Exception encountered: InvalidProb





    0


