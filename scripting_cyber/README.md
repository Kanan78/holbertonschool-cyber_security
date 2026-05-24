# Scripting for Cybersecurity

## Description

This repository contains a series of Ruby scripts developed for cybersecurity
purposes. The project covers fundamental scripting concepts and applies them
to real-world security scenarios including network scanning, exploitation,
post-exploitation, and defensive analysis.

Ruby is the core language of the Metasploit framework, the most widely used
penetration testing platform in the industry. Mastering Ruby scripting in a
security context enables professionals to build custom tools, automate
assessments, and contribute to the broader security community.

All scripts are written with clarity and practicality in mind, following
the Betty style guide.

---

## Repository Structure

```
scripting_cyber/
├── README.md
├── 0x00-hello_world/
├── 0x01-factorial/
├── 0x02-prime_checker/
├── 0x03-file_io/
├── 0x04-class_inheritance/
├── 0x05-http_requests/
├── 0x06-file_downloading/
├── 0x07-network_ping/
├── 0x08-port_scanner/
├── 0x09-banner_grabbing/
├── 0x0A-vulnerability_scanner/
├── 0x0B-password_cracker/
├── 0x0C-ssh_brute_force/
├── 0x0D-injection_detection/
├── 0x0E-mitm_simulation/
├── 0x0F-packet_sniffing/
├── 0x10-reverse_shell/
├── 0x11-keylogger/
├── 0x12-phishing_automation/
├── 0x13-database_interaction/
├── 0x14-rest_api/
├── 0x15-multithreading/
├── 0x16-sinatra_webapp/
├── 0x17-rspec_testing/
└── 0x18-web_scraping/
```

---

## Requirements

- **OS**: Kali Linux
- **Language**: Ruby
- **Allowed editors**: `vi`, `vim`, `emacs`
- First line of every script must be: `#!/usr/bin/env ruby`
- All files must end with a new line
- All files must be executable
- IP range must be passed as `$1` (without quotes)
- Code must comply with **Betty style**
  (checked via `betty-style.pl` and `betty-doc.pl`)
- The following are **not allowed**: backticks, `&&`, `||`, `;`

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/your_username/scripting_cyber.git
cd scripting_cyber
```

### Make scripts executable

```bash
chmod +x path/to/script.rb
```

### Run a script

```bash
./script.rb $1
```

Replace `$1` with the appropriate argument such as an IP address,
IP range, hostname, or target URL depending on the script.

---

## Modules Overview

### Fundamentals

| Directory | Topic |
|-----------|-------|
| `0x00-hello_world` | Functions, Classes, Ruby basics |
| `0x01-factorial` | Recursive and iterative logic |
| `0x02-prime_checker` | Prime class usage |
| `0x03-file_io` | Reading, writing, copying files |
| `0x04-class_inheritance` | Object-oriented design in Ruby |

### Networking and Scanning

| Directory | Topic |
|-----------|-------|
| `0x05-http_requests` | GET, POST, HTTParty gem |
| `0x06-file_downloading` | Fetching remote resources |
| `0x07-network_ping` | Host availability with Net::Ping |
| `0x08-port_scanner` | Socket-based port scanning |
| `0x09-banner_grabbing` | Service fingerprinting |
| `0x0A-vulnerability_scanner` | Basic vulnerability detection |

### Exploitation and Attacks

| Directory | Topic |
|-----------|-------|
| `0x0B-password_cracker` | Hash-based password cracking |
| `0x0C-ssh_brute_force` | SSH brute force with Net::SSH |
| `0x0D-injection_detection` | SQL injection, XSS, directory traversal |
| `0x0E-mitm_simulation` | Man-in-the-middle attack simulation |
| `0x0F-packet_sniffing` | Packet capture in Ruby |
| `0x10-reverse_shell` | Creating and handling reverse shells |
| `0x11-keylogger` | Input capture simulation |
| `0x12-phishing_automation` | Automated phishing via Net::SMTP |

### Advanced Topics

| Directory | Topic |
|-----------|-------|
| `0x13-database_interaction` | SQLite3 queries in Ruby |
| `0x14-rest_api` | Consuming REST APIs |
| `0x15-multithreading` | Thread class and concurrency |
| `0x16-sinatra_webapp` | Simple web application server |
| `0x17-rspec_testing` | Unit testing with RSpec |
| `0x18-web_scraping` | Advanced scraping with Mechanize |

---

## Learning Objectives

By completing this project, you will be able to:

- Explain the role of Ruby in the Metasploit framework
- Write and customize exploits and payloads in Ruby
- Automate network reconnaissance and vulnerability scanning
- Perform brute force attacks and credential testing
- Detect common web vulnerabilities programmatically
- Simulate attack scenarios including MITM and reverse shells
- Interact with external APIs, databases, and web services
- Apply multithreading for performance in security tools
- Write clean, testable, and maintainable Ruby code

---

## Ethical Disclaimer

> All scripts in this repository are developed strictly for educational
> purposes and authorized penetration testing environments.
> Unauthorized use of these tools against systems you do not own or
> have explicit permission to test is **illegal** and **unethical**.
> Always obtain proper written authorization before conducting any
> security assessment.

---

## Resources

- [Ruby Official Documentation](https://www.ruby-lang.org/en/documentation/)
- [Metasploit Unleashed](https://www.offsec.com/metasploit-unleashed/)
- [OWASP Foundation](https://owasp.org/)
- [Net::SSH](https://github.com/net-ssh/net-ssh)
- [HTTParty Gem](https://github.com/jnunemaker/httparty)
- [SQLite3 Gem](https://github.com/sparklemotion/sqlite3-ruby)
- [Sinatra](http://sinatrarb.com/)
- [RSpec](https://rspec.info/)
- [Mechanize Gem](https://github.com/sparklemotion/mechanize)

---

## Author

**Your Name**
- GitHub: [@your_username](https://github.com/your_username)
