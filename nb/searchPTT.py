import requests
import re

def search(term, mode="general", board='Gossiping'):
    if mode == "author":
        pat = re.compile('[^a-zA-Z0-9_-]')
        if pat.search(term) is not None: 
            raise Exception('Invalid Author Id.')
        return search_author(term, board)
    elif mode == "thread":
        return search_thread(term, board)
    else:
        return search_general(term, board)

def search_general(term, board):
    base_url = 'https://www.ptt.cc/bbs/{}/search'.format(board)
    cookies = {'over18': '1'}
    # encode url
    params = {'q': term}
    rq = requests.get(base_url, cookies=cookies, params=params)
    return rq

def search_author(term, board='Gossiping'):
    base_url = 'https://www.ptt.cc/bbs/{}/search'.format(board)
    cookies = {'over18': '1'}
    # encode url
    term = 'author:' + term
    params = {'q': term}
    rq = requests.get(base_url, cookies=cookies, params=params)
    return rq

def search_thread(term, board='Gossiping'):
    base_url = 'https://www.ptt.cc/bbs/{}/search'.format(board)
    cookies = {'over18': '1'}
    # encode url
    term = 'thread:' + term
    params = {'q': term}
    rq = requests.get(base_url, cookies=cookies, params=params)
    return rq