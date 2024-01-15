'''write a program that takes a string and returns the number of unique characters in it'''

variable = "Guvi Geeks Network private limited"
variable = variable.lower()

unique_char_g = input("the character")

count_g = 0

for i in variable:
    if i == unique_char_g:
        count_g = count_g + 1
print("uniquechac",count_g)
    
    
