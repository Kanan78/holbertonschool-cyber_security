Project Overview
This project focuses on mastering Advanced Port Scanning techniques using Nmap on Kali Linux. The primary goal is to understand how TCP/IP flags (SYN, ACK, FIN, PSH, URG) and Window sizes can be manipulated to discover open ports, identify operating systems, and map out firewall rules that standard scans might miss.

Learning Objectives
By the completion of this project, you will be able to explain:

The Difference Between Standard and Advanced Scans: Why raw packet manipulation is superior to standard OS connect calls.

TCP Connect vs. SYN Scans: Understanding the "Half-Open" state and its impact on application logging.

Firewall Rule Detection: Using ACK Scans to determine if a port is "Filtered" or "Unfiltered."

Stealth Techniques: How FIN, NULL, and Xmas scans exploit RFC 793 to bypass SYN-filtering firewalls.

Information Gathering: What advanced scans reveal about network topology and service versions.

Requirements
Environment: All scripts must be executed and tested on Kali Linux.

Script Length: Every script is exactly 2 lines long (wc -l should print 2).

Shebang: The first line of every file must be #!/bin/bash.

Root Privileges: All scripts must start with the sudo command.

Variables: The target IP range must be substituted using $1 without quotes.

Constraints: * No use of echo.

No use of backticks, &&, ||, or ;.

No double " or single ' quotes surrounding $1.

Coding Style: All files must follow the Betty style and end with a new line.
