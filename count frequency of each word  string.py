# program to count frequency of each word appearing in a string using dictionary :-
string = input("\nEnter a string : ")
List = []
List = string.split(" ")
word = [List.count(i) for i in List]

print(dict(zip(List,word)))