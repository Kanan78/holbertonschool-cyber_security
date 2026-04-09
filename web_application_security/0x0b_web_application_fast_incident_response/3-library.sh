#!/bin/bash
awk '{print $12}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | cut -d '"' -f2
