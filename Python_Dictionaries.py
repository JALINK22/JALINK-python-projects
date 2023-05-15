
                                ## PART 1

PetsName = {
    "Type": "Dog",
    "color": "White",
    "NickName": "Max",
    "OwnersName": "Jack",
    "type": "Dog",
    "Color": "Red",
    "Nickname": "Odester",
    "Ownersname": "Jack"
    
}

print("Type : ", PetsName.get('Type'))
print("Color : ", PetsName.get('color'))
print("Nickname : ", PetsName.get('NickName'))
print("Owner : ", PetsName.get('OwnersName'))
print("Type : ", PetsName.get('type'))
print("Color : ", PetsName.get('Color'))
print("Nickname : ", PetsName.get('Nickname'))
print("Owner : ", PetsName.get('Ownersname'))



                                ## PART 2 

print("\n")

england = {
    
'Capital': 'London', 
'Population': 'The population of England is 53.01 million',
'InterestingFact': 'Queen Elizabeths Funeral is held tommrow at 5:30am EST', 
'Top2Languages': 'English' 'French' 

},



france = {
    
'Capital': 'Paris',
'Population': 'The population of France is 66.9 million',
'InterestingFact': 'French people usually don’t like Paris',
'Top2Languages': 'French' 'Enlgish'  
    
},



belgium = {
    
'Capital': 'Brussels',
'Population': 'The population of Belgium is 11.35 million',
'InterestingFact': 'The metric system is the legal standard of weights and measures in Belgium',
'Top2Languages': 'Dutch' ' ' "&" ' ' 'French'

},


print(england, sep=None)

print("\n")

print(france, sep=None)

print("\n")

print(belgium, sep=None)


print("\n")

                                ## PART 3

pizza_order = {

   'CustomersName': 'Jack',
   'Size': 'Large,',
   'Crust': 'Thin-crust',
   'Toppings': 'Pepperoni' ',' ' ' 'sausage' ',' ' ' 'bacon.'
 }

print("Thank you for your order,", pizza_order.get('CustomersName'))
print("You have ordered a", pizza_order.get('Size'),  pizza_order['Crust'], "pizza with the following topings:")
print(pizza_order['Toppings'])
