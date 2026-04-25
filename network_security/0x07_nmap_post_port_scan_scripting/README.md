# Nmap Scripting Engine (NSE) Project

## Description

This project covers the **Nmap Scripting Engine (NSE)** — one of the most powerful features of Nmap. NSE allows users to write and execute scripts to automate a wide variety of networking tasks, including host discovery, vulnerability detection, backdoor detection, and more. Scripts are written in the **Lua** programming language and are organized into categories based on their purpose and risk level.

---

## Learning Objectives

By the end of this project, you should be able to explain — without the help of Google:

- What is the Nmap Scripting Engine (NSE) and why is it important
- How the Nmap Scripting Engine works
- The different script categories in NSE
- How scripts are organized and executed in NSE
- What command-line arguments are used for running NSE scripts
- What you can do with Nmap scripts
- How to write documentation for NSE scripts using NSEDoc

---

## What is NSE?

The **Nmap Scripting Engine (NSE)** is a component of Nmap that allows users to automate networking tasks using scripts written in the **Lua** scripting language. NSE was introduced to extend Nmap's functionality beyond simple port scanning.

### Why is NSE important?

- Automates complex and repetitive network tasks
- Enables vulnerability detection and exploitation testing
- Provides service enumeration and banner grabbing
- Supports brute-force credential testing
- Allows custom script development for specific needs

---

## How NSE Works

1. Nmap scans the target host/network
2. NSE scripts are triggered based on **rules** (e.g., open port, specific service)
3. Scripts interact with the target using the network
4. Results are reported back to the user in the Nmap output

Scripts are located at: `/usr/share/nmap/scripts/`

---

## Script Categories

| Category | Description |
|---|---|
| `auth` | Tests authentication — default credentials, anonymous access |
| `broadcast` | Sends broadcast packets to discover hosts and services |
| `brute` | Performs brute-force attacks on credentials |
| `default` | Runs when `-sC` flag is used; safe and informative scripts |
| `discovery` | Gathers information about target hosts and services |
| `dos` | Tests for denial-of-service vulnerabilities (use with caution) |
| `exploit` | Attempts to exploit known vulnerabilities |
| `external` | Communicates with external services (e.g., Whois, Shodan) |
| `fuzzer` | Sends unexpected or malformed input to detect bugs |
| `intrusive` | Aggressive scripts that may crash or harm the target |
| `malware` | Detects malware and backdoors on target systems |
| `safe` | Scripts that are unlikely to crash or harm the target |
| `version` | Extends Nmap's service version detection |
| `vuln` | Checks for known vulnerabilities (CVEs) |

---

## Command-Line Usage

### Basic Syntax

```bash
# Run default scripts
nmap -sC <target>

# Run a specific script
nmap --script=<script-name> <target>

# Run a category of scripts
nmap --script=<category> <target>

# Run multiple scripts
nmap --script=<script1>,<script2> <target>

# Run all scripts matching a pattern
nmap --script="http-*" <target>

# Pass arguments to a script
nmap --script=<script> --script-args="key=value" <target>
```

### Common Flag Combinations

```bash
# Full scan with service detection, OS detection, and default scripts
nmap -sV -sC -O <target>

# Vulnerability scan
nmap --script=vuln <target>

# Run scripts against a range of IPs using $1
nmap --script=<script> $1
```

---

## Listing and Finding Scripts

```bash
# List all available scripts
ls /usr/share/nmap/scripts/

# Search by keyword
ls /usr/share/nmap/scripts/ | grep http

# View script categories from the database
grep "vuln" /usr/share/nmap/scripts/script.db

# View help for a specific script
nmap --script-help http-enum

# Update the script database
nmap --script-updatedb
```

---

## NSEDoc — Script Documentation

NSEDoc is the documentation standard for NSE scripts. Each script should include:

```lua
description = [[
  A brief description of what the script does.
]]

-- @usage nmap --script=example <target>
-- @output
-- PORT   STATE SERVICE
-- 80/tcp open  http
-- | example:
-- |   result here

categories = {"default", "safe"}
```

### Key NSEDoc Fields

- `description` — What the script does
- `@usage` — Example command to run the script
- `@output` — Example output the script produces
- `@args` — Script arguments (if any)
- `categories` — Which NSE categories the script belongs to

---

## Script Structure (Lua)

```lua
description = [[Short description of the script]]

categories = {"default", "safe"}

local nmap = require "nmap"

-- Rule: when should this script run?
portrule = function(host, port)
    return port.protocol == "tcp" and port.state == "open"
end

-- Action: what should the script do?
action = function(host, port)
    return "Script output here"
end
```

---

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- **OS:** All scripts tested on Kali Linux
- **Script length:** Exactly 2 lines (`wc -l file` must print `2`)
- **First line:** Must be exactly `#!/bin/bash`
- **IP range:** Must use `$1` (without quotes)
- **Prohibited:** backticks, `&&`, `||`, `;`, `echo`, `"` or `'` around `$1`
- **Ports:** Must be referenced by number, not service name
- **Style:** Must follow Betty style guide
- **Executable:** All files must be executable
- **New line:** All files must end with a new line

---

## Resources

- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Nmap Scripting Engine (NSE)](https://nmap.org/book/nse.html)
- [NSEDoc Reference Portal](https://nmap.org/nsedoc/)
- [List of Nmap Scripts](https://nmap.org/nsedoc/scripts/)

---

## Author

This project is part of the Holberton School / ALX curriculum on advanced network scanning techniques using Nmap.
