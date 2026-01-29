# Sum of the Numbers in a String

raw_st = "1xyz23"

sum = 0
for char in raw_st:
    raw_st = raw_st.replace(char, " ") if not char.isdigit() else raw_st
    
numbers = raw_st.split()  

for num in numbers:
    sum += int(num)
    
print(sum)
