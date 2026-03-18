# Nmap Advanced Port Scanning

## Project Overview
This project explores **Advanced Port Scanning** techniques using **Nmap** on **Kali Linux**. It focuses on the manipulation of TCP/IP flags—such as SYN, ACK, FIN, PSH, and URG—to bypass firewalls, identify filtered ports, and map network topologies without triggering standard application logs.

## Learning Objectives
At the completion of this project, you should be able to explain:
* **TCP Connect vs. SYN Scans:** The mechanics of the "Half-Open" stealth scan.
* **Firewall Rule Auditing:** Using **ACK Scans** to differentiate between filtered and unfiltered ports.
* **Stealth Techniques:** How **FIN**, **NULL**, and **Xmas** scans exploit RFC 793 to bypass security filters.
* **Network Reconnaissance:** Detecting operating systems and service versions through advanced fingerprinting.

## Requirements
* **Environment:** All scripts must be executed and tested on **Kali Linux**.
* **Script Structure:** Every script is exactly **2 lines long** (`wc -l` must return 2).
* **Shebang:** The first line of all files must be `#!/bin/bash`.
* **Execution:** All Nmap commands must start with `sudo`.
* **Parameter Handling:** Use the variable `$1` without quotes (`"` or `'`) to handle IP ranges.
* **Constraints:**
    * No use of `echo`.
    * No use of backticks, `&&`, `||`, or `;`.
    * Files must end with a new line and follow the **Betty** style.

## Advanced Scan Types

| Scan Type | Flag | Description |
| :--- | :--- | :--- |
| **SYN Scan** | `-sS` | Stealthy scan that never completes the three-way handshake. |
| **ACK Scan** | `-sA` | Used to determine firewall rulesets and stateful filtering. |
| **Xmas Scan** | `-sX` | Sets FIN, PSH, and URG flags simultaneously. |
| **FIN Scan** | `-sF` | Sets only the FIN bit to bypass certain SYN-filters. |
| **NULL Scan** | `-sN` | Sets no bits in the TCP header to test system response. |
| **Window Scan** | `-sW` | Examines the TCP Window field to differentiate between open/closed ports. |

## Usage
To use the scripts in this repository, provide the target IP or range as the first argument:

```bash
chmod +x <script_name>
./<script_name> 192.168.1.0/24
