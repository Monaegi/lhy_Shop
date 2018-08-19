#!/usr/bin/env bash

# TravisCI에서 실행
#  dev -> master로 자동 merge 스크립트

echo "- Merge Start -"
export GIT_COMMITTER_EMAIL="dev@lhy.kr"
export GIT_COMMITTER_NAME="LeeHanYeong"

echo " Clone repo ($GITHUB_REPO)"
repo_temp=$(mktemp -d)
git clone "https://github.com/$GITHUB_REPO" "$repo_temp"
cd "$repo_temp"

echo " checkout master"
git checkout master
echo " merge current commit"
git merge --ff-only "$TRAVIS_COMMIT"

echo " push to repo"
push_uri="https://$GITHUB_TOKEN@github.com/$GITHUB_REPO"
git push "$push_uri" master >/dev/null 2>&1
echo "- Merge End -"
