---
redirect_from:
  - "/error-handling"
interact_link: content/error_handling.ipynb
kernel_name: python3
has_widgets: false
title: 'Error Handling'
prev_page:
  url: /classes
  title: 'Classes'
next_page:
  url: /requests
  title: 'Request Data from the Web'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Error Handling

## Try, Except, Finally



{:.input_area}
```python
try:
    print("=== Try block ===")
    if "10" > 10:
        print("Content in try block after error encountered")
except:
    print("=== Except block ===")
```


{:.output .output_stream}
```
=== Try block ===
=== Except block ===

```

### Capture Exception Type



{:.input_area}
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


{:.output .output_stream}
```
=== Try block ===
=== Except block ===
<class 'TypeError'> encountered:
    '>' not supported between instances of 'str' and 'int'

```

### Deal With Different Kinds of Exception



{:.input_area}
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


{:.output .output_stream}
```
=== Try block ===

```



{:.input_area}
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


{:.output .output_stream}
```
=== Try block ===
=== Except block 1 ===
TypeError encountered, check input of a

```



{:.input_area}
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


{:.output .output_stream}
```
=== Try block ===
=== Except block 2 ===
ValueError encountered, check input of b

```

### Clean up with `finally`

If we return early (e.g in try-except blocks), the rest of the code won't be excecuted.



{:.input_area}
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




{:.input_area}
```python
x = fun(10, "k")
```


{:.output .output_stream}
```
=== Try block ===
=== Except block 2 ===
ValueError encountered, check input of b

```

If you some code **must be run** after the try-except blocks, a better way is to use the `finally` block.

`finally` block is a good way to clean up code (such as closing the file).



{:.input_area}
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




{:.input_area}
```python
x = fun(10, "k")
```


{:.output .output_stream}
```
=== Try block ===
=== Except block 2 ===
ValueError encountered, check input of b
This is always printed

```

## Raising Exception

To raise a (self-defined) exception in a function, use the expression `raise Exception("exception-name")`.



{:.input_area}
```python
def fun(prob):
    if not 0 <= prob <= 1:
        raise Exception("InvalidProb")
    return prob
```




{:.input_area}
```python
fun(1.5)
```


{:.output .output_traceback_line}
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



{:.input_area}
```python
def safeFun(prob):
    try:
        prob = fun(prob)
    except Exception as exp:
        print('Exception encountered: %s' % str(exp))
        prob = 0
    
    return prob
```




{:.input_area}
```python
x = safeFun(1.5)
```


{:.output .output_stream}
```
Exception encountered: InvalidProb

```
