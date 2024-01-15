variable = input("enter the string")

unique_char = input("enter the unique char")
count = 0
for i in variable:
    if(i==unique_char):
        count = count +1
        if(count>=2):
            print("the char", unique_char)
print("count of unique char: ",count)

  