# Remove all vowels from the String

instr = "take u forward"

for char in instr:
    if char in "aeiouAEIOU":
        instr = instr.replace(char, "")
        
print(instr)