# Privilege Escalation & Security Shells

## 📌 Overview
This section of the project focuses on understanding how system restrictions, restricted shells (like `rbash`), and misconfigured environment permissions can be exploited to achieve **Privilege Escalation**. 

In secure environments, gaining initial access is only half the battle. Security professionals must understand how to leverage local shell features, misconfigured binaries, and environmental weaknesses to break out of restricted environments and elevate execution privileges.

---

## 🚀 Core Concepts Covered

### 1. Restricted Shell Escape (e.g., `rbash`, `rsh`)
* Bypassing environment limitations when commands like `cd` or paths containing slashes (`/`) are blocked.
* Exploiting built-in shell commands and executing alternative environments (`python`, `perl`, `awk`).
* Leveraging **GTFOBins** techniques via authorized binaries (e.g., `less`, `vi`, `man`) to spawn unrestricted shells.

### 2. Environment Variable Manipulation
* Understanding how hijacking `$PATH` or modifying variables like `SHELLOPTS` can lead to unintended execution flows.
* Executing commands through custom paths when administrative restrictions are weak.

### 3. Privilege Escalation Vectors
* Identifying and exploiting binaries with **SUID/SGID** flags set.
* Leveraging misconfigured `sudo` rights without proper command validation.

---

## 🛠️ Constraints & Execution
* **Platform:** Kali Linux
* **Script Rule:** Every automated solution or command script in this directory must be **exactly 1 line long** (`wc -l` must return `1`).
* **Format:** Files must terminate with a valid newline character (`\n`).

---

## 📂 Task Artifacts

| File / Script Name | Objective | Constraint |
| :--- | :--- | :--- |
| `privilege_escalation_security_shells` | One-line payload/command designed to escape a restricted shell or demonstrate privilege escalation. | Exactly 1 line |
