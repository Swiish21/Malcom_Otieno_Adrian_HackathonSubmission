print("Ternary Search")
print('The array is sorted in ascending order')
def ternary_search(arr, target): #defined a function for ternary search with 2 parameters for the array to be searched and target element
    
    left = 0 #initialising the left pointer for the array
    right = len(arr) - 1 #initialising the right pointer for the array
    
    while left <= right: #a while to loop over the array until the left pointer is less than or equal to the right pointer, to ensure all elements are searched
        
        #a ternary search alg splits the array in 3 parts, in the 3 parts we have 2 midpoints
        mid1 = left + (right - left) // 3 # this is how we get the midpoint 1, by idving the total length of the array by 3
        mid2 = right - (right - left) // 3 # this is how we get the midpoint 2, by idving the total length of the array by 3

        if arr[mid1] == target: # this if statement checks if the midpoint 1 is equal to the target
            return mid1
        if arr[mid2] == target: # this if statement checks if the midpoint 2 is equal to the target
            return mid2
        #if the target is found to be either the midpoint 1 or the midpoint 2, we return the index and our loop ends

        #below we are checking the rest of the elements that are not the midpoints
        #if the element checked doesn't meet the requirements, we move the pointers to the next element (reducing the search space)
        if target < arr[mid1]: #if the target element is less than the midpoint 1(if target is in the left part of the array)
            right = mid1 - 1 # we move the right pointer to the midpoint 1 - 1
        elif target > arr[mid2]: # if the target element is greater than the midpoint 2(if target is in the right part of the array)
            left = mid2 + 1 # we move the left pointer to the midpoint 2 + 1
        else: # if the target element is neither less than the midpoint 1 nor greater than the midpoint 2 (target is in the middle part of the array)
            left = mid1 + 1 # we move the left pointer to the midpoint 1 + 1
            right = mid2 - 1 # we move the right pointer to the midpoint 2 - 1

    return -1 # if the target is not found, we return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] # the array to be searched
target = int(input("Enter the target element: ")) #user input for the target element

index = ternary_search(arr, target) #calling the function and assigning it to a variable called index
if index != -1: #if the index is not equal to -1, means that the element was found
    print(f"Element {target} found at index {index}") #we print the element and its index
else:
    print(f"Element {target} not found in the array") #we print that the element was not found