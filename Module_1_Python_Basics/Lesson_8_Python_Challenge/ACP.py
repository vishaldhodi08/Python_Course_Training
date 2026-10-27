
# ================================
# GROCERY COST COMPARISON TOOL
# ================================

print("=== GROCERY COST COMPARISON TOOL ===")


# ---------- PART 1: cost per person ----------
rice_price = 12
milk_price = 4
fruit_price = 8

number_of_baskets = 2
family_members = 4

basket_cost_per_person = (
    (rice_price + milk_price + fruit_price)
    * number_of_baskets
    / family_members
)

print("Basket cost per person:", basket_cost_per_person)


# ---------- PART 2: sharing items equally ----------
total_items = int(input("Enter the total number of items: "))
people = int(input("Enter the number of people: "))

if people == 0:
    print("You cannot share between 0 people.")
elif total_items % people == 0:
    items_each = total_items // people
    print("The items can be shared equally.")
    print("Items per person:", items_each)
else:
    remainder = total_items % people
    print("The items cannot be shared equally.")
    print("Remaining items:", remainder)


# ---------- PART 3: corrected weekly average ----------
recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

original_total = recorded_average * total_weeks
corrected_total = original_total - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks

print("Recorded average:", recorded_average)
print("Original total:", original_total)
print("Corrected average:", corrected_average)


# ---------- PART 4: compare with three stores ----------
store_a_average = 70
store_b_average = 75
store_c_average = 80

verdict = (
    store_a_average < store_b_average
    and store_b_average < store_c_average
)

print("Are store averages in increasing order?", verdict)


# ---------- PART 5: summary ----------
print("\n=== GROCERY SUMMARY ===")
print("Basket cost per person:", basket_cost_per_person)
print("Corrected weekly average:", corrected_average)
print("Store comparison verdict:", verdict)
