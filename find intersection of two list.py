# Method 1 using for and if
print("Method 1 using for and if")
list1 = [10,11,12,13,14,15,16,17,18,19,20]
list2 = [11,23,12,10,15,20,45,13,18]
list3= []
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)


# Method 2 using function
print("Method 1 using function")
def pair(list1,list2):
    list3= []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3
list1 = [10,11,12,13,14,15,16,17,18,19,20]
list2 = [11,23,12,10,15,20,45,13,18]
print(pair(list1, list2))


# removing ith word from the list
#method 1 using new list
print("Method 1 using new list")
def removeword(word,remove,list1):
    list2=[]
    count = 0
    for i in list1:
        if word==i:
            count+=1
            if count != remove:
                list2.append(i)
        else:
            list2.append(i)
    if count==0:
        return False
    else:
        return list2
list1 = ["apple","banana","orange","apple"]
a = "apple"
remove = 2
print("original list : ",list1)
flag = removeword(a, remove, list1)
print("Updated list : ",flag)


#method 2 using del
print("\nMethod 2 using del() method")
def removeword(word,remove,list1):
    count = 0
    index = 0
    for i in list1:
        index +=1
        if word==i:
            count+=1
            if count == remove:
                del list1[index-1]
    if count==0:
        return False
    else:
        return True
list1 = ["apple","banana","orange","apple"]
a = "apple"
remove = 2
print("original list : ",list1)
flag = removeword(a, remove, list1)
print("Updated list : ",list1)

#method 3 using pop()
print("\nMethod 3 using pop() method")
def removeword(word,remove,list1):
    count = 0
    index = 0
    for i in list1:
        index +=1
        if word==i:
            count+=1
            if count == remove:
                list1.pop(index-1)
    if count==0:
        return False
    else:
        return True
list1 = ["apple","banana","orange","apple"]
a = "apple"
remove = 2
print("original list : ",list1)
flag = removeword(a, remove, list1)
print("Updated list : ",list1)