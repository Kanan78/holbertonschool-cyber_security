# Server-Side Request Forgery (SSRF)

## Resources

### Read or Watch
- [Server Side Request Forgery](https://intranet.hbtn.io/rltoken/7KPd7MJ0D0b6t6QcTMAHxg)
- [Server-Side Request Forgery (SSRF)](https://intranet.hbtn.io/rltoken/FQyxRdzQQPBzkpKpMy5Ecg)
- [What is SSRF](https://intranet.hbtn.io/rltoken/g4FPJtviUBqJ1BtULH_fyw)
- [Find and Exploit Server-Side Request Forgery (SSRF)](https://intranet.hbtn.io/rltoken/37wVD_uhNLl4LwU3YQ__tA)
- [Exploiting Server Side Request Forgery (SSRF) in an API](https://intranet.hbtn.io/rltoken/7F744BAFTyfLtxqGMjk2fA)
- [How to Defend Against Server-Side Request Forgery](https://intranet.hbtn.io/rltoken/seaeWBeAIYrr2KGlmdPOrw)

### References
- [SSRF](https://intranet.hbtn.io/rltoken/y-03CDmN1lHMEJUOyIZEcg)

---

## Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is `SSRF`?
- How does `SSRF` work?
- What is an `SSRF` attack and how does it work?
- What are the types of `SSRF` attacks?
- What is the impact of `SSRF` attacks?
- What are the risks of `SSRF`?
- What are some common `SSRF` attack scenarios?
- How to protect against `SSRF` attacks?
- How to prevent `SSRF` attacks?

---

## Concepts Overview

### What is SSRF?
Server-Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain or IP address of the attacker's choosing.

### How Does SSRF Work?
The attacker crafts a malicious request that causes the vulnerable server to make a request to an internal or external resource. Because the request originates from the server itself, it may bypass firewalls, IP whitelists, and other access controls.

### Types of SSRF Attacks
- **Basic SSRF** – Response is directly returned to the attacker.
- **Blind SSRF** – No response is returned, but the server still makes the request (detected via out-of-band techniques).
- **Semi-blind SSRF** – Partial response or error messages leak information.

### Common Attack Scenarios
- Accessing internal services (e.g., `http://localhost/admin`, `http://169.254.169.254/` for cloud metadata)
- Port scanning internal networks
- Bypassing authentication on internal APIs
- Reading local files via `file://` schemes

### Impact of SSRF
- Unauthorized access to internal systems
- Sensitive data exposure (credentials, metadata, configs)
- Remote Code Execution (in chained attacks)
- Internal network reconnaissance

### How to Prevent SSRF
- Validate and sanitize all user-supplied URLs
- Use an allowlist of permitted domains/IPs
- Disable unnecessary URL schemes (`file://`, `gopher://`, `dict://`)
- Block requests to private/loopback IP ranges (`127.0.0.1`, `10.x.x.x`, `169.254.x.x`)
- Use a dedicated egress proxy with strict outbound filtering
- Apply network-level segmentation to limit server outbound access

---

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- All scripts will be tested on **Kali Linux**
- All scripts must be exactly **one line long** (`$ wc -l file` should print `1`)
- All files must end with a **new line**
- A `README.md` file at the root of the project folder is **mandatory**
- Project target: **Cyber - WebSec 0x08**

> ⚠️ **Note:** All applications are port forwarded — pay close attention to the **port number** when constructing redirect URLs.
