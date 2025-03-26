# Question 1
# calculate discount based on the amount and given discount

def calculate_discount(price, discount_percent):
    discount_amount = (price*discount_percent/100)
   
# my Iphone 15 example
original_price = 15000
discount_percent = 20

discount = calculate_discount(price, discount_percent) #type:ignore
print(f"Discount Amount: ${discount:2f}")

if discount_percent == 20:
    print("Discount Applied")
else:  
    print("Original Price")

# Question 2
#get user input

price = float(input("Enter the original price:"))
discount_percent = float(input("Enter the discount percentage:"))

# calculate the final price
discount amount = calculate_discount(price, discount_percent)
final_price = price - discount_amount

print(f"final price after discount: ${final_price:2f}")

