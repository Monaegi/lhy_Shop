#!/usr/bin/env bash

# TravisCI에 전달할 secrets를 포함해서 최신 커밋을 수정 후 push
#  dev브랜치로만 push하며, master는 TravisCI에서 자동 merge한다
#  (Travis에서 script_merge.sh를 실행)
tar -cvf secrets.tar .secrets
travis encrypt-file secrets.tar --add -f
git add -A
git commit --amend --no-edit
git push origin dev
