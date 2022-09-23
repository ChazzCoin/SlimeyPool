#!/bin/zsh


rm -rf completed/
mkdir completed

git add .
git commit -m "automated changes"
git push origin main