'''Wrie a python program to calculate the total number of Vowels and count of each individual vowel A, E, I, O, U in the string 
"Guvi Geeks Network Private Limited"?
'''

variable = "Guvi Geeks Network Private Limited"
count_all_vowels = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for i in variable:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count_all_vowels = count_all_vowels + 1
    if i == 'a':    
        count_a = count_a + 1
    if i == 'e':    
        count_e = count_e + 1
    if i == 'i':    
        count_i = count_i + 1
    if i == 'o':    
        count_o = count_o + 1
    if i == 'u':    
        count_u = count_u + 1
print("total number of vowels in the string 'Guvi Geeks Network Private Limited'", count_all_vowels)
print("count of vowel 'a' is", count_a)
print("count of vowel 'e' is", count_e)
print("count of vowel 'i' is", count_i)
print("count of vowel 'o' is", count_o)
print("count of vowel 'u' is", count_u)
