#!/usr/bin/env bash
export GIT_COMMITTER_EMAIL="dev@lhy.kr"
export GIT_COMMITTER_NAME="LeeHanYeong"

repo_temp=$(mktemp -d)
git clone "https://github.com/$GITHUB_REPO" "$repo_temp"

cd "$repo_temp"

git checkout master
git merge --ff-only "$TRAVIS_COMMIT"

push_uri="https://$GITHUB_TOKEN@github.com/$GITHUB_REPO"

git push "$push_uri" master >/dev/null 2>&1
