#!/bin/bash
grep "Accepted password" ~/auth.log | grep "root" |  awk '{print $11}' | sort | uniq | wc -l
