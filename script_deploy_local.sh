#!/usr/bin/env bash

# master브랜치로 이동하며 작업중이던 내용은 stash처리
git stash
current_branch="$(git rev-parse --abbrev-ref HEAD)"
git fetch origin
git checkout master
git merge origin/master

# requirements생성, secrets를 강제로 staging area에 추가
pipenv lock --requirements > requirements.txt
git add -f .secrets/ requirements.txt

# base이미지 빌드 및 push
docker pull azelf/greenwrap:base
docker build -t azelf/greenwrap:base -f ./.dockerfiles/Dockerfile.base .
docker push azelf/greenwrap:base

# deploy시작
eb deploy --profile greenwrap --staged

# 임시로 추가한 secrets와 requirements를 staging area에서 제거
git reset HEAD .secrets/ requirements.txt
# requirements는 삭제
rm requirements.txt

# 작업중이던 브랜치로 이동, 임시저장내역을 다시 불러옴
git checkout $current_branch
git stash apply
