# Error Handling

## Try, Except, Finally

try:
    print("=== Try block ===")
    if "10" > 10:
        print("Content in try block after error encountered")
except:
    print("=== Except block ===")

### Capture Exception Type

try:
    print("=== Try block ===")
    if "10" > 10:
        print("Content in try block after error encountered")
except Exception as exp:
    print("=== Except block ===")
    print(type(exp), "encountered:")   # Exception type
    print("   ", exp)                  # Exception message

### Deal With Different Kinds of Exception

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

### Clean up with `finally`

If we return early (e.g in try-except blocks), the rest of the code won't be excecuted.

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

x = fun(10, "k")

If you some code **must be run** after the try-except blocks, a better way is to use the `finally` block.

`finally` block is a good way to clean up code (such as closing the file).

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

x = fun(10, "k")

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

```
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-40-0dd1cabf5a55> in <module>
----> 1 fun(1.5)

<ipython-input-39-98ccab9d5d44> in fun(prob)
      1 def fun(prob):
      2     if not 0 <= prob <= 1:
----> 3         raise Exception("InvalidProb")
      4     return prob

Exception: InvalidProb
```

You can then capture this exception with an `except` block:

def safeFun(prob):
    try:
        prob = fun(prob)
    except Exception as exp:
        print('Exception encountered: %s' % str(exp))
        prob = 0
    
    return prob

x = safeFun(1.5)