#!/bin/bash
subfinder -d "$1" -ip -silent | awk '{gsub(/[\[\]]/,""); print $1","$2}' > "$1".csv
