# Active Directory Attack Path Analysis Lab

## 📌 Project Overview
This repository documents a structured, hands-on Active Directory (AD) attack path analysis mimicking a real-world enterprise compromise. Starting as a low-privileged infrastructure intern (`bh_intern`), the objective is to leverage misconfigurations, abuse Access Control Lists (ACLs), execute credential attacks, and chain vulnerabilities together using **BloodHound** as the primary graph-based analytical weapon until full Domain Compromise is achieved.

The lab bridges the gap between offensive execution (Red Team) and defensive forensic discovery (Blue Team) by analyzing corresponding Windows Event IDs, PowerShell logs, and Group Policy configurations for every step taken.

---

## 🎯 Learning Objectives
* **Graph-Based Security:** Map complex AD relationships to visually expose the shortest paths to Domain Admin.
* **ACL Abuse:** Identify and exploit permissive Object Control Lists (specifically `GenericAll` privileges).
* **Credential Flaws:** Execute targeted credential attacks including **Kerberoasting**, **AS-REP Roasting**, and **Password Spraying**.
* **Post-Exploitation & Persistence:** Execute **DCSync** replication abuse and forge signed **Golden Tickets** via the `krbtgt` secret.
* **Defensive Forensics:** Correlate specific offensive phases with Windows security telemetry (Event IDs, Sysmon, and GPO audits).

---

## 💻 Environment Setup & Architecture
The lab infrastructure is built entirely using standalone virtual machines isolated on a host-only network topology:

* **Attacker Machine:** Kali Linux (Platform for all offensive tooling)
* **Target Domain Controller:** Windows Server 2019 (`DC01.pentestlab.local`)
* **Workstation / Victim:** Windows 11 Enterprise

> **Note:** Initial onboarding credentials provided for the entry-level analyst phase:  
> **Username:** `bh_intern` | **Password:** `User@2025!`

---

## 🛠️ Tooling & Methodology

### Offensive Suite
* **BloodHound & Neo4j:** Active Directory relationship mapping and analytical graph execution.
* **SharpHound / bloodhound-python:** Active Directory ingestion and collection tools.
* **Impacket Suite:** (`GetNPUsers.py`, `GetUserSPNs.py`, `secretsdump.py`) for Kerberos interaction and DCSync execution.
* **Mimikatz:** In-memory credential extraction and Kerberos ticket forging.
* **ldapsearch:** Detailed protocol-specific enumeration for extended hidden attributes.

### Defensive / Forensic Telemetry
* **Windows Event Viewer:** Sifting security logs for forensic markers.
* **PowerShell Transcript Logging:** Auditing script execution artifacts.
* **Group Policy Management Console (GPMC):** Correlating audit policy changes with operational noise.

---

## 📈 Attack Path Phases (The Kill Chain)

```text
[bh_intern Access] ──> [BloodHound Ingestion] ──> [ACL Abuse (GenericAll)] 
                                                               │
[Golden Ticket Persistence] <── [DCSync (krbtgt)] <── [Kerberoasting / AS-REP]# Active Directory Attack Path Analysis Lab

## 📌 Project Overview
This repository documents a structured, hands-on Active Directory (AD) attack path analysis mimicking a real-world enterprise compromise. Starting as a low-privileged infrastructure intern (`bh_intern`), the objective is to leverage misconfigurations, abuse Access Control Lists (ACLs), execute credential attacks, and chain vulnerabilities together using **BloodHound** as the primary graph-based analytical weapon until full Domain Compromise is achieved.

The lab bridges the gap between offensive execution (Red Team) and defensive forensic discovery (Blue Team) by analyzing corresponding Windows Event IDs, PowerShell logs, and Group Policy configurations for every step taken.

---

## 🎯 Learning Objectives
* **Graph-Based Security:** Map complex AD relationships to visually expose the shortest paths to Domain Admin.
* **ACL Abuse:** Identify and exploit permissive Object Control Lists (specifically `GenericAll` privileges).
* **Credential Flaws:** Execute targeted credential attacks including **Kerberoasting**, **AS-REP Roasting**, and **Password Spraying**.
* **Post-Exploitation & Persistence:** Execute **DCSync** replication abuse and forge signed **Golden Tickets** via the `krbtgt` secret.
* **Defensive Forensics:** Correlate specific offensive phases with Windows security telemetry (Event IDs, Sysmon, and GPO audits).

---

## 💻 Environment Setup & Architecture
The lab infrastructure is built entirely using standalone virtual machines isolated on a host-only network topology:

* **Attacker Machine:** Kali Linux (Platform for all offensive tooling)
* **Target Domain Controller:** Windows Server 2019 (`DC01.pentestlab.local`)
* **Workstation / Victim:** Windows 11 Enterprise

> **Note:** Initial onboarding credentials provided for the entry-level analyst phase:  
> **Username:** `bh_intern` | **Password:** `User@2025!`

---

## 🛠️ Tooling & Methodology

### Offensive Suite
* **BloodHound & Neo4j:** Active Directory relationship mapping and analytical graph execution.
* **SharpHound / bloodhound-python:** Active Directory ingestion and collection tools.
* **Impacket Suite:** (`GetNPUsers.py`, `GetUserSPNs.py`, `secretsdump.py`) for Kerberos interaction and DCSync execution.
* **Mimikatz:** In-memory credential extraction and Kerberos ticket forging.
* **ldapsearch:** Detailed protocol-specific enumeration for extended hidden attributes.

### Defensive / Forensic Telemetry
* **Windows Event Viewer:** Sifting security logs for forensic markers.
* **PowerShell Transcript Logging:** Auditing script execution artifacts.
* **Group Policy Management Console (GPMC):** Correlating audit policy changes with operational noise.

---

## 📈 Attack Path Phases (The Kill Chain)

```text
[bh_intern Access] ──> [BloodHound Ingestion] ──> [ACL Abuse (GenericAll)] 
                                                               │
[Golden Ticket Persistence] <── [DCSync (krbtgt)] <── [Kerberoasting / AS-REP]
