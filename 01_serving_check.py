# 01_serving_check

recipe = input("What is the name of your recipe?")

def serve_amount():
    valid = False
    while not valid:
        try:
            servings = float(input("How many servings does {} make?".format(recipe)))
            return servings
        except ValueError:
            print("Please put a valid number.")

servings = serve_amount()  #print out the qurstions.

