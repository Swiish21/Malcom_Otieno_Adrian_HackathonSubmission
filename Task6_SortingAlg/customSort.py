#below is  custom sort functions that take in a list of dictionaries and return the sorted list of dictionaries based on the 'marks' key in the dictionary
#the first one is in ascending order and the second one is in descending order.

def sort_dict_list(dict_list, key): # define a function and assign 2 parametres , one for the list of dictionaries and one for the key
    return sorted(dict_list, key=lambda x: x[key]) # here we use the sorted function to sort the list of dictionaries based on the key

dict_list = [ # create a list of dictionaries of a student and their marks
    {'name': 'Joe', 'score': 65},
    {'name': 'Mike', 'score': 78},
    {'name': 'John', 'score': 90},
    {'name': 'Alice', 'score': 40}
]

sorted_list = sort_dict_list(dict_list, 'score') # we define a variable to store the sorted list 
print(sorted_list) # print the sorted list

def sort_dict_desc(dict_list1, key): # define a function and assign 2 parametres , one for the list of dictionaries and one for the key
    return sorted(dict_list1, key=lambda x: x[key], reverse=True) # here it's the same as the above function, except we use the inbult reverse function to sort the list in descending order.

dict_list1 = [  # create a list of dictionaries of a student and their marks
    {'name': 'Eric', 'score': 82},
    {'name': 'Flex', 'score': 91},
    {'name': 'Joanna', 'score': 55},
    {'name': 'Reagan', 'score': 20}
]

sorted_list1 = sort_dict_desc(dict_list1, 'score') # we define a variable to store the sorted list
print(sorted_list1)# print the sorted list