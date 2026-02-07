#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split(",")
    if len(parts) != 3:
        continue

    product_name = parts[1]
    amount = parts[2]

    print(f"{product_name}\t{amount}")
