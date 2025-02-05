bp = float(input("Enter the orignal price"))
sp = float(input("Enter the selling price"))
if sp > bp:
    print ("you got a profit")
    print ("And the profit you got is of ",sp-bp)
else:
    print ("you got a loss")
    print ("And the loss you got is of ",bp-sp)
