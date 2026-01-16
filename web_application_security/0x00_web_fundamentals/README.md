# Web Application Fundamentals

This project covers the core concepts of web infrastructure, architecture evolution, and application security.

## Learning Objectives
* Understand how the Web works and the Request-Response cycle.
* Distinguish between Web 1.0, 2.0, and 3.0.
* Identify Progressive Web Applications (PWA).
* Explain Frontend-Backend communication and CORS.
* Differentiate between Stateful vs. Stateless designs.
* Compare Structured vs. Unstructured data.
* Analyze Web Security Risks (OWASP Top 10) and Bug Bounty Programs.

## Requirements
* **Environment:** Tested on Kali Linux 2023.3.
* **Scripting:** All scripts must be exactly 2 lines long.
* **Shebang:** First line must be `#!/bin/bash`.
* **Style:** Adheres to the Betty style guide.
* **Execution:** All scripts must be executable.
* **Parameterization:** Use `$1` for dynamic IP range substitution.

## Tech Stack
* **Shell:** Bash
* **Security Tools:** `curl`, `sqlmap`
* **Linter:** Betty Style (Perl scripts)

## Files
| File | Description |
| --- | --- |
| `README.md` | Project documentation. |
| `[script_names].sh` | Executable Bash scripts for network and security tasks. |

## Installation
```bash
sudo apt update
sudo apt install curl sqlmap
chmod +x *.sh
