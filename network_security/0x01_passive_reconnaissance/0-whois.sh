#!/bin/bash
whois $1 | awk -F: '/^(Registrant|Admin|Tech)/{sub(/^ /,"",$2); print $1 "," $2}'
