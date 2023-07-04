print("program to find length of list by using recursion") 
print("---------------------------------------------------------------------")
def list_length(my_list):    
    if not my_list: 
        return 0
    return 1 + list_length(my_list[1::2]) + list_length(my_list[2::2]) 
    
my_list = [1, 2, 3, 34, 52, 78] 
print("The list is :") 
print(my_list) 
print("The length of the string is : ") 
print(list_length(my_list))