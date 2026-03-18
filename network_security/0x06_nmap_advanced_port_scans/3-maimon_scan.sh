#!/bin/bash
sudo nmap -sM -p http*,ftp,ssh,telnet -vv $1
