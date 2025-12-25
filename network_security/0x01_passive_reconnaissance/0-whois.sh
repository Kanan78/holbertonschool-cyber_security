#!/bin/bash
whois holbertonstudents.com | awk -F: '/^(Registrant|Admin|Tech)/{if($1~/Ext/)print $1 ":," $2; else print $1 "," $2}'
