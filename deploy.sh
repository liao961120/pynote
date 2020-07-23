#!/usr/bin/env sh
set -e

jupyter-book build ./
echo 'https://pynote.netlify.app/* https://pynote.yongfu.name/:splat 301!' > _redirects

read -p "Commit message: " msg
git add -A
git commit -m "${msg}"
git push origin master

