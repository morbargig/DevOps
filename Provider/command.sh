#!/bin/bash
branchName="provider"
date=`date`
git checkout $branchName
git add .
commit="automatic commit"
if [ "$1" ]; then commit="$1"; fi
git commit -m "$commit push ${date::${#date}-4}"
git pull origin $branchName
git add .
git commit -m "$commit pull & push ${date::${#date}-4}"
git push origin $branchName