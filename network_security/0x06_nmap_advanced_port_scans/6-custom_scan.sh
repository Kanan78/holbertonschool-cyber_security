#!/bin/bash
  sudo nmap --scanflags URG,ACK,PSH,RST,SYN,FIN -p $2 -oN custom_scan.txt $1 > /dev/null 2>&1
