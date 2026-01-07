# Nmap Scanning Project

## Project Overview

This project focuses on understanding and utilizing **Nmap**, a powerful network scanning tool. You will learn how to:

- Understand and explain the functions of Nmap and its various scanning techniques.
- Use Nmap to scan IP addresses and check open ports.
- Perform different types of pings and scans such as ARP, ICMP, TCP, and UDP.
- Enumerate targets and identify services running on a network.

The project is designed to help you get hands-on experience with Nmap in a bash script environment on **Kali Linux**.

## Learning Objectives

At the end of this project, you should be able to explain and perform the following tasks:

- What is **Nmap** and how to use it.
- How Nmap scanning works.
- Understand **Subnetworks** and how they are used in scanning.
- Enumerate targets and understand different types of Nmap scans:
  - ARP Scan
  - ICMP Echo Scan
  - ICMP Timestamp Scan
  - ICMP Address Mask Scan
  - TCP SYN Ping Scan
  - TCP ACK Ping Scan
  - UDP Ping Scan
- Detect what Nmap can identify during a scan.
- Perform basic Nmap commands like scanning IP addresses and checking for open ports.

## Project Requirements

### General Requirements:
- **Allowed Editors**: vi, vim, emacs.
- **Environment**: Kali Linux.
- **Script Constraints**:
  - All scripts must be exactly 2 lines long (no more, no less).
  - The first line of all scripts should be `#!/bin/bash`.
  - No use of backticks, `&&`, `||`, or `;` in scripts.
  - The IP range must be substituted for `$1` (with no quotes around it).
  - All files must end with a new line.
  - Your scripts must adhere to the **Betty style** guidelines.
  - All files must be executable.

### Files to be Submitted:
- Bash scripts (two lines each).
- A `README.md` file explaining your project.
- Scripts should be tested and executed on **Kali Linux**.
- Ensure all files have been checked with `chmod +x` to be executable.

## Script Explanation

Each script will utilize Nmap commands to perform different types of scans. Examples of possible tasks include:

1. **ARP Scan**: Identify devices on a local network using ARP requests.
2. **ICMP Echo Scan**: Ping a target to check its availability.
3. **TCP SYN Scan**: Check if a port is open on the target machine.
4. **UDP Ping Scan**: Check for UDP open ports.

The scripts must be written in a simple format where each one performs a specific scan and takes an IP range as input (`$1`).

### Example of a Simple Scan Script:
```bash
#!/bin/bash
nmap -sn $1

