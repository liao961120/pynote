---
interact_link: content/requests.ipynb
kernel_name: python3
has_widgets: false
title: 'Requests Data from the Web'
prev_page:
  url: /error_handling
  title: 'Error Handling'
next_page:
  url: https://github.com/liao961120/pynote
  title: 'GitHub'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Requests

## URLs

```
<protocal>://<domain>/<path>
https://www.ptt.cc/bbs/Gossiping/search?q=thread%3A%nhk
```

- protocal: `https`
- domain: `www.ptt.cc`
- path: `/Gossiping/search?q=thread%3A%nhk`

## Request Params

`/search?q=thread%3A%nhk`

1. after `?`
1. `<key>=<value>`: `q=thread%3A%nhk`
1. multiple params: `<key1>=<value1>&<key2>=<value2>`




{:.input_area}
```python
import requests

search_term = '總統'

base_url = 'https://www.ptt.cc/bbs/Gossiping/search'
cookies = {'over18': '1'}
params = {'q': search_term}

rq = requests.get(base_url, cookies=cookies, params=params)
print(rq.url)
print()
print(rq.text[:150])
```


{:.output .output_stream}
```
https://www.ptt.cc/bbs/Gossiping/search?q=%E7%B8%BD%E7%B5%B1

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>總統 - Gossipin

```

## Wrappers: [`searchPTT.py`](https://github.com/liao961120/pynote/tree/master/content/searchPTT.py)



{:.input_area}
```python
import searchPTT

rq = searchPTT.search('總統', board='Gossiping')
print(rq.url)
print()
print(rq.text[:200])
```


{:.output .output_stream}
```
https://www.ptt.cc/bbs/Gossiping/search?q=%E7%B8%BD%E7%B5%B1

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>總統 - Gossiping - 批踢踢實業坊</title>

<link rel="stylesheet" type="t

```



{:.input_area}
```python
rq = searchPTT.search('EbinaHina', mode='author', board='Gossiping')
print(rq.url)
print()
print(rq.text[:200])
```


{:.output .output_stream}
```
https://www.ptt.cc/bbs/Gossiping/search?q=author%3AEbinaHina

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>author:EbinaHina - Gossiping - 批踢踢實業坊</title>

<link rel="style

```



{:.input_area}
```python
rq = searchPTT.search('thread:[爆卦] 突擊罷工 長榮協商對話整理', mode='thread', board='Gossiping')
print(rq.url)
print()
print(rq.text[:200])
```


{:.output .output_stream}
```
https://www.ptt.cc/bbs/Gossiping/search?q=thread%3Athread%3A%5B%E7%88%86%E5%8D%A6%5D+%E7%AA%81%E6%93%8A%E7%BD%B7%E5%B7%A5+%E9%95%B7%E6%A6%AE%E5%8D%94%E5%95%86%E5%B0%8D%E8%A9%B1%E6%95%B4%E7%90%86

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>thread:thread:[爆卦] 突擊罷工 長榮協商對話整理 - Gossiping - 批踢踢實業坊</title>



```
