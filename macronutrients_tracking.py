protein_count = 0
kilojoule_count = 0

print("How much protein have you had?")
protein_consumed = int(input())
protein_count = protein_count + protein_consumed

print("How many kilojoules have you had?")
kilojoules_consumed = int(input())
kilojoule_count = kilojoule_count + kilojoules_consumed

while protein_count < 150 or kilojoule_count < 8000:
    print("You have", 150 - protein_count, "grams of protein left and you have", 8000 - kilojoule_count,
          "kilojoules left. When you eat again, tell me how much more protein you had, here:")
    protein_consumed = int(input())
    print("Thanks! Now, how many more kilojoules have you had?")
    kilojoules_consumed = int(input())

    protein_count = protein_count + protein_consumed
    kilojoule_count = kilojoule_count + kilojoules_consumed

    while protein_count > 149 and kilojoule_count < 8000:
        print("You have", 8000 - kilojoule_count,
              "kilojoules left. When you eat again, tell me how many kilojoules you had, here:")
        kilojoules_consumed = int(input())
        kilojoule_count = kilojoule_count + kilojoules_consumed

    while protein_count < 150 and kilojoule_count > 7999:
        print("Nothing but protein from here on out. You have", 150 - protein_count,
              "grams of protein left. When you eat again, tell me how much more protein you had, here:")
        protein_consumed = int(input())
        protein_count = protein_count + protein_consumed

print("You have consumed the recommended 150+ grams of protein and 8000+ kilojoules. Lift on, brother.")
