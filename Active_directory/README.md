# Active Directory (AD) Fundamentals

## Description
Active Directory (AD) is a directory service developed by Microsoft for Windows
domain networks. It is included in most Windows Server operating systems as a
set of processes and services. Initially, Active Directory was only used for
centralized domain management. However, it now serves as an umbrella title for
a wide range of directory-based identity-related services.

---

## Core Components

### 1. Logical Structure
The logical structure of AD organizes the network resources into a hierarchical
and manageable form, independent of the physical topology.

* **Objects:** The most basic element in AD. Represents network resources
    such as users, computers, printers, and groups.
* **Organizational Units (OUs):** Containers used to organize objects within
    a domain. Useful for delegating administrative authority and applying Group
    Policy Objects (GPOs).
* **Domains:** A logical grouping of network objects that share a common
    directory database, security policies, and trust relationships.
* **Trees:** A collection of one or more domains that share a contiguous
    namespace (e.g., `parent.local` and `child.parent.local`).
* **Forests:** The uppermost container in the AD logical hierarchy. A forest
    is a collection of one or more domain trees that share a common schema,
    configuration, and global catalog.

### 2. Physical Structure
The physical structure governs how replication occurs and how users log into
the network based on geographical locations.

* **Domain Controllers (DCs):** Servers running the Active Directory Domain
    Services (AD DS) role. DCs hold a copy of the directory database, replicate
    changes, and handle authentication requests.
* **AD Sites:** One or more well-connected (high bandwidth) IP subnets representing
    a physical location. Sites optimize replication traffic and authentication.

---

## Essential Protocols

Active Directory relies heavily on standard network protocols to function properly:

| Protocol | Default Port | Description |
| :--- | :--- | :--- |
| **LDAP** | 389 / 636 (SSL) | Lightweight Directory Access Protocol. Used to query and modify objects inside the AD database. |
| **Kerberos** | 88 | The primary authentication protocol in AD. Uses tickets to verify identities without sending passwords over the wire. |
| **SMB** | 445 | Server Message Block. Used for file sharing, policy dissemination (SYSVOL), and remote administration. |
| **DNS** | 53 | Domain Name System. Vital for locating Domain Controllers and translating human-readable names to IP addresses. |

---

## Naming Conventions (LDAP Syntax)

LDAP objects are addressed using specific naming attributes to define their
exact location within the directory information tree (DIT).

* **CN (Common Name):** Refers to the specific object itself (e.g., `CN=Administrator`).
* **OU (Organizational Unit):** Refers to the container holding the object (e.g., `OU=Admins`).
* **DC (Domain Component):** Refers to the parts of the domain name (e.g., `lab.local` becomes `DC=lab,DC=local`).

> ### Distinguished Name (DN) Example:
> `CN=Kanan,OU=Users,DC=lab,DC=local`
>
> This string represents the absolute path to the user object "Kanan" within the "Users" OU of the "lab.local" domain.

---

## Security & Enumeration Concepts

Understanding AD architecture is essential for both system administrators
and penetration testers:

### 1. Domain Enumeration
The process of gathering information about the internal network, mapping users,
groups, domain controllers, and trust relationships. Attackers utilize standard
queries (such as LDAP searches) to understand the landscape.

### 2. Operational Attributes
Active Directory objects contain certain attributes that are not returned during
standard directory queries. These are called **operational** or **constructed**
attributes. They are calculated dynamically by the server and require explicit
property requests (e.g., utilizing specific filters or wildcards like `+` in
`ldapsearch`) to become visible.

### 3. GPO (Group Policy Objects)
A collection of settings that define what a system looks like and how it acts
for a defined group of users or computers. GPOs are often targeted by auditors
and attackers to find misconfigurations.
