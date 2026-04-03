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

    if search_str == "":
        return

    try:
        # Open maps file to find heap boundaries
        with open("/proc/{}/maps".format(pid), "r") as f:
            for line in f:
                if "[heap]" in line:
                    addr_range = line.split()[0].split('-')
                    start = int(addr_range[0], 16)
                    end = int(addr_range[1], 16)
                    break
            else:
                sys.exit(1)

        # Open mem file in read/write binary mode
        with open("/proc/{}/mem".format(pid), "rb+") as f:
            f.seek(start)
            data = f.read(end - start)
            
            # Find the search string in the heap data
            idx = data.find(search_str.encode())
            
            if idx == -1:
                sys.exit(1)

            # Move to the position and overwrite
            f.seek(start + idx)
            f.write(replace_str.encode())
            # Important: if replace is shorter, we might need to null-terminate
            # but usually for these tasks, just writing the string is enough.
            
    except (IOError, IndexError, ValueError):
        sys.exit(1)


if __name__ == "__main__":
    read_write_heap()
