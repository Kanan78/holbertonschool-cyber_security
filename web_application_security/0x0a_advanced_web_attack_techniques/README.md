# Advanced Web Attack Techniques

> "Security is not a product, but a process." — Bruce Schneier

## Description

This project moves beyond basic vulnerability identification into active exploitation of advanced web attack techniques. Working within a realistic testing scenario, you will encounter subtle behavioral signals — anomalous HTTP requests, unexpected server-side file access, and unusual application responses — and follow those clues systematically to identify, analyze, and exploit vulnerabilities before a real attacker can.

## Learning Objectives

By the end of this project, you will be able to:

- Recognize behavioral indicators of advanced web vulnerabilities in live applications
- Identify and explain the different types of Cross-Site Scripting (XSS)
- Explain how XSS injections work and how they exploit web applications
- Understand insecure deserialization and its impact on web applications
- Understand Server-Side Template Injection (SSTI) and how it is exploited
- Implement prevention techniques for each vulnerability class
- Apply structured methodology to move from discovery to exploitation
- Document findings with the precision expected in professional penetration testing reports
- Integrate security checks into the development lifecycle to prevent vulnerabilities

## Vulnerability Coverage

### Cross-Site Scripting (XSS)

XSS occurs when an attacker injects malicious scripts into content that is then served to other users. There are three main types:

- **Reflected XSS** — The malicious script is embedded in a URL and executed immediately when the victim visits the crafted link. The server reflects user input back into the response without proper sanitization.
- **Stored XSS** — The payload is permanently stored on the server (e.g., in a database) and executed every time a user loads the affected page.
- **DOM-based XSS** — The vulnerability exists entirely in client-side JavaScript. The DOM is manipulated using attacker-controlled data without any server involvement.

**Prevention:** Output encoding, Content Security Policy (CSP), input validation, and using safe DOM APIs (`textContent` instead of `innerHTML`).

### Insecure Deserialization

Insecure deserialization occurs when an application deserializes data from an untrusted source without proper validation. Attackers can manipulate serialized objects to achieve remote code execution, privilege escalation, or denial of service.

**Prevention:** Never deserialize untrusted data, use integrity checks (e.g., digital signatures), prefer data formats like JSON over native serialization, and implement strict type constraints during deserialization.

### Server-Side Template Injection (SSTI)

SSTI occurs when user input is embedded directly into a server-side template and evaluated by the template engine (e.g., Jinja2, Twig, Freemarker). This can lead to remote code execution if the template engine is powerful enough to access system-level functions.

**Prevention:** Never pass raw user input to template rendering functions, use a sandboxed template environment, and treat all user input as data — not as template logic.

## Endpoints

| Task   | Endpoint                          |
|--------|-----------------------------------|
| Task 0 | `http://web0x0a.task0.hbtn/`     |
| Task 1 | `http://web0x0a.task1.hbtn/`     |
| Task 2 | `http://web0x0a.task2.hbtn/`     |
| Task 3 | `http://web0x0a.task3.hbtn/`     |
| Task 4 | `http://web0x0a.task4.hbtn/`     |

> **Note:** Use the IP address in all tasks, not the hostname.

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- All scripts are tested on **Kali Linux**
- All files must end with a new line
- Use the **IP address** in tasks, not the hostname

## Resources

- [What is Cross-Site Scripting (XSS)?](https://intranet.hbtn.io/rltoken/sRmcz6od3qWRquVOfMaXiA)
- [How to Prevent XSS in JavaScript](https://intranet.hbtn.io/rltoken/bL2dHldZ3xRbIlmWS6kw-g)
- [XSS Injection](https://intranet.hbtn.io/rltoken/9DGRrdriQFXoDQSraLrSRQ)
- [Insecure Deserialization](https://intranet.hbtn.io/rltoken/8GYm1oQMVy9bKoiDvg5zDA)
- [PHP Deserialization](https://intranet.hbtn.io/rltoken/WLbgz2nuNbzr-kl0bB5QKw)
- [Preventing Insecure Deserialization Vulnerabilities](https://intranet.hbtn.io/rltoken/R-vuAOzeg_b8YNb1RgeV4Q)
- [Server-Side Template Injection](https://intranet.hbtn.io/rltoken/FRSGngZLDp6v_ohrNrv1fQ)
- [Server-Side Template Injection 2](https://intranet.hbtn.io/rltoken/YC4577U0zlHP_5H52UgjEQ)
- [SSTI: What It Is and How to Prevent It](https://intranet.hbtn.io/rltoken/UFlg_xvr2BbkzAWkiP91cw)
