# Active Directory Security: Understanding Kerberoasting & Restricted SMB Shares

## Introduction
This repository serves as a conceptual and educational guide on **Kerberoasting**—a common post-exploitation technique used by adversaries to bypass modern defenses within Active Directory (AD) environments. It also highlights how misconfigured Network Shares (SMB) can amplify the impact of compromised service accounts.

---

## What is Kerberoasting?

Kerberoasting is an attack vector that targets standard domain user accounts that have a **Service Principal Name (SPN)** registered (e.g., MSSQL, IIS, or Backup services). The primary goal of the attacker is to request a service ticket from the Domain Controller and crack its cryptographic password hash offline.

### How the Attack Works (Conceptually)

1. **SPN Discovery:** Any authenticated domain user (even with minimal privileges) can query the Active Directory database to find accounts linked to specific services (SPNs).
2. **Ticket Request:** The attacker requests a **Ticket Granting Service (TGS)** ticket for the discovered SPN from the Domain Controller.
3. **Extraction & Offline Cracking:** Because the TGS ticket is encrypted with the service account's password hash, the attacker extracts this ticket from memory and attempts to brute-force the password offline using tools like `Hashcat` or `John the Ripper`.

Since the cracking process happens entirely on the attacker's local machine, it triggers **zero network alerts** or account lockout logs on the Domain Controller.

---

## The Danger of Restricted SMB Shares

Securing the service account is only half the battle. In many enterprise environments, service accounts are granted excessive permissions on network shares to perform automated tasks (such as automated database backups, log processing, or deployment scripts).

If an attacker successfully cracks a service account's password via Kerberoasting, they inherit all the network access tied to that account. This often leads to:
* **Unauthorized Data Access:** Gaining entry to restricted administrative, financial, or custom application shares (e.g., `KerberosFlag`, `AdminProof`, or `Backups`).
* **Privilege Escalation:** Locating cleartext configuration files or scripts stored within hidden shares to compromise higher-level assets.
* **Data Exfiltration:** Secretly copying or modifying corporate assets.

---

## Defensive Countermeasures & Remediation

To mitigate Kerberoasting and secure network shares, organizations should enforce the following security best practices:

### 1. Implement Group Managed Service Accounts (gMSAs)
Traditional user accounts should not be used to run services. Instead, migrate to **gMSAs**. Group Managed Service Accounts utilize complex, 240-character automatically managed passwords that are updated by Active Directory periodically, rendering offline cracking attempts mathematically impossible.

### 2. Enforce AES Encryption for Kerberos
By default, older environments may still support **RC4-HMAC** encryption for Kerberos tickets, which is highly vulnerable to rapid brute-forcing. Enforcing **AES-256 (AES256-CTS-HMAC-SHA1-96)** significantly increases the computational cost and time required to crack a hash.

### 3. Apply the Principle of Least Privilege (PoLP)
Review and tightly restrict network share Access Control Lists (ACLs). Service accounts should only have access to the exact directories they require to function, rather than general read/write permissions across domain-wide shares.

### 4. Continuous Monitoring and Auditing
* Monitor Event ID **4769** (A Kerberos service ticket was requested) on Domain Controllers, focusing on unusual spikes or requests utilizing legacy encryption options (like RC4/Type 23).
* Audit share access and monitor anomalous authentication behavior from non-standard service host machines.
