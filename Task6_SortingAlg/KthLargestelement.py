#below is a simple python algorithm to find the kth largest element in a list
def find_kth_largest(nums, k): # we start by defining a function with two parametres, one for the list and one for the value of k

    nums.sort(reverse=True) # we use pythons inbuilt sort function to sort the list, then we reverse it from largest to smallest using the reverse function
 
    return nums[k-1] # then we return the kth largest element, but the value of k is given by the user


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] # we create a list of numbers to test the function
print('The length of the list is:', len(nums), '\n') # a simple print statement to show the length of the list, for the user to know how many numbers are in the list(stay in range during input)
k = int(input('Enter the value of k: ')) # we ask the user to input the value of k
result = find_kth_largest(nums, k) # we call the function with the list and the value of k, and assign the result to a variable
print('The ', k, 'th largest element is:', result, '\n') # we print the result..
