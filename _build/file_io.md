---
redirect_from:
  - "/file-io"
interact_link: content/file_io.ipynb
kernel_name: python3
title: 'File I/O'
prev_page:
  url: /index
  title: 'Home'
next_page:
  url: /classes
  title: 'Classes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Reading & Writing Files

## Plain Text Files

### Read



{:.input_area}
```python
filePath = 'foo.txt'
file = open(filePath, 'r', encoding='utf-8')

for line in file:
    print(line.strip())

file.close()
```


{:.output .output_stream}
```
1. This is file foo.
2. Just for demo, no practical utilities.
3. hahahah
4. This is line 4

6. Line 5 (previous line) is empty

```

#### Wrap up



{:.input_area}
```python
def print_file(filePath):
    file = open(filePath, 'r', encoding='utf-8')

    for line in file:
        print(line.strip())

    file.close()

print_file('foo.txt')
```


{:.output .output_stream}
```
1. This is file foo.
2. Just for demo, no practical utilities.
3. hahahah
4. This is line 4

6. Line 5 (previous line) is empty

```

### Write



{:.input_area}
```python
somestr = 'abp中文字123隨機'

filePath = 'write.txt'
file = open(filePath, 'w', encoding='utf-8')

lineCount = 1
for char in somestr:
    file.write(str(lineCount) + '. ' + char + '\n')
    lineCount += 1

file.close()
```


#### Wrap up: Self-defined `file.writelines()` (No `\n` required)



{:.input_area}
```python
def writelines(fpath, lst):
    file = open(fpath, 'w', encoding='utf-8')

    for ele in lst:
        file.write(str(ele) + '\n')

    file.close()

writelines('writelines.txt', ['This is line 1', 'This is line 2', 3, 4, [1,2,'3'], {'a':1, 'x':2}])
```

