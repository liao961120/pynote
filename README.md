[![Build Status](https://travis-ci.org/liao961120/pynote.svg?branch=master)](https://travis-ci.org/liao961120/pynote)

# My Notes for Python

## About

This is where I write my notes for Python, which is served at a [web site](https://pynote.netlify.com)

The notes are written with Jupyter notebooks and converted to a web site by [jupyter-book](https://jupyter.org/jupyter-book).

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
