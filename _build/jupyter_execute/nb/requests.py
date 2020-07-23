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


import requests

search_term = '總統'

base_url = 'https://www.ptt.cc/bbs/Gossiping/search'
cookies = {'over18': '1'}
params = {'q': search_term}

rq = requests.get(base_url, cookies=cookies, params=params)
print(rq.url)
print()
print(rq.text[:150])

## Wrappers: [`searchPTT.py`](https://github.com/liao961120/pynote/tree/master/content/searchPTT.py)

import searchPTT

rq = searchPTT.search('總統', board='Gossiping')
print(rq.url)
print()
print(rq.text[:200])

rq = searchPTT.search('EbinaHina', mode='author', board='Gossiping')
print(rq.url)
print()
print(rq.text[:200])

rq = searchPTT.search('thread:[爆卦] 突擊罷工 長榮協商對話整理', mode='thread', board='Gossiping')
print(rq.url)
print()
print(rq.text[:200])