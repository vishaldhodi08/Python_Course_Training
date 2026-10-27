
# ================================
# SWIMMING POOL ENTRY CHECKER
# ================================

print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")


# ---------- collect the three answers ----------
age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)


# ---------- PART 1: age group ----------
if age < 4:
    age_group = "Toddler"
    pool_access = "Splash pool only, always with an adult"
elif age < 12:
    age_group = "Child"
    pool_access = "Main pool with an adult"
elif age < 18:
    age_group = "Teen"
    pool_access = "Main pool alone if you can swim"
else:
    age_group = "Adult"
    pool_access = "All pools open to you"

print("Age group:", age_group)
print("Pool category:", pool_access)


# ---------- PART 2: validate answers ----------
if can_swim != "yes" and can_swim != "no":
    print("Input error: Please answer yes or no for swimming.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Input error: Please answer yes or no for adult presence.")
    adult_known = False
else:
    adult_known = True


# ---------- PART 3: AND - the deep pool ----------
if swim_known and adult_known:
    if can_swim == "yes" and adult_here == "yes":
        print("Deep pool: You meet the swimming and adult-presence conditions.")
    else:
        print("Deep pool: Entry conditions are not met.")


# ---------- PART 4: OR - the shallow end ----------
if can_swim == "no" or age < 12:
    print("Shallow end: Please take extra care.")


# ---------- PART 5: NOT - the lifeguard reminder ----------
if adult_known and not (adult_here == "yes"):
    print("Reminder: An adult is not with you.")


# ---------- PART 6: final verdict ----------
if not swim_known or not adult_known:
    print("Final verdict: Cannot decide until the answers are corrected.")
elif age < 4:
    if adult_here == "yes":
        print("Final verdict: Splash pool only, with an adult.")
    else:
        print("Final verdict: Please bring an adult before entering.")
elif age < 12:
    if adult_here == "yes":
        print("Final verdict: Main pool with an adult.")
    else:
        print("Final verdict: Please bring an adult before entering.")
elif age < 18:
    if can_swim == "yes":
        print("Final verdict: Main pool access, subject to pool rules.")
    else:
        print("Final verdict: Swimming supervision or lessons are needed.")
else:
    print("Final verdict: Adult category. Follow the pool's safety rules.")

print()
print("Have a safe swim!")
