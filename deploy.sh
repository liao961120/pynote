#!/usr/bin/env sh
set -e

read -p "Commit message: " msg

jupyter-book build ./
echo 'https://pynote.netlify.app/* https://pynote.yongfu.name/:splat 301!' > _redirects

git add -A
git commit -m "${msg}"
git push origin master

