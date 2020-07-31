#!/bin/bash
branchName="master"
date=`date`
whoami=`whoami`
git checkout $branchName
commit="automatic commit"
if [ "$1" ]; then commit="$1"; fi
git commit -am "\"$commit\" pull && push by $whoami at ${date::${#date}-4}"
git pull origin $branchName
git add .
git commit -am "\"$commit\" push by $whoami at ${date::${#date}-4}"
git push origin $branchName



