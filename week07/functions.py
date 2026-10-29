#1- In exercise 5 the first bug I found was when the for loop didn't have a colon at the end. I think that my debugging skills are fairly good, but I do feel like I need more practice for less obvious bugs. 
#2- The line apply_discount(price, tier) will call the product a value when apply_discount is called. This value will return the parameters price and tier. A colleuge could use this without looking at the body because they could assume that price is the numerical value and that the tier could be a level, like silver or gold. 
#3- Debugging: The Syntax Error reported showed that line 10 was missing a colon after the for loop., The Index Error here showed that i was out of bounds from the sales, it was too large so I had to adjust the condition to make it fit in bounds.

# Exercise 1: calculate_tax

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2: apply_discount

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3: Compose them

# Write it out manually first

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${after_tax:.2f}")
print(f"After Tax: ${after_tax:.2f}")

#Refactor into function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4: Additional functionality

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5:

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}") # This will print the last sale value instead of the sum

count = 0
for sale in sales:     # The Syntax Error reported showed that line 10 was missing a colon after the for loop.
    count += 1
print(f"Count: {count}") 

i = 0
while i < len(sales):  # The Index Error here showed that i was out of bounds from the sales, it was too large so I had to adjust the condition to make it fit in bounds.
    print(i, len(sales))
    print(sales[i])
    i += 1

# Exercise 6:

x = 100 # apple, Global

def double_it():
    x = 999 # another different apple, local
    return x * 2

print(x)
print(double_it())
print(x)
