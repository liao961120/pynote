#!/usr/bin/env sh
set -e

jupyter-book build ./
echo 'https://pynote.netlify.app/* https://pynote.yongfu.name/:splat 301!' > _redirects

git add -A
git commit -m 'deploy'
git push -f https://github.com/liao961120/pynote.git master:web

cd -
