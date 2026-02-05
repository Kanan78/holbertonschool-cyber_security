#!/bin/bash
find $1 -name "*" -type f -exec chmod o=r {} + 2>/dev/null
