# Windows Persistence Mechanisms (`persistence_in_windows`)

## Overview
Gaining initial access to a system is often fleeting; persistence makes it permanent. In the lifecycle of a cyber attack, maintaining a foothold is critical for long-term engagement, allowing adversaries to survive reboots, retain control, and stage further operations.

This directory contains research, execution scripts, and output logs detailing various Windows Persistence techniques. The project demonstrates how benign system features—such as the Startup folder, Registry keys, Scheduled Tasks, DLL Search Order Hijacking, WMI Subscriptions, and BITS Jobs—can be leveraged to ensure continuous access to a compromised Windows environment.

---

## Learning Objectives
By completing and reviewing this project, the following core concepts are demonstrated:
* **Windows Persistence:** What it is and why it is critical in offensive and defensive cybersecurity operations.
* **Autostart Execution:** Utilizing the Windows Startup folder, Registry Run/RunOnce keys, and Scheduled Tasks for persistent payload delivery.
* **Hijacking Execution Flow:** The risks associated with DLL Search Order Hijacking and how to mitigate them.
* **Event-Driven Persistence:** Leveraging Windows Management Instrumentation (WMI) event subscriptions to execute commands based on system events.
* **Asynchronous Payload Delivery:** Utilizing Background Intelligent Transfer Service (BITS) jobs to download payloads stealthily in the background.

---

## Target Environment & Configuration

* **Operating System:** Windows Virtual Machine (VM)
* **Student Account Credentials:** `Student` / `Student`
* **SuperAdministrator Account Credentials:** `SuperAdministrator` / `Root@123`
* **Allowed Frameworks & Tools:** PowerShell, Metasploit, Cobalt Strike, Sysinternals (Autoruns, Procmon)

---

## Summary of Techniques Covered

### 1. Startup Folder Modification
* **MITRE ATT&CK:** [T1547.001](https://attack.mitre.org/techniques/T1547/001/)
* **Mechanics:** Executable files, batch scripts (`.bat`), or shortcuts (`.lnk`) placed in autostart paths execute automatically upon user logon.
* **Key Paths:**
  * **User-Specific:** `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
  * **Global (All Users):** `%ProgramData%\Microsoft\Windows\Start Menu\Programs\StartUp`

### 2. Registry Run / RunOnce Keys
* **MITRE ATT&CK:** [T1547.001](https://attack.mitre.org/techniques/T1547/001/)
* **Mechanics:** Adding persistent payload string values to specific registry keys under `HKCU` or `HKLM` hives to execute commands on boot or user authentication.
* **Key Paths:**
  * `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  * `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
  * `HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce`

### 3. Scheduled Tasks
* **MITRE ATT&CK:** [T1053.005](https://attack.mitre.org/techniques/T1053/005/)
* **Mechanics:** Creating automated system tasks via `schtasks.exe` or PowerShell (`New-ScheduledTaskAction`) triggered at boot, on user logon, or at specified time intervals.

### 4. DLL Search Order Hijacking
* **MITRE ATT&CK:** [T1574.001](https://attack.mitre.org/techniques/T1574/001/)
* **Mechanics:** Placing a malicious DLL in a directory searched prior to the legitimate system directory, forcing a trusted binary to execute the payload.

### 5. WMI Event Subscriptions
* **MITRE ATT&CK:** [T1546.003](https://attack.mitre.org/techniques/T1546/003/)
* **Mechanics:** Binding a `__EventFilter`, `EventConsumer` (e.g., `CommandLineEventConsumer`), and `__FilterToConsumerBinding` to trigger covert execution when specific system events occur (e.g., system uptime thresholds, user logon).

### 6. BITS Jobs (Background Intelligent Transfer Service)
* **MITRE ATT&CK:** [T1197](https://attack.mitre.org/techniques/T1197/)
* **Mechanics:** Abusing BITS (`bitsadmin` or `Start-BitsTransfer`) to create asynchronous background transfer jobs that download payloads and execute command-line actions upon completion.

---

## Directory Structure

```text
persistence_in_windows/
├── README.md               # Main documentation for the project
├── results.md              # Execution output, evidence, and detailed analysis
├── scripts/                # Tested persistence scripts with descriptive inline comments
│   ├── startup_persist.bat # Startup folder payload execution script
│   ├── registry_persist.ps1# Registry key modification script
│   ├── schtask_persist.ps1 # Scheduled Task creation script
│   ├── wmi_persist.ps1     # WMI Event Subscription script
│   └── bits_persist.ps1    # BITS job creation script
└── payloads/               # Test binaries and scripts (No hardcoded credentials)
