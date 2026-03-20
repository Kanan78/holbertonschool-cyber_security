#!/bin/bash
sudo nmap --scanflags -p "$2" -oN custom_scan "$1" > /dev/null 2>&1
