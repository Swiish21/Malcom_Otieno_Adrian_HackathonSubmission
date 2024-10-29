//this is the entry point of this dart program
void main() {
  List<int> numbers = [5, 2, 8, 3, 1, 6, 4, -1, 0, 13];// defining a list of integers we are going to sort
  List<int> sortedNumbers = mergeSort(numbers); // defining a var that we'll use to store the sorted list
  print(sortedNumbers); // printing out the sorted list
}


List<int> mergeSort(List<int> list) { //defining a the merge sort funtion and the parameter is the list we want to sort will be a parameter. We start defing the function with List<int> because we are going to return a list in this function.
  if (list.length <= 1) { //if our list length is less than or equal to 1, it means it already sorted hence no need to run the algorithm
    print('This list has a length of 0 or 1, it is already sorted'); // a simple print statement
    return list; // return the list
  }

  int middle = list.length ~/ 2; // defining a var that stores the middle point of the list of the list
  List<int> left = list.sublist(0, middle); // defining a var that stores the left half of the list, from index 0 to the middle point
  List<int> right = list.sublist(middle); // defining a var that stores the right half of the list, from the middle point to the end of the list

  return merge(mergeSort(left), mergeSort(right)); // this line of code will merge the two halves of the list and return the result
}

List<int> merge(List<int> left, List<int> right) { // here we are defining the merge function and the parameters are the two halves of the list
  List<int> result = [];// the we'll need somewhere to store the sorted list, hence the var result
  int i = 0, j = 0; // the two pointers(i- left and j- right) that will be used to traverse the two halves of the list

  while (i < left.length && j < right.length) { // to iterate through the list we use a while loop, as a condition we need to check if the pointers are less than the length of the list first
    if (left[i] <= right[j]) { //we use an if statement to compare the elements of the two lists
      result.add(left[i++]); // if the left element is less than the right element, we add the left element to the result list
    } else {
      result.add(right[j++]); // else, we add the right element to the result list
    }
  }

  result.addAll(left.sublist(i)); // if at one point the left list is longer than the right list, we add the rest of the elements to the result list 
  result.addAll(right.sublist(j)); // if at one point the right list is longer than the left list, we add the rest of the elements to the result list
  return result; // return the result(the sorted list)
}