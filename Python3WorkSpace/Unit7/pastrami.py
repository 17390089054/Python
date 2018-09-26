print("pastrami has been sold out\n")
sandwish_orders=['StrawBerry','pastrami','Banana','pastrami','pastrami','Apple','Pine','watermelon']
while 'pastrami' in sandwish_orders:
    sandwish_orders.remove('pastrami')
print("Here are left sandwish")
for sandwish in sandwish_orders:
    print(sandwish)
