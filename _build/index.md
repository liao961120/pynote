---
title: 'Home'
prev_page:
  url: 
  title: ''
next_page:
  url: /classes
  title: 'Classes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# My Notes for Python

<img src="https://travis-ci.org/liao961120/pynote.svg?branch=master" class="left">

## About

This is where I put my notes for Python. The notes are written with Jupyter notebooks and converted to a web site by [jupyter-book](https://jupyter.org/jupyter-book).

## Build the Site

The web site is built with the following commands: 

```bash
make clean
make book
```

After the web site is built, it can be served with Jekyll:

```bash
jekyll build
# jekyll serve  # locally
```

I use netlify and Travis-CI to build the web site for me.
