#!/bin/bash
whois holbertonstudents.com | awk -F: '/^(Registrant|Admin|Tech)/{print $1 "," $2}'
