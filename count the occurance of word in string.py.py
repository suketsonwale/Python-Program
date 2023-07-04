# practical 5
s = input("Enter a Sentence : ")
word = input("Enter the word to search : ")
count=0

a=s.split(" ")
for ref in a:
    if ref==word:
        count=count+1
print("The ",word," present ",count," times in the given string.")


    

