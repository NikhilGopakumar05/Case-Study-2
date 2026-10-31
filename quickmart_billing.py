# quickmart_billing.py - QuickMart Billing System
import function as f
cart = [
{"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
{"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
{"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
{"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
{"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]

price=cart[0].get("price")
qty=cart[0].get("qty")
to_price=f.line_total(cart[0])
print(f"Task1: Line Total\n{to_price:<6}")

s_total=f.sub_total(cart)
print(f"Task2: Sub Total\n{s_total:<6}")

print(f"Task3: Discount\n{f.apply_discount(500):<6}\n{f.apply_discount(500,10):<4}")

print(f"Task4: GST\n{f.gst(100):<6}\n{f.gst(100,5):<4}")

totals=f.category_totals(cart)
print(f"Task5: Category totals")
for category in sorted(totals.keys()):
    print(f"{category:<12} {totals[category]}")

print("Task 6: Top items")
t_item1=f.top_items(cart)
t_item2=f.top_items(cart, 3)
print(f"{t_item1}\n{t_item2}")

print("Task 7: Bill")
print(f.print_bill(cart, 10))

