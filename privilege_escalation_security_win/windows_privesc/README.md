# Windows Privilege Escalation Project

This project focuses on the mechanics of Windows Privilege Escalation, exploring how misconfigurations, insecure defaults, and weak permissions can be exploited to escalate privileges from a standard user to `NT AUTHORITY\SYSTEM` or `Administrator`. It covers foundational theoretical concepts and provides documentation for identifying and mitigating these security flaws.

---

## Learning Objectives & Core Concepts

### 1. What is Windows Privilege Escalation?
Privilege escalation is the process of exploiting a bug, design flaw, or configuration error in an operating system or software application to gain elevated access to resources that are normally protected from an application or user. In cybersecurity, it is a critical phase because initial access is often gained via low-privileged accounts (e.g., phishing, service exploits). Escalating privileges allows an attacker or penetration tester to perform administrative actions, access sensitive data, alter system settings, and establish persistence.

### 2. Token Manipulation & SeImpersonatePrivilege
Windows uses access tokens to determine the security context of a process or thread. 
*   **SeImpersonatePrivilege** allows a process to impersonate a client after authentication. 
*   If a low-privileged service or account (like `NT AUTHORITY\LOCAL SERVICE` or `IIS_IUSRS`) possesses this privilege, an attacker can trick a higher-privileged service (like `SYSTEM`) into authenticating against an attacker-controlled tool (e.g., via named pipes or RPC). 
*   Tools like **JuicyPotato** or **PrintSpoofer** exploit this by forcing a system service to connect to them, capturing the `SYSTEM` token, and spawning a new process using that token.

### 3. DLL Hijacking
When a Windows application loads a Dynamic Link Library (DLL) without specifying an absolute path, the operating system searches for the DLL in a specific sequence (DLL Search Order):
1. The directory from which the application loaded.
2. The system directory (`C:\Windows\System32`).
3. The 16-bit system directory.
4. The Windows directory (`C:\Windows`).
5. The current directory.
6. The directories listed in the PATH environment variable.

If an attacker has write permissions to any directory in the search order before the legitimate DLL is found, they can place a malicious DLL with the same name in that directory. When the application executes (especially if it runs with elevated privileges), it executes the malicious code.

### 4. Unquoted Service Paths
An unquoted service path vulnerability occurs when a service path contains spaces and is not enclosed in quotation marks. For example:
`C:\Program Files\Development Tools\Service Folder\service.exe`

When Windows attempts to start this service, it interprets the spaces as terminators and looks for executables in the following order:
1. `C:\Program.exe`
2. `C:\Program Files\Development.exe`
3. `C:\Program Files\Development Tools\Service.exe`
4. `C:\Program Files\Development Tools\Service Folder\service.exe`

If a low-privileged user has write permissions to `C:\Program Files\Development Tools\`, they can place a malicious executable named `Service.exe` there, which will run with the privileges of the service (often `SYSTEM`) upon restart.

### 5. Misconfigured Service Permissions
Windows services run under specific security contexts and have security descriptors (Access Control Lists - ACLs). If a service's ACL allows low-privileged users modification rights (such as `SERVICE_CHANGE_CONFIG` or `SERVICE_ALL_ACCESS`), an attacker can use tools like `sc.exe` or PowerShell to modify the service configuration binary path (`binpath`). By pointing the binary path to a malicious executable and restarting the service, the malicious code runs under the service's elevated context.

### 6. Vulnerabilities in Scheduled Tasks and At Jobs
Scheduled Tasks often run with elevated privileges (e.g., `SYSTEM` or an Administrator account). Vulnerabilities arise if:
*   The executable or script executed by the task has weak file permissions, allowing a low-privileged user to modify or replace it.
*   The task runs a script from a directory where a low-privileged user has write access.
*   The task definition XML file itself can be modified due to weak registry or file permissions.

### 7. Weak Registry Permissions
The Windows Registry stores configuration data for services, applications, and the operating system. If registry keys associated with services (located under `HKLM\SYSTEM\CurrentControlSet\Services\`) have weak permissions allowing standard users to modify values, an attacker can alter the `ImagePath` parameter of a service. When the service restarts, it will execute the attacker's payload instead of the original binary.

### 8. Insecure File Permissions
Insecure file permissions occur when critical system binaries, configuration files, or startup folders grant write or modify permissions to groups like `Everyone`, `Authenticated Users`, or `Users`. Attackers can overwrite legitimate binaries or place malicious shortcuts in the Startup folder (`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`), executing payloads automatically when an administrator logs in.

### 9. Bypassing UAC (User Account Control)
UAC is a security feature that prevents unauthorized changes to the operating system. Standard users run in a low-privilege context, while administrators run in a split-token context until elevation is requested. Attackers bypass UAC by exploiting trusted applications that possess the `autoElevate` property in their manifest. Since these applications elevate automatically without prompting the user, an attacker can use techniques like registry hijacking (e.g., `fodhelper.exe` or `computerdefaults.exe` looking for keys under `HKCU\Software\Classes\`) to force the trusted application to load a malicious command in an elevated context.

### 10. Abuse of Background Intelligent Transfer Service (BITS)
BITS is a Windows component used to transfer files asynchronously between a client and a server. Attackers can abuse BITS by creating BITS transfer jobs that execute a specific command or payload upon completion or error (using the Notification Command line property). Since BITS jobs run under a system-level context, this can be leveraged for both privilege escalation and persistence.

---

## Key Tools Used in Windows Privilege Escalation

*   **JuicyPotato / PrintSpoofer:** Local privilege escalation tools that leverage `SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege` via NT authority authentication interception.
*   **Mimikatz:** A credential dumping utility capable of extracting plaintext passwords, hashes, PINs, and Kerberos tickets from memory (`lsass.exe`), used to escalate privileges horizontally or vertically once an initial admin foothold is found.
*   **WinPEAS / PowerUp:** Automated enumeration scripts used to detect misconfigurations, unquoted service paths, weak file permissions, and unattended installation files on a target host.

---

## Exploitation Methodology Case: Unattended Installation Files

During a Windows automated deployment process, configuration files such as `Unattend.xml`, `autounattend.xml`, or `sysprep.inf` are utilized to configure system settings automatically. If administrative credentials are left inside these files post-deployment, any user with read access can extract them.

### Common Unattended File Locations:
*   `C:\Windows\Panther\Unattend.xml`
*   `C:\Windows\Panther\Unattend\Unattend.xml`
*   `C:\Windows\System32\Sysprep\unattend.xml`
*   `C:\Windows\System32\Sysprep\sysprep.inf`

### Credentials Format:
Passwords in these XML files may be stored in plaintext or encoded using Base64 inside the `<AdministratorPassword>` block:
```xml
<AdministratorPassword>
    <Value>U3Ryb25nUGFzc3dvcmQxMjM=</Value>
    <PlainText>false</PlainText>
</AdministratorPassword>
