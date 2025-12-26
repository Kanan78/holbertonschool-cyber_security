#!/bin/bash
whois $1 | awk -F': *' '/^(Registrant|Admin|Tech)/{k=$1; v=$2; if(k~/ Ext$/)k=k":"; if(k~/Street$/&&v~/(Suite|suite|Ste|STE|Apt|APT|Apartment|#)/)v=v" "; if(v=="")print k ", "; else print k ", " v}' > $1.csv

