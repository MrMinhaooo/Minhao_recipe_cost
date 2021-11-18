import pandas
# Initialise snack lists...

all_ingredients = ['Chickpeas', 'Onion', 'Parsely', 'Cumin', 'Ground Coriander', 'Salt', 'Chickpea flour']
all_Amounts = [166, 40, 5, 2, 1, 3, 4]

Price = []
Amount = []
Weight = []
orange_juice = []

snack_lists = [Price, Amount, Weight, orange_juice]


# Data Frame  Dictionary
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

    # print(snack_lists)

    # get order (hard order for easy testing)...
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            Amount = (item[0])
            add_list = ingredient_data_dict[to_find]
            add_list[-1] = Amount

print()

# Create dataframe set index to Ingredients column
ingredient_frame = pandas.DataFrame(ingredient_data_dict)
ingredient_frame = ingredient_frame.set_index('Ingredients')

# create column called 'Sub Total'
# fill is price for snacks and Amount

ingredient_frame['Amount'] + \
    ingredient_frame['Price'] + \
    ingredient_frame['Weight'] + \
    ingredient_frame['Cost to make']

print(ingredient_frame)
print()
print("Total:      $4.71")
print("Per serve:  $1.88")
