# Active Directory Enumeration & Hardening with PowerView

## 📌 Project Overview
This repository documents a comprehensive, project-based module focusing on Active Directory (AD) infrastructure from both offensive and defensive perspectives. Using **PowerView**, a powerful PowerShell-based reconnaissance tool, we simulate internal threat actor behaviors directly from the command line to discover misconfigurations, over-privileged users, exposed ACLs, and weak Group Policies within the `pentestlab.local` domain. 

In parallel, this module addresses structural defense mechanics by hardening Domain Controllers, deploying **Windows LAPS** (Local Administrator Password Solution), configuring Group Policy Objects (GPOs), and establishing robust auditing metrics to break critical attack paths.

---

## 🎯 Learning Objectives
* **CLI-Based AD Recon:** Understand how PowerView interacts natively with Active Directory via LDAP queries.
* **Object Enumeration:** Map domain architecture including users, functional groups, domain controllers, and trust systems.
* **ACL Exposure Analysis:** Discover over-permissioned entry points and dangerous object controls (`GenericAll`, `WriteDACL`, `GenericWrite`).
* **Policy Auditing:** Enumerate GPO structures and evaluate configuration flaws or cleartext credential leakage.
* **Defense Architecture:** Configure Active Directory hardening baselines using GPOs, AppLocker, and centralized local account isolation (LAPS).

---

## 💻 Environment Setup & Architecture
The testing laboratory operates entirely on pre-configured virtual appliances interconnected via an isolated host-only virtualization network:

* **Attacker Native Platform:** Kali Linux
* **Operational Pivot Workstation:** Windows 11 Enterprise (Acts as the internal insider workstation where PowerView operations are executed)
* **Target Domain Architecture:** Windows Server 2019 Domain Controller

### 🔐 Initial Entry Vectors
* **Target Workstation Username:** `bh_intern`
* **Target Workstation Password:** `User@2025!`

---

## 🚀 Execution Guide (PowerView Initialization)

Before executing enumeration cmdlets on the Windows 11 workstation, the built-in PowerShell execution policy restrictions must be bypassed for the active process container, followed by dot-sourcing the script library.

```powershell
# Step 1: Bypass PowerShell execution constraints for the active scope
Set-ExecutionPolicy Bypass -Scope Process

# Step 2: Dot-source and load PowerView modules into operational memory
. .\PowerView.ps1
