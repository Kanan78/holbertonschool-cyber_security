#!/usr/bin/python3
"""
Module to find and replace a string in the heap of a running process.
This script takes a PID, a search string, and a replacement string.
"""
import sys


def read_write_heap():
    """
    Finds and replaces a search_string with a replace_string in the
    heap of the process identified by pid.
    """
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search replace")
        sys.exit(1)

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if not search_str:
        return

    try:
        # Open maps file to find the heap range
        with open("/proc/{}/maps".format(pid), "r") as f:
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

        # Open mem file to perform the search and replace
        with open("/proc/{}/mem".format(pid), "rb+") as f:
            f.seek(heap_start)
            data = f.read(heap_end - heap_start)
            
            # Use bytes for search
            idx = data.find(search_str.encode())
            
            if idx == -1:
                sys.exit(1)

            # Move to the specific offset and overwrite
            f.seek(heap_start + idx)
            # Writing an empty string ("") is valid and will overwrite 0 bytes
            f.write(replace_str.encode())
            
    except (IOError, OSError, ValueError):
        sys.exit(1)


if __name__ == "__main__":
    read_write_heap()
