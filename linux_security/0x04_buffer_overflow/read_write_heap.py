#!/usr/bin/python3
"""
This module provides a script to find and replace a string in the heap
of a running process. It accesses /proc/[pid]/maps and /proc/[pid]/mem.
"""
import sys


def read_write_heap():
    """
    Finds and replaces a string in the heap of a running process.
    Usage: read_write_heap.py pid search_string replace_string
    """
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search replace")
        sys.exit(1)

    pid, search, replace = sys.argv[1:]

    try:
        # Open maps file to find the heap range
        with open("/proc/{}/maps".format(pid), "r") as f:
            heap_line = [line for line in f if "[heap]" in line][0]
            addr_range = heap_line.split()[0].split('-')
            start = int(addr_range[0], 16)
            end = int(addr_range[1], 16)

        # Open mem file to perform the search and replace
        with open("/proc/{}/mem".format(pid), "rb+") as f:
            f.seek(start)
            data = f.read(end - start)
            idx = data.find(search.encode())

            if idx != -1:
                f.seek(start + idx)
                f.write(replace.encode())
            else:
                sys.exit(1)

    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    read_write_heap()
