print("Program to create dictionary with key as first character and value as a word in the string ")  
print("----------------------------------------------------------------------")  
stirng = input("Enter any string :-")  
print("----------------------------------------------------------------------")  
sstring = stirng.split()  
dict={}  
for ref in sstring:     
    if ref[0]not in dict.keys():  
        dict[ref[0]] = [ref]     
    else:         
        dict[ref[0]].append(ref) 
print(dict)