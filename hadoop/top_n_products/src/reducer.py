#!/usr/bin/env python3
import sys

current_product = None
current_total = 0
sales = {}

for line in sys.stdin:
    line = line.strip()
    product, amount = line.split("\t")
    amount = int(amount)

    sales[product] = sales.get(product, 0) + amount

# Top N
N = 3
top_products = sorted(sales.items(), key=lambda x: x[1], reverse=True)[:N]

for product, total in top_products:
    print(f"{product}\t{total}")
