# Reflection 1: Coming in, I was not very familiar with lists and thought that they were just used to state things in a specific order. I am suprised that lists are mutable and cannot be changed once sent. 
# Reflection 2: At my old job working at Dairy Queen we often lost track of what items were sold out and it left customers and staff confused as to what we did and didn't have. A list would make this so much easier to track because I could just remove or append each item. This is a lot quicker than manually putting sold out stickers on items or sending out a large email to the staff. 

# Exercise 1: build the list

inventory = ['pen', 'notebook', 'stapler', 'tape', 'marker']
print(inventory)
print(len(inventory))

# Exercise 2: index practice

print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3: slicing

print(inventory[0:3])
print(inventory[3:5])
print(inventory[::2])

# Exercise 4: modify

inventory.append('envelope')
inventory.remove('tape')
inventory.sort()
print(inventory)

# Exercise 5: tuple comparison

coords = (40.7128, -74.0060)
# coords[0] = 99 # Tuples are good for coordinates because they are immutable and they keep the values together.
print(coords)

# Exercise 6: average of a list of sales

sales = [100, 250, 75, 480, 200]

Total = sum(sales)
Count = len(sales)
Average = Total / Count
Best_day = max(sales)
Worst_day = min(sales)

print("Total sales:", Total)
print("Number of sales:", Count)
print("Average sales:", Average)
print("Best day sales:", Best_day)
print("Worst day sales:", Worst_day)

# Exercise 7: accumulator pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted_prices = []

for price in prices:
    discounted_price = price * 0.9  # Apply a 10% discount
    discounted_prices.append(discounted_price)

print("Original prices:", prices)
print("Discounted prices:", [round(price, 2) for price in discounted_prices])

# Exercise 8: filter above threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

average = sum(high_sales) / len(high_sales)

print("Sales above 300:", high_sales)
print("Count:", len(high_sales))
print("Average of sales above 300:", [round(average, 2)])