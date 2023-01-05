#!/bin/zsh


rm -rf completed/
rm -rf failed/
git reset --hard HEAD
git pull origin main
mkdir completed
mkdir failed