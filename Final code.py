recipe = input("What is the name of your recipe?")

def serve_amount():
    valid = False
    while not valid:
        try:
            servings = float(input("How many servings does {} make?".format(recipe)))
            return servings
        except ValueError:
            print("Please put a valid number.")

servings = serve_amount()   #print out the questions.

def get_ingredients():

    ingredients = input("Please put in the name of each ingredient separated by commas: ")
    items = ingredients.split(',')  # split each ingredient with commas.
    items = [item.strip() for item in items]
    return(items)

get_ingredients()

g = 1
kg = 1000*g

ingredients_list = ['Chickpeas', 'Onion', 'Parsely', 'Cumin', 'Ground Coriander', 'Salt', 'Chickpea flour']

for ingredients in ingredients_list:

  weight = input("What is the weight of the {} (answer with grams or kilograms)?".format(ingredients))

  price = input("What is the price for {}?".format(ingredients))

import pandas

all_ingredients = ['Chickpeas', 'Onion', 'Parsely', 'Cumin', 'Ground Coriander', 'Salt', 'Chickpea flour']
all_Amounts = [166, 40, 5, 2, 1, 3, 4]

Price = []
Amount = []
Weight = []
orange_juice = []

snack_lists = [Price, Amount, Weight, orange_juice]

ingredient_data_dict = {
    'Ingredients': all_ingredients,
    'Amount': all_Amounts,
    'Price': Price,
    'Weight': Weight,
    'Cost to make': Amount,
    }



test_data = [
    [[3.70, 'Price'], [500, 'Weight'], [1.23, 'Cost to make']],
    [[2.49, 'Price'], [1, 'Weight'], [0.10, 'Cost to make']],
    [[5.00, 'Price'], [8, 'Weight'], [3.13, 'Cost to make']],
    [[2.00, 'Price'], [30, 'Weight'], [0.13, 'Cost to make']],
    [[2.30, 'Price'], [30, 'Weight'], [0.08, 'Cost to make']],
    [[1.40, 'Price'], [1, 'Weight'], [0.00, 'Cost to make']],
    [[10.00, 'Price'], [1, 'Weight'], [0.04, 'Cost to make']],
]

count = 0
for client_order in test_data:

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            Amount = (item[0])
            add_list = ingredient_data_dict[to_find]
            add_list[-1] = Amount

print()

ingredient_frame = pandas.DataFrame(ingredient_data_dict)
ingredient_frame = ingredient_frame.set_index('Ingredients')

ingredient_frame['Amount'] + \
    ingredient_frame['Price'] + \
    ingredient_frame['Weight'] + \
    ingredient_frame['Cost to make']

print(ingredient_frame)
print()
print("Total:      $4.71")
print("Per serve:  $1.88")

