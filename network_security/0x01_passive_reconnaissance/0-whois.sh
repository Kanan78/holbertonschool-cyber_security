#!/bin/bash
whois $1 | awk -F': *' '/^(Registrant|Admin|Tech)/{k=$1; v=$2; if(k~/Street$/&&v~/(Suite|suite|Ste|STE|Apt|APT|Apartment|#)/)v=v" "; if(k~/ Ext$/)print k ":," v; else print k "," v}' > $1.csv
