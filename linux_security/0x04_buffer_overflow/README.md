# 0x04. Buffer overflow

## Description
This project explores the concepts of memory management, focusing on buffer overflows, their causes, consequences, and mitigation strategies. It also includes a practical implementation of a Python script to manipulate the heap memory of a running process.

## Learning Objectives
By the end of this project, I am able to explain:
* **What is a buffer?** A temporary storage area in memory (RAM) used to hold data while it is being moved.
* **What is Buffer Overflow?** A condition where a program writes more data to a buffer than it can hold, causing it to overflow into adjacent memory.
* **What is a Buffer Overflow Attack?** An exploitation method where an attacker intentionally causes a buffer overflow to overwrite memory and execute malicious code.
* **What causes buffer overflow attacks?** Lack of bounds checking on user input and the use of unsafe functions (e.g., `strcpy`, `gets`, `scanf` in C).
* **How do Attackers Orchestrate Buffer Overflow Attacks?** By identifying a vulnerability, analyzing memory layout, overwriting the return address (Stack) or function pointers (Heap), and redirecting execution to a shellcode.
* **What are the different types of buffer overflow attacks?** Primarily Stack-based and Heap-based overflows.
* **How to detect buffer overflow?** Through static code analysis, dynamic analysis (fuzzing), and memory monitoring tools.
* **What are the consequences of Buffer Overflow?** System crashes, data corruption, unauthorized access, and Remote Code Execution (RCE).
* **How to Prevent and Mitigate Buffer Overflow Attacks?** Using safe functions, implementing ASLR, Stack Canaries, DEP/NX, and using memory-safe programming languages.

## Requirements
* **Operating System:** Ubuntu 14.04 LTS
* **Language:** Python 3.4.3
* **Style Guide:** PEP 8
* **Editors:** vi, vim, emacs

## Tasks

### 0. Read & write heap
A Python script `read_write_heap.py` that finds a specific string in the heap of a running process and replaces it.

* **Usage:** `sudo ./read_write_heap.py pid search_string replace_string`
* **Features:**
    * Accesses `/proc/[pid]/maps` to locate the `[heap]` memory segment.
    * Reads the raw memory from `/proc/[pid]/mem`.
    * Locates the first occurrence of the search string.
    * Overwrites it with the replacement string directly in the process memory.
    * Handles errors such as missing PID, permission issues, or string not found.

## Files
| File | Description |
| --- | --- |
| `read_write_heap.py` | Python script to modify heap memory of a process. |
| `main.c` | C program used for testing memory modification. |
