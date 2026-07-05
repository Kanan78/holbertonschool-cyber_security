# 0x00. What The Shell?

## 📌 Overview
This repository/section marks the beginning of the advanced shell scripting and command bypass journey. Before learning how to bypass security restrictions, we must understand the core environment we are operating in: **The Shell**.

A shell is a command-line interpreter that acts as an interface between the user and the operating system kernel. In cybersecurity and system administration, mastering the shell—whether it is Bash in Linux or PowerShell/CMD in Windows—is fundamental for automation, defense auditing, and post-exploitation.

---

## 🎯 Learning Focus
This module explores the foundational mechanics of shell environments:
* **The Kernel vs. The Shell:** Understanding how the shell translates user input into system calls.
* **Flavors of Shells:** Differentiating between traditional POSIX shells (sh, Bash), Windows Command Prompt (CMD), and modern object-oriented environments like **PowerShell**.
* **Cross-Platform Scripting:** How PowerShell operates seamlessly across Linux and macOS.
* **Environment Execution:** How scripts are read, parsed, and executed by the system.

---

## ⚙️ Constraints & Requirements
* **Platform:** Kali Linux
* **Script Constraint:** The script/payload file associated with this task must be **exactly 1 line long**.
  > Running `wc -l 0x00_what_the_shell` must print exactly `1`.
* **Formatting:** The file must end with a valid newline character (`\n`).
* **Allowed Editors:** `vi`, `vim`, `emacs`.

---

## 📂 Task Directory

| File Name | Description | Constraints |
| :--- | :--- | :--- |
| `0x00_what_the_shell` | A one-line script or command that demonstrates basic shell interaction, identification, or environment printing. | Exactly 1 line |

---

## 💡 Quick Tips for This Task
Since the file **must** be exactly one line long, you can verify your script's line count directly in your Kali Linux terminal before submitting:

```bash
wc -l 0x00_what_the_shell
