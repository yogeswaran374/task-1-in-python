variable1=input("enter the string1 : ")
variable2=input("enter the string2 : ")
len1 = len(variable1)
len2 = len(variable2)
if(len1==len2 and sorted(variable1)==sorted(variable2)):
    print("the strigs are anagram")
else:
    print("the strings are not anagram")