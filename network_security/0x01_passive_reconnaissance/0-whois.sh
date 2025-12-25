#!/bin/bash

whois "$1" | awk -F':' '
/^(Registrant|Admin|Tech)/ {
  v=$2
  if($1 ~ /Street/) v=v" "
  f=$1
  if(f ~ /Ext/) f=f":"
  printf "%s,%s%s", f, v, (NR==NR_total?"":"\n")
}
BEGIN{NR_total=0} {NR_total++} END{printf ""}'
