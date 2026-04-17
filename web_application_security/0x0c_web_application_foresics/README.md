# Digital Forensics and Network Security (Linux Firewalls)

## Description
This project covers the fundamentals of Digital Forensics and Incident Response (DFIR), with a specific focus on Linux network security using `iptables` and `firewalld`. It explores how to analyze web application logs, investigate network traffic, and manage firewall policies to secure Kali Linux environments.

## Resources
* **Concepts:** Computer Forensics, Cyber Forensic Investigations, Types of Forensics.
* **Technical:** Linux IPtables, Linux Firewalls, Firewalld vs. Iptables.
* **Reports:** DFIR Reports and Log Analysis.

## Learning Objectives
By the end of this project, the following concepts should be understood without external assistance:
* **Digital Forensics:** Core principles and legal frameworks.
* **Web Application Forensics:** Analyzing `access.log` and `auth.log` to trace attack origins.
* **Network Analysis:** Using Wireshark and Burp Suite for forensic investigations.
* **Firewall Management:** Differentiating between and configuring `iptables` and `firewalld`.
* **Incident Response:** Identifying vulnerabilities and documenting forensic findings in professional reports.

## Requirements
* **Operating System:** All scripts are tested on **Kali Linux**.
* **Allowed Editors:** `vi`, `vim`, `emacs`.
* **Script Standards:**
    * All files must end with a new line.
    * The first line of every script must be `#!/bin/bash`.
    * All files must be executable.
    * **Prohibited:** Use of backticks (`` ` ``), `&&`, `||`, or `;` is not allowed.
    * **Style:** Code must adhere to the **Betty style** (checked via `betty-style.pl` and `betty-doc.pl`).
    * **Arguments:** Use `$1` without quotes to prevent unintended argument type alterations.

## Files
| File | Description |
| :--- | :--- |
| `README.md` | Project documentation and objectives. |
| `auth.log` | System authentication logs used for forensic analysis. |
| `dmesg` | Kernel-ring buffer information for hardware and driver diagnostics. |

## Usage
To execute any script in this project, ensure it has executable permissions:
```bash
chmod +x <script_name>
./<script_name>
