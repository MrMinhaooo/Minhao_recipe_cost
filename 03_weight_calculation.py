# 03_weight_calculation
g = 1
kg = 1000*g

ingredients_list = ['Chickpeas', 'Onion', 'Parsely', 'Cumin', 'Ground Coriander', 'Salt', 'Chickpea flour']

for ingredients in ingredients_list:

  weight = input("What is the weight of the {} (answer with grams or kilograms)?".format(ingredients))

  price = input("What is the price for {}?".format(ingredients))
