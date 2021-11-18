# 02_ingredients_list

def get_ingredients():

    ingredients = input("Please put in the name of each ingredient separated by commas: ")
    items = ingredients.split(',')  # split each ingredient with commas.
    items = [item.strip() for item in items]
    return(items)

get_ingredients()
