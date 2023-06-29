#Lists of food and their prices'that the user will input into these empty lists
Food=[]
Total=[]

def format():
  for i in Food:
    if len(i)==8:
      print (i,'{:>12.2f}'.format(Total.pop(0)))
    elif len(i)==7:
      print (i,'{:>13.2f}'.format(Total.pop(0)))
    elif len(i)==6:
      print (i,'{:>14.2f}'.format(Total.pop(0)))
    elif len(i)==4:
      print (i,'{:>16.2f}'.format(Total.pop(0)))
    elif len(i)==3:
      print (i,'{:>17.2f}'.format(Total.pop(0)))
    #Takes into account longer and shorter word lengths of orders for proper formatting
    else:
      print (i,'{:>15.2f}'.format(Total.pop(0)))
    #Standard word length of a order is set to 5


print("Welcome to Michael's Diner!")

order=input("What would you like to order? (press q to stop ordering) ")

price_total=0 #A value that keeps track of the total cost of food being ordered

item=0
while item==0:
  if order.upper()=="Q":
    tip=int(input("How much would you like to tip? (enter a percent) "))
    item=item+1 #ends the users order

  else:
    Food.append(order)
    price=float(input("How much does it cost (in dollars and cents?) "))
    Total.append(price)

    price=price+price_total
    price_total=price #price_total is intially 0, so the price is added based on how much the food item costs, also calculates the Sub-total
    
    order=input("What else would you like to order? (press q to stop ordering) ") #Keeps asking if the user wants to add more food to their order as well as the price

tax=0.05
tip=tip*.01
#Set values for tax and tip

Tax=price*tax
Tip=price*tip
#Calculates the tax and tip

price=price+price*tax
price=price+price*tip
#Calculates the total bill

print ("Heres your receipt")
print ("Item            Price")
print("---------------------")

format()

print("---------------------")

print ("Sub-total", '{:>11.2f}'.format(price_total))
print ("Tax", '{:>17.2f}'.format(Tax))
print ("Tip", '{:>17.2f}'.format(Tip))
print("---------------------")

print("Total", '{:>15.2f}'.format(price))
