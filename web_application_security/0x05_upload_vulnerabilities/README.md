# Cyber - WebSec 0x05: File Upload Vulnerabilities

## Description
This project focuses on identifying and exploiting file upload vulnerabilities within a controlled environment. The target of this project is **Cyber - WebSec 0x05**. The objective is to understand how unrestricted file uploads can lead to system compromise and how to implement robust security measures to prevent such attacks.

## Learning Objectives
By the end of this project, the following concepts will be covered:
* Understanding unrestricted file uploads and their security risks.
* Exploitation techniques using web shells.
* The role of MIME types and content-type spoofing in file uploads.
* Bypassing client-side checks and server-side validation techniques.
* Security best practices: File extension filtering, size limitations, and secure directory permissions.
* Risks of storing uploaded files on the same domain and executable directories.

## Requirements
* **Operating System:** All scripts are tested on Kali Linux.
* **Editors:** `vi`, `vim`, or `emacs`.
* **Script Format:** All scripts must be exactly one line long.
* **File Standards:** All files must end with a new line.

## Project Structure
| Task | Description |
| --- | --- |
| Subdomain Enumeration | Identifying the target web application host. |
| Vulnerability Analysis | Inspecting upload features and processing logic. |
| Exploitation | Attempting bypasses and benign file uploads for verification. |

## Resources
* OWASP File Upload Protection Cheat Sheet
* Testing for Upload Vulnerability (WSTG)
* MIME Types and File Extensions Documentation
