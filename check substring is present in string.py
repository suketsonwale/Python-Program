print("Program to check if a substring is present in given string.")
print("1. By using if...and...in :")
s="An Apple keeps Doctor away."
sub="Apple"
print("String is :-",s,"\nSubstring is :-",sub)
if sub in s:
    print(sub," substring is present in : ",s)
else:
    print("Substring is not found.")

print("\n---------------------------------------------------\n")
print("2. By using Spilt()")
s="close the door of car."
sub="close"
print("String is :-",s,"\nSubstring is :-",sub)
a=s.split(" ")
for ref in a:
    if ref==sub:
        print(sub," substring is present in : ",s)

print("\n---------------------------------------------------\n")
print("3. By using Find()")
s="The Sun is star."
print("String is :-",s,"\nSubstring is :- the")
if s.find("the")==-1:
    print(">>word is not Found")
else:
    print("the substring is present in : ",s)

print("\n---------------------------------------------------\n")
print("4. By using count()")
s="Create new folder for storing data"
print("String is :-",s,"\nSubstring is :- for")
if s.count("for"):
    print("for substring is present in : ",s)

print("\n---------------------------------------------------\n")
print("5. By using index()")
s="Sun is the largest star."
print("String is :-",s,"\nSubstring is :- largest")
print("Word Found at ",s.index("largest"))

print("\n---------------------------------------------------\n")
print("6. By using _contains_()")
s="library have so many books."
sub="library"
print("String is :-",s,"\nSubstring is :-",sub)
if s.__contains__(sub):
    print(sub," substring is present in : ",s)
    