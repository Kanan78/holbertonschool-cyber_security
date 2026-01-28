# Content Discovery - WebSec 0x04

This project focuses on identifying hidden resources and mapping the attack surface of web applications. The primary target for this project is **Cyber - WebSec 0x04**.

## 📖 Resources

### Read or watch:
* **Content discovery**
* **Content Discovery for Web Application Security**
* **Content Discovery: Understanding Your Web Attack Surface**
* **What are the content discovery**
* **OWASP Testing Guide: Content Discovery**
* **Exploiting: Content Discovery**

### References:
* `dirb`, `nikto`, `sfuzz`, `wfuzz`
* `gobuster`, `dirbuster`, `feroxbuster`

---

## 🎯 Learning Objectives

By the end of this project, you are expected to be able to explain the following without the help of Google:

* **What is content discovery?** The process of finding hidden or unlinked resources on a web server.
* **Why is content discovery important?** To identify sensitive files (backups, configs) and hidden entry points.
* **How does directory bruteforcing work?** Systematically testing common directory names using a wordlist.
* **What is Gobuster and how is it used?** A tool used for discovering URIs and DNS subdomains.
* **Burp Suite in content discovery:** Using tools like Spider or Intruder to map applications.
* **OWASP ZAP assist:** Using the forced browse and spidering features for discovery.
* **Wordlists:** Their role as the dictionary for brute-forcing tools.
* **DirBuster purpose:** A multi-threaded application for brute-forcing directories and file names.
* **Hidden directories and files:** Understanding `.env`, `.git`, `backup/`, and other sensitive paths.
* **Fuzzing in web security:** Providing unexpected data to inputs to discover vulnerabilities or paths.

---

## 💻 Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`.
* **OS:** All scripts will be tested on **Kali Linux**.
* **Script Format:** All scripts must be exactly **one line long**.
* **File Endings:** All files must end with a new line.
* **Mandatory File:** A `README.md` file at the root of the project folder.
* **Target:** Focus on **Cyber - WebSec 0x04**.

---

## 🛠️ Tasks

| File Name | Description |
| :--- | :--- |
| `0-gobuster.sh` | One-line command for directory discovery using Gobuster. |
| `1-feroxbuster.sh` | One-line command for recursive discovery using Feroxbuster. |
| `2-wfuzz.sh` | One-line command for parameter or directory fuzzing. |
