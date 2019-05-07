# My Notes for Python

## About

This is where I write my notes for Python. A web site is generated from the notes here, which can be found at <https://pynote.netlify.com>

Each page of this web site is generated from a Jupyter notebook. You can find the source of these notes at [liao961120/pynote](https://github.com/liao961120/pynote)

## Build the Site

The web site is built by the following steps: 

1. Convert Jupyter notebooks to markdown documents (by [nbconvert](https://github.com/jupyter/nbconvert))
1. Turn the md documents into a web site with Jekyll  
(Auto-generated by GitHub Pages in the `docs/` folder in the repo)

or more simply, just run:

```bash
bash build.sh
```

Note that in order to create yaml frontmatter (for Hugo) in the markdown documents generated from the Jupyter notebooks, each Jupyter notebook begins with a raw block with yaml frontmatter written in it:

```yaml
---
title: Configuration
weight: 5
chapter: true
---
```

## Web Site Theme

The theme of the web site is copied from <https://github.com/matcornic/hugo-theme-learn>
