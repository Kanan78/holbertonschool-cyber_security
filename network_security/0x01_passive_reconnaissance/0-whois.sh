#!/bin/bash
whois "$1" | awk -F: '/^(Registrant|Admin|Tech)[[:space:]]/{f=$1;gsub(/[[:space:]]+/,"",f);v=$2;sub(/^[ \t]+/,"",v);if(f~/Street/)v=v" ";if(f~/Ext/&&v=="")v=":";printf "%s,%s%s",f,v,ORS} END{printf ""}'
