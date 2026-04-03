#!/usr/bin/python3
"""
Module to find and replace a string in the heap of a running process.
This script takes a PID, a search string, and a replacement string.
"""
import sys


def read_write_heap():
    """
    Finds and replaces a search_string with a replace_string
    in the heap of the process identified by pid.
    """
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search replace")
        sys.exit(1)

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if not search_str:
        sys.exit(1)

    try:
        # Heap aralığını tap
        with open(f"/proc/{pid}/maps", "r") as f:
            heap_start = None
            heap_end = None

            for line in f:
                if "[heap]" in line:
                    addr_range = line.split()[0].split('-')
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    break

            if heap_start is None:
                sys.exit(1)

        # Heap-i oxu və dəyiş
        with open(f"/proc/{pid}/mem", "rb+") as f:
            f.seek(heap_start)
            data = f.read(heap_end - heap_start)

            search_bytes = search_str.encode()
            idx = data.find(search_bytes)

            if idx == -1:
                sys.exit(1)

            replace_bytes = replace_str.encode()

            search_len = len(search_bytes)
            replace_len = len(replace_bytes)

            if replace_len == 0:
                replace_bytes = b'\x00' * search_len
            elif replace_len < search_len:
                diff = search_len - replace_len
                replace_bytes += b'\x00' * diff
            elif replace_len > search_len:
                replace_bytes = replace_bytes[:search_len]

            # Yaz
            f.seek(heap_start + idx)
            f.write(replace_bytes)

    except (IOError, OSError, ValueError):
        sys.exit(1)


if __name__ == "__main__":
    read_write_heap()
