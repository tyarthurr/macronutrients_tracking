# UPDATE (28/03/24)
TBC.
# Description
Python script that tracks and manages macronutrients (specifically, protein and kilojoules) each day under user-specified macronutrient count goals. 

Script will prompt user to input how much protein and kilojoules they've consumed after their first meal of the day then subtract those integers (input data type is force-defined) from the predefined macronutrient counts (defined as integer variables) and display the result to the user so the user knows how much more macronutrients they need to consume for the day. The script will keep looping for subsequent meals while tracking previous inputs until the predefined count goals are met. Nested while loops are used to change the prompt depending on if the user meets one macronutrient count goal but not the other and vice versa. 

Once both macronutrient count goals have been met, script will notify the user then terminate.
# What did I learn?
Practising while loops, comparison operations, and force-defining data types. Making user experience more friendly by changing the prompt and displayed information depending on if one goal has been met but the other hasn't (with the use of while loop nesting). Fixing up lines with too many characters and adding a line at the end of a script to abide by PEP 8 guidelines.
