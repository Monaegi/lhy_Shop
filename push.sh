#!/usr/bin/env bash
tar -cvf secrets.tar .secrets
travis encrypt-file secrets.tar --add -f
