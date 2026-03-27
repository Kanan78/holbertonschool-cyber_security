# Cyber - WebSec 0x07: File Inclusion (LFI & RFI)

## Description
This project focuses on identifying, exploiting, and mitigating File Inclusion vulnerabilities, specifically **Local File Inclusion (LFI)** and **Remote File Inclusion (RFI)**. These vulnerabilities occur when an application allows a user to submit input that is then used to include a file on the server without proper validation.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* **What is LFI?**: Local File Inclusion is a vulnerability that allows an attacker to include files stored locally on the server.
* **What is RFI?**: Remote File Inclusion is a vulnerability that allows an attacker to include and execute scripts from external/remote sources.
* **How to prevent FI attacks?**: Implementing strict input validation, using whitelists, and disabling dangerous PHP settings like `allow_url_include`.
* **What is `../../` used for in FI?**: This is a Directory Traversal technique used to navigate outside the intended directory to reach sensitive system files (e.g., `/etc/passwd`).
* **How can LFI lead to RCE?**: Through techniques like Log Poisoning or using PHP Wrappers to execute system commands.
* **Mechanisms of Exploitation**: Manipulating URL parameters, using wrappers, or poisoning log files.
* **Potential Impact**: Data leakage, unauthorized access to sensitive files, and full system takeover via Remote Code Execution.
* **Detection Techniques**: Fuzzing parameters, observing error messages, and analyzing server-side file handling logic.
* **Mitigation Strategies**: Using a whitelist of allowed files, sanitizing inputs, and properly configuring server settings.

## Resources
### Read or watch
* [Local File Inclusion (LFI) – OWASP](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)
* [Remote File Inclusion (RFI) – OWASP](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion)
* [LFI to RCE: Basic Exploitation Guide](https://www.hackingarticles.in/lfi-to-rce-basic-exploitation-guide/)
* [File Inclusion Types, Examples, and Prevention](https://www.acunetix.com/blog/articles/file-inclusion-vulnerabilities/)
* [File Inclusion Path Traversal](https://portswigger.net/web-security/file-path-traversal)

### References
* [PHP Manual on include() and require()](https://www.php.net/manual/en/function.include.php)
* [File Inclusion Cheat Sheet](https://highon.coffee/blog/lfi-cheat-sheet/)
* [File Inclusion Payload Github](https://github.com/payloadbox/rfi-lfi-payload-list)

## Requirements
* **Allowed editors**: `vi`, `vim`, `emacs`.
* **Testing Environment**: All scripts will be tested on **Kali Linux**.
* **Script Length**: All scripts should be exactly one line long.
* **New Line**: All files must end with a new line.
* **Mandatory File**: A `README.md` file at the root of the project folder is required.
* **Target Domain**: `Cyber - WebSec 0x07`.

## Project Structure
| File | Task Description |
| --- | --- |
| `README.md` | Mandatory project documentation. |
| (Task Files) | Specific one-line exploitation/analysis scripts. |
