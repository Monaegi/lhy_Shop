#!/usr/bin/env bash
echo "- EB Deploy Start -"
export GIT_COMMITTER_EMAIL="dev@lhy.kr"
export GIT_COMMITTER_NAME="LeeHanYeong"

echo "Branch!"
echo $TRAVIS_BRANCH
if [ ! $TRAVIS_BRANCH = "master" ];then
    echo " Not master branch, deploy aborted"
    exit 1
fi

echo " checkout master"
repo_uri="https://$GITHUB_TOKEN@github.com/$GITHUB_REPO"
git fetch $repo_uri
git merge $repo_uri/master

echo " make requirements, add secrets"
# requirements생성, secrets를 강제로 staging area에 추가
pipenv lock --requirements > requirements.txt
git add -f .secrets/ requirements.txt

echo " make & push base image"
# base이미지 빌드 및 push
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker pull azelf/greenwrap:base
docker build -t azelf/greenwrap:base -f ./.dockerfiles/Dockerfile.base .
docker push azelf/greenwrap:base

echo " eb deploy"
# deploy시작
eb deploy --staged
echo "- EB Deploy End -"
