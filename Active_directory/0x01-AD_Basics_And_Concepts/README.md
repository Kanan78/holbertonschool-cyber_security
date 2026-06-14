# Active Directory Architecture and Exploitation Lab

## Description
This project focuses on the architecture, inner workings, and security vulnerabilities
of Active Directory (AD) environments. Active Directory serves as the identity
and access management backbone for over 90% of enterprise networks globally,
making it a primary target for cyberattacks. This module covers how Domain
Controllers are structured, how permissions inherit across Users and Groups, and
how misconfigurations in Group Policy Objects (GPOs) can be exploited to achieve
privilege escalation and lateral movement.

---

## Learning Objectives
By the end of this project, you should be able to comprehensively explain the
following concepts without external references:
* **Active Directory:** The centralized directory service for Windows domain networks.
* **Authorization:** The process of verifying what resources an authenticated user can access.
* **Authentication:** The process of verifying the identity of a user or system.
* **Domain Controllers:** Servers that manage security authentication requests and host the AD database.
* **Domains:** A logical grouping of network objects sharing a common directory database and policies.
* **LDAP:** Lightweight Directory Access Protocol, used to query and manage directory objects.

---

## Requirements & Lab Environment

### Operating System Images
* **Windows Server 2019 VM** (Target / Domain Controller)
* **Kali Linux** (Attacker Platform)

### Crucial Constraints
* **Deployment Option:** Students must **only** download and set up the Windows
    Server 2019 VM. The Windows 11 workstation module is omitted based on hardware
    and deployment scope constraints.
* **Network Configuration:** All virtual machines must be connected to the exact
    same virtual network interface (e.g., Host-Only or NAT Network) to ensure proper
    inter-VM communication.
* **Access Control:** No direct credentials will be provided for the Windows Server
    environment. All access, credential harvesting, and enumeration must be executed
    remotely from the Kali Linux attack machine via exploitation.

---

## Technical Specifications & Protocols

The following default infrastructure components are evaluated during the assessment:

| Component | Default Protocol / Port | Purpose inside AD |
| :--- | :--- | :--- |
| **LDAP** | TCP/UDP 389 | Directory querying and object attribute extraction. |
| **LDAP (SSL)** | TCP 636 | Secure directory operations and credential transport. |
| **Kerberos** | TCP/UDP 88 | Ticket-based authentication management. |
| **SMB** | TCP 445 | Policy dissemination (SYSVOL) and remote share enumeration. |
| **WinRM** | TCP 5985 / 5986 | Remote management and initial foothold access. |

---

## Methodology and Project Workflow

### 1. Network
