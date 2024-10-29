#below is a binary search algorithm that searches in a rotated sorted array
print("Binary Search Algorithm")
def search(nums, target): #we define a function for binary search with 2 parameters for the array to be searched and target element
    
    #we give the loop the left and right pointers
    left = 0 #index of the left pointer
    right = len(nums) - 1 #index of the right pointer
    
    while left <= right: #this is a while loop to loop over the array until the left pointer is less than or equal to the right pointer(ensures all elements are searched)
        
        mid = left + (right - left) // 2 #this is how we get the midpoint, by diving the total length of the array by 2
        
        if nums[mid] == target: #this if statement checks if the midpoint is equal to the target, if yes then it returns the index of the midpoint(same as target index)ending the loop
            return mid
        
        #below is how we handle the case where the array is rotated
        if nums[left] <= nums[mid]: # if the left pointer is less than or equal to the midpoint(meaning that side is sorted), we move to the nested if below, if not we go to else(21)
            if nums[left] <= target < nums[mid]: # here we check if the target is between the left and the midpoint(0 - target - midpoint)
                right = mid - 1 # if yes, we move the right pointer to the midpoint - 1
            else: 
                left = mid + 1 # if not, we move the left pointer to the midpoint + 1
        else:# if the left pointer is greater than the midpoint(meaning that side is not sorted)
            if nums[mid] < target <= nums[right]: # here we check if the target is between the midpoint and the right (midpoint - target - (-1))
                left = mid + 1 # if yes, we move the left pointer to the midpoint + 1
            else:
                right = mid - 1 # if not, we move the right pointer to the midpoint - 1
                
    return -1 # if the target is not found, we return -1

nums = [4, 5, 6, 7, 0, 1, 2] # the array to be searched
target = int(input("Enter the target element: ")) #user input for the target element
print(f"Element {target} found at index {search(nums, target)}") #we print the element and its index	
