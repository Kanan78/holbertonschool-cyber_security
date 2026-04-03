#!/usr/bin/python3
"""
Finds and replaces a string in the heap of a running process.
Usage: read_write_heap.py pid search_string replace_string
"""
import sys

if len(sys.argv) != 4:
    print("Usage: read_write_heap.py pid search replace")
    sys.exit(1)

pid, search, replace = sys.argv[1:]

try:
    # Locate heap boundaries in /proc/[pid]/maps
    with open(f"/proc/{pid}/maps", "r") as f:
        heap_line = [line for line in f if "[heap]" in line][0]
        start, end = [int(x, 16) for x in heap_line.split()[0].split('-')]
    
    print(f"[*] Found heap: {hex(start)} - {hex(end)}")

    # Open /proc/[pid]/mem and perform the replacement
    with open(f"/proc/{pid}/mem", "rb+") as f:
        f.seek(start)
        data = f.read(end - start)
        idx = data.find(search.encode())

        if idx == -1:
            print(f"[-] String '{search}' not found in heap.")
            sys.exit(1)

        print(f"[+] Found '{search}' at {hex(start + idx)}")
        f.seek(start + idx)
        f.write(replace.encode())
        print(f"[+] Successfully replaced with '{replace}'")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
