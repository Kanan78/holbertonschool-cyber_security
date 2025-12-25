#!/bin/bash
whois "$1" | awk -F: '/^(Registrant|Admin|Tech)/{v=$2; sub(/^[ \t]+/,"",v); if($1~/Street/)v=v" "; if($1~/Ext/ && v=="")v=":"; printf "%s, %s%s", $1, v, ORS}'
