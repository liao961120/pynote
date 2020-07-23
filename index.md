# My Notes for Python


## About

This is where I put my notes for Python. The notes are written with Jupyter notebooks and converted to a web site by [jupyter-book](https://jupyter.org/jupyter-book).


## Writing Notes

After putting one notebook in `nb/`, remember to add TOC information in `_toc.yml`.


## Publishing the Site

Simply run the bash script `deploy.sh` to update the site on GitHub.

To build the web site without publishing, run: 

```bash
jupyter-book build ./
```

which generates the web site in `_build/html/`.
