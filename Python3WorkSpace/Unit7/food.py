sandwish_orders=['StrawBerry','Banana','Apple','Pine','watermelon']
finished_sandwishes=[]
while sandwish_orders:
    sandwish=sandwish_orders.pop()
    finished_sandwishes.append(sandwish)
for sandwish in finished_sandwishes:
    print("Finish "+sandwish+"sandwish!")
    
