#!/bin/bash
find $1 -perm -4000 -o -perm -2000 -type f -exec -mtime -1 ls -ldb {} + 2>/dev/null
