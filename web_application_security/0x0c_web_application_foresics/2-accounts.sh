#!/bin/bash
tail -n 1000 auth.log | grep 'sudo:session' | sort | uniq -c | sort -nr | head -n 1 | awk '{print $12}'
