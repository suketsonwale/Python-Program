print("Program to read file and capitalize first letter of every words in the file") 

print("---------------------------------------------------------------------") 
print("By using capitalize()")
print(" ---------------------------------------------------------------------") 
fobj=open('temp.txt',"r") 
a=fobj.readline() 
sp=a.split() 
for ref in sp:     
    w=ref.capitalize()
    print(w) 
    fobj.close() 
    
print("-----------------------------------------------------------") 
print("By using title()") 
print("---------------------------------------------------------------------") 
fobj=open('temp.txt',"r") 
a=fobj.readline() 
sp=a.split() 
for ref in sp:     
    w=ref.title()
    print(w) 
    fobj.close() 
    
print("-------------------------------------------------------------------") 

import string 
print("by using capwords()") 
print(" --------------------------------------------------------------------- ")

 
fobj=open('temp.txt',"r") 
a=fobj.readline() 
sp=a.split() 
for ref in sp:     
    w=string.capwords(ref)  
    print(w) 
    fobj.close() 
