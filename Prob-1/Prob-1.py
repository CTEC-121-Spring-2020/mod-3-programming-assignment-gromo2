# Module 3
#   Programming Assignment 4
#     Prob-1.py

# <Garrett>

def shippingCost(orderSubTotal):
    if orderSubTotal >= 10.00:
        shippingCost = 0
    else:
        shippingCost = 2.99


    return shippingCost

def unitTest():
    orderSubTotal = int(input("Enter Subtotal: "))
    if orderSubTotal < 10.00:
        print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    else:
        print("Shipping cost if subtotal >= 10.00\t", shippingCost(11))


if __name__ == "__main__":
    unitTest()