#declaration/creation of list1 : 
list1 = [1,2,3,4,5,6]

print("\n\n --------- Declaration of list ---------")
print("List1 is : ",list1)

#special element get from list : access list item at index 2.
#Access list item
print("\n\n --------- Access list item ---------")
print("Element at index 2 in list1 is : ",list1[2])

#add list item :
print("\n\n --------- Adding item to list ---------")
print("1.Using append :")
print("List1 before adding item  : ",list1)
list1.append(7)
print("List1 after adding item : ",list1)

print("\n2.Using insert :")
print("List1 before adding item  : ",list1)
list1.insert(2, 15)
print("List1 after adding item : ",list1)



#remove list1 item using pop,remove and del method.
print("\n\n --------- Removing list item ---------")
print("1.Using pop.")
print("pop item from list 1 is : ",list1.pop())
print("List1 after poping a element : ",list1)

print("\n2.Using remove.")
list1.remove(2)
print("List1 after removing element 2 : ",list1)

print("\n3.Using del (delete).")
del list1[1]
print("List1 after deleting a element : ",list1)

#change list item
print("\n\n --------- Changing list item ---------")
print("List1 before changing element at index 2 : ",list1)
list1[2] = 10
print("List1 after changing element at index 2 : ",list1)

#union of two list :
print("\n\n --------- Union of two list ---------")
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10]
print("List 1 is : ",list1)
print("list 2 is : ",list2)

print("\n1.Using + opreator :")
list3 = list1+list2
print("union of list1 and list2 is : ",list3)

print("\n2.Using extend :")
list1.extend(list2)
print("union of list1 and list2 is : ",list1)
