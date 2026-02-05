# Linux - Permissions and User Management

## Description
This project focuses on understanding and managing file permissions, ownership, and user groups within a Linux environment, specifically tested on Kali Linux. It covers the fundamental concepts of access control, special permissions like SUID and SGID, and the utility of umask in file creation.

## Learning Objectives
By the end of this project, the following concepts are expected to be explained without external help:
* **User Groups:** Understanding the three user-based permission groups (Owner, Group, Others).
* **Command Mastery:** Proper usage of chmod, sudo, su, chown, and chgrp.
* **Special Permissions:** Purpose and implementation of setuid (SUID) and setgid (SGID).
* **Ownership Difference:** Understanding the distinct roles of chown versus chgrp.
* **Permission Masking:** Defining default permissions for new files and directories using Umask.
* **Audit and Best Practices:** Managing and auditing file permissions changes on a Linux system.

## Requirements
* **Allowed Editors:** vi, vim, emacs.
* **Testing Environment:** All scripts are tested on Kali Linux.
* **Script Standards:**
    * The first line of all files is exactly #!/bin/bash.
    * All files end with a new line.
    * All files are executable.
* **Constraints:**
    * No usage of backticks, && or ||.
    * Code must adhere to the Betty style (checked via betty-style.pl and betty-doc.pl).

## Core Concepts Summary

### Permission Groups
* **User:** The individual owner of the file.
* **Group:** A set of users with shared access to the file.
* **Others:** All other users on the system.

### Key Commands
* `chmod`: Changes file mode bits.
* `sudo` / `su`: Executes commands with elevated privileges or switches users.
* `chown`: Changes file owner and group.
* `chgrp`: Changes group ownership.
* `umask`: Sets default creation permissions by masking bits.

### Special Permissions
* **SUID:** Process runs with the file owner's privileges.
* **SGID:** Files inherit the group ID of the directory or processes run with group privileges.
