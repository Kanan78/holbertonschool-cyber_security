#!/bin/bash
whois $1 | awk -F': *' '$1 ~ /^(Registrant|Admin|Tech) (Name|Organization|Street|City|State\/Province|Postal Code|Country|Phone|Phone Ext|Fax|Fax Ext|Email)$/ {k=$1; v=$2; if (k ~ /Street$/) v=v" "; if (k ~ / Ext$/) k=k":"; print k "," v}' > $1.csv
