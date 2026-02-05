#!/bin/bash
find $1 -perm /6000 -type f -exec -mtime -1 ls -ldb {} + 2>/dev/null
