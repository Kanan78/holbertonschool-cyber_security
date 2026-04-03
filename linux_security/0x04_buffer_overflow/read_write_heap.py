#!/usr/bin/python3
"""
Finds and replaces a string in the heap of a running process.
Usage: read_write_heap.py pid search_string replace_string
"""
import sys

if len(sys.argv) != 4:
    sys.exit(1)

pid, search, replace = sys.argv[1:]

try:
    with open("/proc/{}/maps".format(pid), "r") as f:
        heap_line = [line for line in f if "[heap]" in line][0]
        addr_range = heap_line.split()[0].split('-')
        start, end = int(addr_range[0], 16), int(addr_range[1], 16)

    with open("/proc/{}/mem".format(pid), "rb+") as f:
        f.seek(start)
        data = f.read(end - start)
        idx = data.find(search.encode())

        if idx != -1:
            f.seek(start + idx)
            f.write(replace.encode())
except Exception:
    sys.exit(1)
