# Project: Cyber - WebSec 0x06: Insecure Direct Object Reference (IDOR)

## Description
This project focuses on understanding, identifying, and mitigating **Insecure Direct Object Reference (IDOR)** vulnerabilities. IDOR is a critical security flaw that occurs when an application provides direct access to objects based on user-supplied input without proper authorization checks.

---

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external help:

* **What is an IDOR?** Understanding the fundamental definition.
* **Definition:** What "Insecure Direct Object Reference" specifically means in a web context.
* **Mechanism:** How IDOR works and how an attack happens.
* **Comparison:** The difference between IDOR and other vulnerabilities (like Broken Access Control).
* **Types:** Different forms of IDOR (URL parameters, body parameters, etc.).
* **Impact:** The potential damage an IDOR exploit can cause to data and privacy.
* **Detection:** How to find IDOR vulnerabilities during security testing.
* **Prevention & Mitigation:** Best practices to secure applications against IDOR.

---

## Resources
### Read or Watch:
* [Insecure Direct Object References (IDOR)](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control)
* [All About Insecure Direct Object Reference (IDOR)](https://portswigger.net/web-security/access-control/idor)
* [IDOR Explained - Deep Dive](https://www.hackerone.com/blog/how-to-find-and-exploit-idor-vulnerabilities)
* [OWASP Top 10: IDOR](https://owasp.org/www-chapter-ghana/assets/slides/IDOR.pdf)

### References:
* [Testing for IDOR](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)
* [IDOR Mitigation Best Practices](https://cwe.mitre.org/data/definitions/639.html)

---

## Requirements
* **Allowed Editors:** `vi`, `vim`, `emacs`.
* **Environment:** All scripts will be tested on **Kali Linux**.
* **Script Format:** All scripts must be exactly **one line long**.
* **File Ending:** All files must end with a new line.
* **Mandatory File:** A `README.md` file at the root of the project folder is required.
* **Target:** Focus on **Cyber - WebSec 0x06**.

---

## Tasks Summary
Investigation of various application areas such as:
1.  Transaction History
2.  User Settings
3.  Profile Management
4.  API Endpoints for ID exposure.
