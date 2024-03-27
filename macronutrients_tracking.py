# Declaring variables
protein_count = 0
kilojoule_count = 0
protein_goal = 0
kilojoule_goal = 0
macro_goal = ["bulking", "maintaining", "cutting"]


# Defining while loop function: If a condition is met and the other isn't, drop the met condition from being prompted
def exceeded_macro_check():
    global kilojoule_count
    global protein_count
    global protein_goal
    global kilojoule_goal
    global kilojoules_consumed
    global protein_consumed

    while protein_count > protein_goal and kilojoule_count < kilojoule_goal:
        print("You have",
              kilojoule_goal - kilojoule_count,
              "kilojoules left. When you eat again, tell me how many kilojoules you had, here:")
        kilojoules_consumed = int(input())
        kilojoule_count = kilojoule_count + kilojoules_consumed

    while protein_count < protein_goal and kilojoule_count > kilojoule_goal:
        print("Nothing but protein from here on out. You have",
              protein_goal - protein_count,
              "grams of protein left. When you eat again, tell me how much more protein you had, here:")
        protein_consumed = int(input())
        protein_count = protein_count + protein_consumed


# Asking user for input on BMR factors
print("How old are you?")
user_age = int(input())
print("How tall are you in centimetres?")
user_height = int(input())
print("How much do you weigh in kilograms?")
user_weight = int(input())

# User input picks their dietary goals from macro_goal list
print("""Choose one of the below. Are you:
      1. Bulking
      2. Maintaining
      3. Cutting
Enter your chosen number below.""")
macro_goal_answer = int(input()) - 1
macro_goal = macro_goal[macro_goal_answer]

# Determining BMR and setting macro parameters for each option in the macro_goal list with Mifflin-St Jeor equation
if macro_goal[macro_goal_answer] == macro_goal[0]:
    protein_goal = (user_weight * 2.205) * 0.7
    kilojoule_goal = (((10 * user_weight + 6.25 * user_height - 5 * user_age + 5) * 1.55) * 4.184) * 1.2
    print("Today, you want to eat",
          protein_goal, "grams of protein and",
          kilojoule_goal, "kilojoules.")

elif macro_goal[macro_goal_answer] == macro_goal[1]:
    protein_goal = user_weight * 2.205
    kilojoule_goal = ((10 * user_weight + 6.25 * user_height - 5 * user_age + 5) * 1.55) * 4.184
    print("Today, you want to eat",
          protein_goal, "grams of protein and",
          kilojoule_goal, "kilojoules.")

elif macro_goal[macro_goal_answer] == macro_goal[2]:
    protein_goal = user_weight * 2.205
    kilojoule_goal = (((10 * user_weight + 6.25 * user_height - 5 * user_age + 5) * 1.55) * 4.184) * 0.8
    print("Today, you want to eat",
          protein_goal, "grams of protein and",
          kilojoule_goal, "kilojoules.")

# Asking user for consumed macros count which is recorded as ****_consumed then added onto ****_count
print("Now, how much protein have you had?")
protein_consumed = int(input())
protein_count = protein_count + protein_consumed

print("Brilliant. How many kilojoules have you had?")
kilojoules_consumed = int(input())
kilojoule_count = kilojoule_count + kilojoules_consumed

# Calling the function that was defined in Line 13
exceeded_macro_check()

# While the count is below the goal, keep asking for more input
while protein_count < protein_goal and kilojoule_count < kilojoule_goal:
    print("You have",
          protein_goal - protein_count,
          "grams of protein left and you have",
          kilojoule_goal - kilojoule_count,
          "kilojoules left. When you eat again, tell me how much more protein you had, here:")
    protein_consumed = int(input())
    print("Thanks! Now, how many more kilojoules have you had?")
    kilojoules_consumed = int(input())

    protein_count = protein_count + protein_consumed
    kilojoule_count = kilojoule_count + kilojoules_consumed

    # Calling the function that was defined in Line 13
    exceeded_macro_check()

# Congratulatory statement and running infinite loop to keep script up so that user can close terminal when ready
print("You have consumed the recommended",
      protein_goal, "grams of protein and",
      kilojoule_goal, "kilojoules. Lift on, brother.")
while True:
    pass
