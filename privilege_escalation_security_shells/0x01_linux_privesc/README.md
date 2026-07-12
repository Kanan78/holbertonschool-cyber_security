# Shell Mechanics, Restrictions, and Command Obfuscation

This repository contains defensive and offensive shell script solutions focused on navigating hardened environments, bypassing string filters, escaping restricted execution environments, and understanding core shell internals across both POSIX and Windows subsystems.

---

## 📋 Learning Objectives

*   **Shell Architecture:** Core execution principles of modern command interpreters (`Bash`, `PowerShell`).
*   **Filter Evasion & Obfuscation:** Utilizing wildcard expansion (globbing), character interpolation, variable slicing, and encoding to bypass static string blacklists.
*   **Restricted Environments:** Mechanisms of restricted shells (`rbash`) and strategies for environmental breakout.
*   **Cross-Platform Automation:** Administrative paradigms of scripting engines, syntax deviations between standard DOS `CMD` and object-oriented `PowerShell`.

---

## 🛠️ Project Requirements

*   **Permitted Editors:** `vi`, `vim`, `emacs`
*   **Target OS Environment:** Kali Linux
*   **Script Constraints:** Every script file must contain exactly **1 line** of execution logic (`wc -l` must output `1`).
*   **Formatting:** All source files must terminate with a valid trailing newline character.

---

## 🔍 Key Concepts Covered

### 1. Globbing and Wildcard Expansion
Bypassing strict string matching filters by referencing binary locations via system wildcards without explicit alphanumeric declarations.
```bash
/usr/bin/p?ng -> /usr/bin/ping
