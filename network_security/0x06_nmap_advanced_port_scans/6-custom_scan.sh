#!/bin/bash
sudo nmap --scanflags URGACKPSHRSTSYNFIN -p $2 -oN custom_scan.txt -d $1
