#!/bin/bash
# Make sure you have the docker image jgoldfar/pandoc-nbconvert-docker on your computer

for f in *.ipynb; do
    docker run --rm -v `pwd`:/source --user $(id -u):$(id -g) jgoldfar/pandoc-nbconvert-docker nbconvert ${f} --to markdown
    
    filename=$(basename -- "$f")
    extension="${filename##*.}"
    filename="${filename%.*}"
    
    mv ${filename}'.md' *_files docs/content/notes
done
