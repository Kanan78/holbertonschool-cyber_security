# Web Application Security - OWASP Top 10

## Description
This project focuses on identifying and exploiting common web application vulnerabilities as defined by the **OWASP Top 10:2021**. The main objective is to understand the underlying mechanics of security flaws such as Session Hijacking, Injection, and Broken Access Control through practical laboratory exercises on the `Cyber - WebSec 0x01` target machine.

## Resources
### Read or watch:
* [OWASP Top 10:2021](https://owasp.org/www-project-top-ten/)
* [Explaining the OWASP Top 10](https://owasp.org/www-project-top-ten/)
* [Understanding the OWASP Top 10 with Examples](https://www.vaadata.com/blog/owasp-top-10-vulnerabilities-examples-and-remediation/)
* [OWASP Top 10 Risks – Mitigation Strategies](https://cheatsheetseries.owasp.org/)
* [How to Choose a Password](https://www.enisa.europa.eu/topics/cyber-threats/passwords)

### References:
* [OWASP Official Website](https://owasp.org/)
* [OWASP ZAP - Web Application Penetration Testing Tool](https://www.zaproxy.org/)
* [OWASP Juice Shop - Vulnerable Web Application](https://owasp.org/www-project-juice-shop/)
* [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)

## Learning Objectives
By the end of this project, you should be able to explain the following without assistance:
* The significance of the **OWASP Top 10** in modern web security.
* Why **Injection** (SQLi, Command Injection) remains a top threat.
* The impact of **XSS (Cross-Site Scripting)** on end-users.
* Risks associated with **Broken Authentication** and **Session Management**.
* How **Security Misconfigurations** and **Broken Access Controls** lead to unauthorized data access.
* The importance of **Security Logging and Monitoring** for incident response.

## Requirements
* **Environment:** All scripts must run on **Kali Linux 2023.2**.
* **Editors:** `vi`, `vim`, or `emacs`.
* **Shebang:** The first line of all scripts must be `#!/bin/bash`.
* **Style:** Code must adhere to the **Betty style** (checked via `betty-style.pl`).
* **Constraints:** * No use of backticks (\`), `&&`, `||`, or `;`.
    * Must substitute the IP range for `$1` where applicable.
    * All files must end with a new line.

## Project Setup
To access the target machine, map the local hostname by running:
```bash
sudo bash -c "echo web0x01.hbtn >> /etc/hosts"
