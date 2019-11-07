---
redirect_from:
  - "/file-io"
interact_link: content/file_io.ipynb
kernel_name: python3
has_widgets: false
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

## Plain Text

### Read



{:.input_area}
```python
filePath = 'prac/foo.txt'
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

print_file('prac/foo.txt')
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

filePath = 'prac/write.txt'
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

writelines('prac/writelines.txt', ['This is line 1', 'This is line 2', 3, 4, [1,2,'3'], {'a':1, 'x':2}])
```


## JSON

### Read JSON

#### Read from file



{:.input_area}
```python
import json

with open("prac/dcard_forums.json") as f:
    data = json.load(f)

print(len(data))
data[0:2]
```


{:.output .output_stream}
```
373

```




{:.output .output_data_text}
```
[{'alias': 'midnightlab',
  'availableLayouts': ['classic'],
  'canPost': False,
  'canUseNickname': True,
  'createdAt': '2016-05-14T19:15:15.698Z',
  'description': '午夜實驗室10/6、10/7即將在華山登場！這裏提供大家交流活動資訊與討論，請大家要遵守 Dcard 板規喔！',
  'fullyAnonymous': False,
  'id': '7f125e07-4460-4ea5-80b5-33f0e9aafa0c',
  'ignorePost': False,
  'invisible': True,
  'isSchool': False,
  'limitCountries': [],
  'limitStage': 0,
  'mediaThreshold': {},
  'name': '午夜實驗室',
  'nsfw': False,
  'postCount': {'last30Days': 0},
  'postThumbnail': {'size': 'small'},
  'read': False,
  'shouldCategorized': False,
  'subcategories': [],
  'subscribed': False,
  'subscriptionCount': 1837,
  'titlePlaceholder': '',
  'topics': ['午夜實驗室'],
  'updatedAt': '2018-11-05T03:24:32.914Z'},
 {'alias': 'timecapsule',
  'availableLayouts': ['classic'],
  'canPost': False,
  'canUseNickname': True,
  'createdAt': '2016-05-14T20:15:15.698Z',
  'description': '寫下你的新年新希望，一年後將收到「時光膠囊」，幫助你檢視這一年達成了多少目標，實現了多少願望！',
  'fullyAnonymous': False,
  'id': 'c0ed3f99-ed1c-49a8-b413-ed5e925aafe4',
  'ignorePost': True,
  'invisible': True,
  'isSchool': False,
  'limitCountries': [],
  'limitStage': 0,
  'mediaThreshold': {},
  'name': '時光膠囊',
  'nsfw': False,
  'postCount': {'last30Days': 0},
  'postThumbnail': {'size': 'small'},
  'read': False,
  'shouldCategorized': False,
  'subcategories': [],
  'subscribed': False,
  'subscriptionCount': 2202,
  'titlePlaceholder': '',
  'topics': [],
  'updatedAt': '2019-01-03T16:02:02.892Z'}]
```



#### Read from string



{:.input_area}
```python
jsonData = """
{"a":1,
"b":2,
"c":3,
"d":4,
"e":5}
"""

data = json.loads(jsonData)
data
```





{:.output .output_data_text}
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```



## CSV

### Read: `DictReader`



{:.input_area}
```python
import csv
import pprint as pp

fpath = 'prac/stock.tsv'
file = open(fpath, "r", encoding='cp950')
csvFile = csv.DictReader(file, delimiter='\t')

pp.pprint(list(csvFile)[:3])
file.close()
```


{:.output .output_stream}
```
[OrderedDict([('證券代碼', '4938   '),
              ('簡稱', '和碩         '),
              ('年月日', '20110103'),
              ('開盤價(元)', '   29.32'),
              ('最高價(元)', '   29.42'),
              ('最低價(元)', '   29.21'),
              ('收盤價(元)', '   29.28'),
              ('成交值(千元)', '       89508')]),
 OrderedDict([('證券代碼', '4938   '),
              ('簡稱', '和碩         '),
              ('年月日', '20110104'),
              ('開盤價(元)', '   29.42'),
              ('最高價(元)', '   29.56'),
              ('最低價(元)', '   29.28'),
              ('收盤價(元)', '   29.42'),
              ('成交值(千元)', '      107340')]),
 OrderedDict([('證券代碼', '4938   '),
              ('簡稱', '和碩         '),
              ('年月日', '20110105'),
              ('開盤價(元)', '   29.42'),
              ('最高價(元)', '   29.42'),
              ('最低價(元)', '   28.16'),
              ('收盤價(元)', '   28.72'),
              ('成交值(千元)', '      193077')])]

```



{:.input_area}
```python
fpath = 'prac/stock.tsv'
file = open(fpath, "r", encoding='cp950')
csvFile = csv.DictReader(file, delimiter='\t')

lineCount = 1
for row in csvFile:
    print(int(row['證券代碼']), int(row['成交值(千元)']))
    if lineCount == 5: break 
    lineCount += 1
    
file.close()
```


{:.output .output_stream}
```
4938 89508
4938 107340
4938 193077
4938 259533
4938 330576

```

### Read: `reader`



{:.input_area}
```python
with open(fpath, 'r', encoding='cp950') as f:
    csvFile = csv.reader(f, delimiter='\t')
    header = next(csvFile)
    print('FIELDNAMES:', header)
    
    lineCount = 1
    for row in csvFile:
        row = [ele.strip() for ele in row]
        print(row)
        
        if lineCount == 5: break
        lineCount += 1
```


{:.output .output_stream}
```
FIELDNAMES: ['證券代碼', '簡稱', '年月日', '開盤價(元)', '最高價(元)', '最低價(元)', '收盤價(元)', '成交值(千元)']
['4938', '和碩', '20110103', '29.32', '29.42', '29.21', '29.28', '89508']
['4938', '和碩', '20110104', '29.42', '29.56', '29.28', '29.42', '107340']
['4938', '和碩', '20110105', '29.42', '29.42', '28.16', '28.72', '193077']
['4938', '和碩', '20110106', '28.93', '29.00', '28.02', '28.20', '259533']
['4938', '和碩', '20110107', '28.02', '28.16', '27.22', '27.32', '330576']

```
