# Active Directory Exploitation - Lab Documentation

## Introduction
Active Directory (AD) acts as the central nervous system for enterprise networks, making it a primary target for attackers seeking total control. This project moves beyond individual host security to explore domain-wide compromise. Through this laboratory environment, we analyze the structure of domains and forests, and exploit inherent trust in protocols like Kerberos and NTLM. By mastering techniques such as Kerberoasting, Pass-the-Hash, and DCSync attacks, we demonstrate how a single weak configuration can lead to full infrastructure dominance.

---

## Learning Objectives
By the end of this project, you will be able to explain and demonstrate:
* How to identify attack surfaces in Active Directory (AD).
* The inner workings of Kerberos authentication, Kerberoasting, Golden Ticket, and Pass-the-Hash (PtH) attacks.
* Exploitation techniques targeting NTLM authentication vulnerabilities.
* The structure of Active Directory (domains, forests, domain controllers, and trusts).
* Service Principal Names (SPNs) and their role in Windows environments.

---

## Lab Environment & Requirements
* **Domain Controller:** Windows Server 2019 (Host: `DC01`, Domain: `PENTESTLAB.local`, IP: `192.168.56.20`)
* **Attacker Machine:** Kali Linux (All operations, enumeration, and exploits are performed from this machine).
* **Network Configuration:** Host-Only / Internal Network (Both machines must reside in the same subnet).
* **Allowed Editors:** `vi`, `vim`, `emacs`

### Primary Tools Used
* `ldapsearch`
* `crackmapexec` / `netexec`
* `impacket-secretsdump`
* `smbclient`

---

## Task Walkthrough & Exploitation Chain

### Task 1: Active Directory User Enumeration via SMB
* **Objective:** Enumerate all domain users and their description fields to find credentials exposed by administrators for convenience.
* **Commands & Methodology:**
  ```bash
  # Enumerating domain users and descriptions using netexec/crackmapexec
  nxc smb 192.168.56.20 -u '' -p '' --users
