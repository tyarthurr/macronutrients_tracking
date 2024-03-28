# UPDATE (28/03/24)
I've updated the script to remove hardcoded counts. Instead, the script now determines the user's basal metabolic rate and sets macro goals depending on whether the user is in a bulking, maintaining, or cutting phase. It does this with a bunch of variables that are declared at the start of the script which represents the user's overall consumed protein count, protein goal, meal-specific consumed protein count (this is declared later in the script), the same 3 variables but referring to kilojoules instead and a tuple containing the words: bulking, maintaining, cutting. The user is asked to input their age, height, and weight and is then asked to choose what phase they are in (with a number representing each option). Once the user chooses and inputs the corresponding number, the number is then used to index from the tuple which points to three if-statements, each using the Mifflin-St Jeor equation to determine the user's BMR and set protein and kilojoule goals that will achieve the dietary requirements of the user's desired phase. The script is then similar to what it was before except for UX being a bit friendlier and the script calling variables instead of hardcoded counts.

# Updated Learning
Playing around with variables, how to define and call a function (to spare myself from having redundant lines of repetitive code in the script), creating and indexing tuples which then determine which if-statement to run, learning that tuples are better than lists for a fixed collection of items, commenting above each new code block to make the code easier to navigate, executing an infinite loop at the end of the script so that the terminal doesn't close on the user straight away.

# Description
Python script that tracks and manages macronutrients (specifically, protein and kilojoules) each day under user-specified macronutrient count goals. 

Script will prompt user to input how much protein and kilojoules they've consumed after their first meal of the day then subtract those integers (input data type is force-defined) from the hardcoded macronutrient counts (defined as integer variables) and display the result to the user so the user knows how much more macronutrients they need to consume for the day. The script will keep looping for subsequent meals while tracking previous inputs until the hardcoded count goals are met. Nested while loops are used to change the prompt depending on if the user meets one macronutrient count goal but not the other and vice versa. 

Once both macronutrient count goals have been met, script will notify the user then terminate.
# What did I learn?
Practising while loops, comparison operations, and force-defining data types. Making user experience more friendly by changing the prompt and displayed information depending on if one goal has been met but the other hasn't (with the use of while loop nesting). Fixing up lines with too many characters and adding a line at the end of a script to abide by PEP 8 guidelines.
