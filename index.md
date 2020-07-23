# My Notes for Python

<img src="https://travis-ci.org/liao961120/pynote.svg?branch=master" class="left">

## About

This is where I put my notes for Python. The notes are written with Jupyter notebooks and converted to a web site by [jupyter-book](https://jupyter.org/jupyter-book).


## Writing Notes

After putting one notebook in `nb/`, remember to add TOC information in `_toc.yml`.


## Build the Site

The web site is built with the following command: 

```bash
jupyter-book build ./
```

which generates the web site in `_build/html/`


I use netlify and Travis-CI to build the web site for me.
