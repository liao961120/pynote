# Reading & Writing Files

## Plain Text

### Read

with open('prac/foo.txt', 'r', encoding='utf-8') as f:
    file = [line.strip() for line in f]

file

### Write

with open('prac/write.txt', 'w', encoding='utf-8') as f:
    for line in file:
        f.write(line + '\n')

## JSON

### Read JSON

#### Read from file

import json

with open("prac/dcard_forums.json") as f:
    data = json.load(f)

print(len(data))
data[0]

#### Read from string

jsonData = """
{"a":1,
"b":2,
"c":3,
"d":4,
"e":5}
"""

json.loads(jsonData)

### Write JSON

#### Write to file

with open("prac/afile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

a_dict = {'a': 1, 'b': 2}
json.dumps(a_dict)

## CSV

### Read: `DictReader`

import csv
import pprint as pp

fpath = 'prac/stock.tsv'
file = open(fpath, "r", encoding='cp950')
csvFile = csv.DictReader(file, delimiter='\t')

pp.pprint(list(csvFile)[:3])
file.close()

fpath = 'prac/stock.tsv'
file = open(fpath, "r", encoding='cp950')
csvFile = csv.DictReader(file, delimiter='\t')

lineCount = 1
for row in csvFile:
    print(int(row['證券代碼']), int(row['成交值(千元)']))
    if lineCount == 5: break 
    lineCount += 1
    
file.close()

### Read: `reader`

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

### Read: Pandas

import pandas as pd

df = pd.read_csv("prac/stock.tsv", sep="\t", encoding="cp950")
df

### Write `PdDataFrame.to_csv()`

df.to_csv("prac/stock.csv", index=False)

### Write `PdDataFrame.to_json()`

df.iloc[:2,:]

df.iloc[:2,:].to_json("prac/stock.json", orient="records", force_ascii=False)

#### Details of `to_json()`

See [doc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json) for details.

json_str = df.iloc[:2,:].to_json(orient="records", force_ascii=False)
json_str

json.loads(json_str)


```{toctree}
:hidden:
:titlesonly:


classes
error_handling
requests
numpy
pandas
jupyter
django
```
