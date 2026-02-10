# AppArmor and Mandatory Access Control (MAC)

## Project Overview

This project focuses on understanding **Mandatory Access Control (MAC)** in Linux systems and how it is implemented using security frameworks such as **SELinux** and **AppArmor**.  
The main goal is to gain a clear and practical understanding of how access control policies are enforced to protect processes, files, and system resources.

This project provides both conceptual knowledge and practical foundations for working with Linux security mechanisms.

---

## Learning Objectives

By the end of this project, you should be able to explain, without using external resources:

- What is MAC in Linux?
- How does SELinux enforce MAC?
- What are the differences between SELinux and AppArmor?
- What is the purpose of policy in MAC systems?
- How do labels work in SELinux?
- What are Type Enforcement, Role-Based Access Control (RBAC), and Multi-Level Security (MLS) in SELinux?
- How can you check the status of SELinux on a system?
- What are common SELinux management commands?
- How do you set file contexts in SELinux?
- What is an AppArmor profile?
- How do you reload AppArmor profiles?
- What is the concept of least privilege in MAC?
- How do you troubleshoot SELinux issues?
- What is the significance of audit logs in MAC systems?
- Can you explain the concept of capabilities in Linux security?
- How to use `semanage`

---

## Resources

Read or watch:

- Introduction to Mandatory Access Control (MAC)
- Your visual how-to guide for SELinux policy enforcement
- 5 security technologies to know in Red Hat Enterprise Linux
- AppArmor: An alternative to SELinux
- Linux Security: MAC, DAC, and RBAC
- Security-Enhanced Linux for mere mortals
- AppArmor vs SELinux: What's the Difference?
- semanage Command with Examples

---

## References

- National Institute of Standards and Technology (NIST) on MAC
- SELinux
- SELinux Project Wiki
- AppArmor Project Wiki
- CentOS Documentation on SELinux
- Arch Linux Wiki on Security
- Linux Kernel Capabilities and MAC
- semanage

---

## Key Concepts

- **Mandatory Access Control (MAC)**  
  A security model in which access decisions are enforced by the system based on defined security policies, not by user discretion.

- **SELinux**  
  A Linux security module that implements MAC using labels and policies.

- **AppArmor**  
  A Linux security module that enforces MAC using application profiles and path-based rules.

- **Policy**  
  A set of rules that defines what actions subjects (processes) can perform on objects (files, sockets, devices, etc.).

- **Labels**  
  Metadata assigned to processes and objects in SELinux and used to make access control decisions.

- **Capabilities**  
  A mechanism that splits root privileges into smaller, fine-grained permissions.

---

## Requirements

### General

- All files will be run on **Kali Linux 2023.2**.
- Allowed editors: `vi`, `vim`, `emacs`.
- You must substitute the IP range for `$1`.

### Scripts

- The first line of all your files must be exactly:
- All files must end with a new line.
- All scripts must be exactly **2 lines long**  
(`wc -l file` must print `2`).
- You are **not allowed** to use `printf`.
- You are **not allowed** to use backticks, `&&`, `||`, or `;`.
- Your code must follow the **Betty style**.
- It will be checked using `betty-style.pl` and `betty-doc.pl`.

---
