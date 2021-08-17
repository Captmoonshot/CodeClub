# allergy_detector.py
# by Sammy Lee

"""The following function uses a Python set to detect allergies in food recipes"""

def detect_allergies(dish, recipe, allergies):
    """The following function uses the python
    intersection method to detect potential allergies in food"""
    allergic = recipe.intersection(allergies)
    if len(allergic) > 0:
        print(f"Allergies detected for {dish}: {allergic}")
    else:
        print(f"Allergies detected for {dish}: None")



my_allergies = {"peanuts", "fish", "wheat", "mayonnaise", "dog"}

baked_salmon = {"fish", "mayonnaise", "lemon"}

mac_and_cheese = {"pasta", "cheese"}

shrimp_salad = {"fish", "lettuce", "lemon"}

print(f"""
I have the folling recipes:
\t*baked_salmon: {baked_salmon}
\t*mac_and_cheese: {mac_and_cheese}
\t*shrimp_salad: {shrimp_salad}
""")

print()

print(f"My allergies include: {my_allergies}")

print()

print("""I will now try to find out if any of these recipes are allergic with my
handy little function called detect_allergies().""")

print()

detect_allergies("baked salmon", baked_salmon, my_allergies)
detect_allergies("mac and cheese", mac_and_cheese, my_allergies)
detect_allergies("shrimp salad", shrimp_salad, my_allergies)

print()


