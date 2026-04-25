#!/bin/bash
nmap -sV -A --script banner ssl-enum-ciphers smb-enum-domains default $1 -oN service_enumeration_results.txt
