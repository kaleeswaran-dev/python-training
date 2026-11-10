age = 30
name = "kaleeswaran"
salary=52000.99
list = ["java script","java","anugular","python"]
duble = ("python","gen AI","machine learning")
setvale = {10,20,20,30,10}
dictionary = {
    name :"kaleeswaran",
    age :30,
    salary:52000.99
}

print(type(list))

print(type(duble))

print(type(setvale))

print(type(dictionary))



#sales = [12000, 80000,10000,0, 8500, 15000, -200, 9800,]
# total = 0

# for amount in sales:
#     total += amount
#     print("added value " + str(total))
#     if(total == 30000):
#         print("total value " + str(total))

# for sale in sales:
#     # if sale==0 or sale<0:
#     #     print(sale)
#     #     continue

#     total += sale
#     print("added value" + str(total))
#     if total==30000:
#         break
        
    # if total>30000:
    #     break


#print("total value" + str(total))
# if total == 30000:
#     print("target reached")

# elif total<30000:
#     #total+=added
#     print("target not reached")

# elif total==0 or total<0:
#     print("invalid value")


# ratelimit = 30000
# added = 15000


# for in range(30000):


# if total == ratelimit:
#     print("target reached")

# elif total<ratelimit:
#     total+=added
#     print("target not reached")

# elif added==0 or added<0:
#     print("invalid value")


sales = [12000, 80000,10000,0, 8500, 15000, -200, 9800,]

total = 0

for amount in sales:
    total += amount

    if total > 30000:
        break

if total > 30000:
    print("Target reached")
elif total == 30000:
    print("Target reached exactly")
else:
    print("Target not reached")

print("Total:", total)