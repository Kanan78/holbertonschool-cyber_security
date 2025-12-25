#!/bin/bash
whois "$1" | awk -F: '{v=$2; sub(/^[ \t]+/,"",v); if($1~/Street/){v=v" "} if($1~/Ext/ && v=="") v=":"; printf "%s:%s", $1, v ORS}' | tr -d '\n' && echo
