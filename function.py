def line_total(item):
    return item["price"] * item["qty"]



def sub_total(cart):
    total=[]
    for x in range(len(cart)):
        price=cart[x].get("price")
        qty=cart[x].get("qty")
        total1=price*qty
        total.append(total1)
    sub_total=sum(total)
    return sub_total    

def apply_discount(p,discount=0):
     d_price=p*(1-discount/100)
     return d_price

def gst(g,rate=18):
     g_price=g*rate/100
     return g_price

def category_totals(cart):
    
    totals = {}
    for item in cart:
        cat = item["category"]
        if cat not in totals:
            totals[cat] = 0  
        totals[cat] += item["price"] * item["qty"]
    return totals

def top_items(cart, n=2):
    sorted_items = sorted(cart, key=line_total, reverse=True)
    return [item["name"] for item in sorted_items[:n]]

def print_bill(cart, discount_percent=0):
    print(f"{'Item':<10}{'Price':>6}{'Qty':>5}{'Total':>8}")
    print("-" * 30)
    for item in cart:
        print(f"{item['name']:<10}{item['price']:>6}{item['qty']:>5}{line_total(item):>8}")
    print("-" * 30)
    
    sub = sub_total(cart)
    disc_amount = sub * (discount_percent / 100)
    discounted_sub = sub - disc_amount
    gst_amount = gst(discounted_sub, rate=18)
    grand_total = discounted_sub + gst_amount
    
    print(f"{'Subtotal':<21}{sub:>8.2f}")
    print(f"{f'Discount {discount_percent}%':<21}{disc_amount:>8.2f}")
    print(f"{'GST 18%':<21}{gst_amount:>8.2f}")
    print(f"{'Grand total':<21}{grand_total:>8.2f}")