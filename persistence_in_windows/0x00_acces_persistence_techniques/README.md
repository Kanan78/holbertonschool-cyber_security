# Windows Persistence Techniques Project

## Overview
Gaining initial access to a system is often fleeting; persistence makes it permanent. In the lifecycle of a cyber attack, maintaining a foothold is critical for long-term engagement, allowing adversaries to survive reboots, retain control, and stage further operations.

This project explores the mechanics of Windows Persistence by examining how benign system features—such as the Startup folder, Registry keys, Scheduled Tasks, DLL Hijacking, WMI Subscriptions, and BITS jobs—can be leveraged to ensure continuous access to a compromised endpoint.

---

## Learning Objectives
By completing this project, the following concepts are demonstrated and documented:
* **Windows Persistence:** What it is and why it is critical in offensive and defensive cybersecurity operations.
* **Autostart Mechanisms:** Utilizing the Windows Startup folder, Registry Run/RunOnce keys, and Scheduled Tasks for persistent execution.
* **Hijacking Execution Flow:** The risks associated with DLL Search Order Hijacking and its mitigation.
* **Event-Driven Execution:** Leveraging Windows Management Instrumentation (WMI) event subscriptions to execute payloads upon specific system triggers.
* **Asynchronous File Transfers:** Utilizing Background Intelligent Transfer Service (BITS) jobs to stealthily download malicious payloads.

---

## Prerequisites & Environment Settings

### Target System Details
* **Environment:** Windows Virtual Machine (VM)
* **Student Account:** `Student` / `Student`
* **SuperAdministrator Account:** `SuperAdministrator` / `Root@123`

### Allowed Tools & Frameworks
* **PowerShell** (v5.1+)
* **Metasploit Framework**
* **Cobalt Strike**
* **Sysinternals Suite** (Autoruns, Process Monitor, etc.)

---

## Persistence Techniques Covered

### 1. Startup Folder Modification
* **MITRE ATT&CK:** [T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
* **Description:** Executables, batch scripts (`.bat`), or shortcut files (`.lnk`) placed in the user or global Startup directory execute automatically upon user logon.
* **Locations:**
  * **Current User:** `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
  * **All Users (Global):** `%ProgramData%\Microsoft\Windows\Start Menu\Programs\StartUp`

### 2. Registry Run Keys & Services
* **MITRE ATT&CK:** [T1547.001](https://attack.mitre.org/techniques/T1547/001/) / [T1543.003](https://attack.mitre.org/techniques/T1543/003/)
* **Description:** Adding payload path entries to Windows Registry keys that automatically run during system boot or logon.
* **Key Registry Paths:**
  * `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  * `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
  * `HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce`

### 3. Scheduled Tasks
* **MITRE ATT&CK:** [T1053.005 - Scheduled Task/Job: Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)
* **Description:** Creating automated tasks using `schtasks.exe` or PowerShell `ScheduledTasks` module to trigger payloads at set times, system boot, or on user idle.

### 4. DLL Search Order Hijacking
* **MITRE ATT&CK:** [T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001/)
* **Description:** Exploiting the Windows DLL search order by placing a malicious DLL in a directory searched before the legitimate system directory.

### 5. WMI Event Subscriptions
* **MITRE ATT&CK:** [T1546.003 - Event-Triggered Execution: Windows Management Instrumentation Event Subscription](https://attack.mitre.org/techniques/T1546/003/)
* **Description:** Configuring WMI `__EventFilter`, `EventConsumer`, and `__FilterToConsumerBinding` to execute payloads silently in response to system events (e.g., system startup, screen unlock).

### 6. BITS Jobs (Background Intelligent Transfer Service)
* **MITRE ATT&CK:** [T1197 - BITS Jobs](https://attack.mitre.org/techniques/T1197/)
* **Description:** Abuse of BITS to schedule asynchronous, background HTTP/SMB downloads that remain persistent across reboots and trigger command execution upon transfer completion.

---

## Repository Structure

```text
.
├── README.md               # Main project documentation and concepts overview
├── results.md              # Detailed output and analysis for each tested technique
├── scripts/                # Documented scripts for persistence mechanisms
│   ├── startup_persist.bat # Startup folder payload execution script
│   ├── registry_persist.ps1# Registry key persistence setup script
│   ├── schtask_persist.ps1 # Scheduled Task creation script
│   └── wmi_persist.ps1     # WMI Event Subscription installation script
└── payloads/               # Test binaries and scripts (No hardcoded credentials)
