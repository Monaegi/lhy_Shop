#!/usr/bin/env bash
tar -cvf secrets.tar .secrets
travis encrypt-file secrets.tar --add -f
git add -A
git commit --amend --no-edit
git push origin dev
