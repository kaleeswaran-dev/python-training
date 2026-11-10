prices = [500, 1200, 800, 2500, 300]

def apply_discount(price, discount=10):
    return price*discount/100



result = apply_discount(500)

print(result)




# using * args
def total(*prices):
    total = 0
    for price in prices:
        total+= price

        return total



prices = (500, 1200, 800, 2500, 300)
totalresult = total(*prices)
print(totalresult)


belowprices = []

for price in prices:
    if price<1000:
        belowprices.append(price)



print(belowprices)



# map and lambada in python


#prices = [500, 1200, 800, 2500, 300]

# Add 18% GST
gst_prices = list(map(lambda price:round(price*1.18,2),prices))
print("GST Prices:", gst_prices)

# Keep prices below 1000
filtered_price = list(filter(lambda price : price<1000,gst_prices))
print("Below 1000:", filtered_price)