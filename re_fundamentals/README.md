# Software Reverse Engineering & Binary Analysis

> "Every program tells a story. Reverse engineering is how you learn to read it."

---

## 📝 Introduction

Modern software runs everywhere—on computers, servers, mobile devices, and embedded systems. Sometimes the source code is not available, but the behavior of the program still matters. 

Security professionals must be able to analyze applications, understand how they work, and identify hidden functionality or vulnerabilities. Learning reverse engineering builds deep technical thinking. It teaches how to examine compiled programs, trace execution flow, and understand system behavior step by step. 

These skills are essential for:
* **Malware Analysis**
* **Vulnerability Research**
* **Incident Response**
* **Software Security Testing**

Understanding what a program does internally allows defenders to detect threats, verify software integrity, and protect critical systems.

---

## 🔍 Context

During a security investigation, a company discovered an unknown program running on one of its servers. The application had no documentation, and its purpose was unclear. 

System logs showed unusual network connections, but there was no obvious error or alert. Security analysts began examining the file carefully. By analyzing the program structure and monitoring its behavior, they identified hidden functions that were collecting system information and sending it to an external server. The issue was not visible to normal users, but detailed analysis revealed the risk.

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* What reverse engineering is in software.
* Why reverse engineering is important in malware analysis, vulnerability research, and software compatibility.
* What disassembly is, and how it translates machine code into assembly language.
* What decompilation is, and how it differs from disassembly.
* How code flow analysis helps in understanding program logic.
* What techniques are used to identify functions in binaries.
* What the common disassemblers (**IDA Pro**, **Ghidra**, **Radare2**) are, and how they differ.
* How debuggers (**GDB**, **x64dbg**, **OllyDbg**) help in reverse engineering.
* How decompilers (**Hex-Rays**, **RetDec**) convert assembly code to higher-level languages.
* What the role of static analysis tools (**Binwalk**, **Strings**) is in reverse engineering.
* What the main executable file formats (**PE**, **ELF**, **Mach-O**) are, and how they are analyzed.
* How **Control Flow Graphs (CFGs)** help visualize program execution.
* How cross-referencing helps track functions, variables, and data within a program.
* What common anti-reverse engineering techniques are (**obfuscation**, **packing**, **anti-debugging**).
* How to bypass anti-reverse engineering techniques.
* How to use common reverse engineering techniques in real-world CTF challenges.

---

## 🛠 Requirements & Guidelines

### General Guidelines
* **Target Binary:** For this project, your focus will be on the target `target_binary`.
* **Allowed Tools:** `objdump`, `readelf`, `ldd`.
* **Execution Environment:** All analyses **must** be conducted in a controlled environment, such as a Virtual Machine (VM) or Sandbox.
* **OS & Compatibility:** All scripts must be executable and runnable on **Kali Linux**.
* **Paths & Code Quality:** Avoid hardcoded paths; always utilize **relative paths** in your scripts.
* **Offline Requirement:** You are **not allowed** to use online tools or services for your analysis; everything must be executed locally.

### Best Practices
* Ensure that all files are backed up regularly during the analysis process.
* Validate the integrity of the binaries before analyzing them.
* All analysis findings should be organized and clearly formatted for easy reference.

---

## 📚 Resources

### Read or Watch
* **OpenSecurityTraining:** *Intro to x86*
* **Reverse Engineering Fundamentals**
* **Ghidra Tutorial Series**

### Recommended Books & Articles
* *Reverse Engineering for Beginners*
* *Practical Reverse Engineering*
* *The IDA Pro Book*

### Tools Stack
* **Disassemblers / Decompilers:** IDA Pro, Ghidra, Radare2
* **Debuggers:** x64dbg, OllyDbg, GDB
