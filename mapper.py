#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) > 0:
        status = parts[-1]
        if status.startswith('4') or status.startswith('5'):
            print(f"{status}\t1")
