
# ================================
# DAILY ACTIVITY PLANNER
# ================================

# ---------- PART 1: homework time ----------
homework_minutes = int(input("Enter your homework time in minutes: "))


# ---------- PART 2: choose a plan ----------
if homework_minutes > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")


# ---------- PART 3: free time ----------
free_time = input("Is there free time after homework? (yes/no): ")

if free_time == "yes":
    print("Remember to pick a hobby for your free time!")


# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
print("Homework minutes:", homework_minutes)
print("Plan:", plan)
print("Free time answer:", free_time)
