#String functions

# 1-->To check length of a string
string="hello"
print(len(string))

#2-->To convert characters into uppercase
str="saieswar"
print(str.upper())

#3-->To convert characters into lowercase
str="HARSHA"
print(str.lower())

#4-->To capitalize first character capital.
str="sai"
print(str.capitalize())

#5-->To remove leading and trailing whitespaces
str=" saieswar   "
print(str.strip())

#6-->To replace occurrences of a substring with another substring.
str="hi saieswar"
print(str.replace("hi","hello"))

#7--->To join two words into a single string
str1=["hi","sai"]
print(" ".join(str1))

#8-->To check all characters in the string are digits ot not
str2 = "2801"
print(str2.isdigit())

#9-->To check all characters in the string are alphabets ot not
str2 = "sai"
print(str2.isalpha())

#10-->To check all characters in the string are alphanumeric ot not
str2 = "sai7299"
print(str2.isalnum())
