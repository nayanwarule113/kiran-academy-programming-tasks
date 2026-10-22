
# Calculate electronics bill with 18% GST
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst

# Calculate fashion bill with 13% GST
def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst

# Calculate food bill with 7% GST
def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

# Calculate total bill after GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food

# Calculate discounted bill
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    payable = total - discount

    print(f"Total after GST = {total:.2f}")
    print(f"Discount = {discount:.2f}")
    print(f"Final payable amount = {payable:.2f}")

    return payable

# Sample values
calculateDiscountedBill(100, 100, 100, 100, 100)
