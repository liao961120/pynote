# Pandas

[Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

import pandas as pd

df = pd.DataFrame({
    "a" : [4 ,4, 6, 5],
    "b" : [7.0, 8.0, 9.0, 15.0],
    "c" : [10.0, 11.0, 12.0, 20.0],
    "text": ['我', '今天', '沒', '吃飽']
})

df

## Basic Data Frame Manitpulation

### Sort Values

- `df.sort_values('a')`
- `df.sort_values('a',ascending=False)`

### Columns

- `df.drop(columns=['a','c'])`
- `df[list_of_COLNAMES]`: `df[['a','b','c']]`
    - returns df
- `df.select_dtypes(include=['float64'])`
- `df.select_dtypes(exclude=['float64'])`
- `df[COLNAME]`: `df['width']`
    - returns series

### Rows

- `df.head()`, `df.tail()`
- `df.iloc[:3]`
- `df[df["a"] > 4]`, `df[~(df["a"] > 4)]`  `df[df['a'].isin({5, 6})]`
- `df.drop_duplicates()`
- `df.sample(frac=0.5)`, df.sample(n=100)


### Rows + Columns

- `df.iloc[:3, [0, 2]]`
- `df.iloc[:3][['a', 'b']]`


### Cell Value

df.at[num, colname]:

- `df.at[0, 'c']`
- assign: `df.at[0, 'new_text'] = '今天星期一'`

## Text Processing

df[df["text"].str.match('..')]

df[df["text"].isin({'我', '沒'})]

df.at[0, 'new_text'] = '今天星期一'
df

## Iteration

for i, row in df.iterrows():
    print(i)
    print(f"Cell 0: {row[0]}")
    print(f"Cell 1: {row[1]}")
    print(f"Cell 2: {row[2]}")
    print(f"Cell 3: {row[3]}")
    print()

day = list('日一二三四五六')

for i, row in df.iterrows():
    df.at[i, 'new_text'] = f"今天星期{day[i]}"

df

for col in df:
    print(f"Colname: {col}")

## Plotting

### Setting up `matplotlib` display options in Jupyter notebook

import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['font.family'] = ['AR PL KaitiM Big5']  # Custom font (installed on computer, .ttf format)
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']    # Custom font (installed on computer, .ttf format)
plt.rcParams.update({'font.size': 18})
plt.rcParams['axes.unicode_minus'] = False

df['a'].plot.hist()

df[['a', 'b']].plot.hist(alpha=0.5)

df[['a', 'b']].plot.hist(subplots=True, layout=(1,2), figsize=(10, 4))

df.plot.bar(x='text', y='b', rot=55) 

## Miscellaneous

df.corr()

df.select_dtypes(exclude=['float64'])

df.select_dtypes(include=['float64']).to_numpy()