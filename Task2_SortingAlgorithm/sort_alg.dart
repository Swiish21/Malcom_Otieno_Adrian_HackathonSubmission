// void main is the entry point of the dart program
void main () {

List<int> quickSort(List<int> list) { // defining a function and calling it quickSort, its parameter is the list we want to sort
  if (list.length <= 1) { //if our list length is less than or equal to 1, it means it already sorted hence no need to run the algorithm
    return list; // return the list
  }

  int pivot = list[0]; // define a var that hold the pivot element in the list, zero in our case
  List<int> less = []; // define a var that will store the elements less than the pivot
  List<int> greater = []; // define a var that will store the elements greater than the pivot

  for (int i = 1; i < list.length; i++) { // using a for  loop to go through the list
    if (list[i] <= pivot) { // if the element is less than or equal to the pivot
      less.add(list[i]); // add the element to the less list
    } else {
      greater.add(list[i]); // if not, add the element to the greater list
    }
  }

  return quickSort(less) + [pivot] + quickSort(greater); // here we combine 3 things, the less than pivot list, the pivot element and the greater than pivot list
  // after combining we return the result
}

  List<int> numbers = [5, 2, 8, 3, 1, 6, 4, 13, -1, 0]; // an example of a list to be sorted
  List<int> sortedNumbers = quickSort(numbers); // declaring a list variable that will store the result of the quickSort function 
  print(sortedNumbers); // printing out the sorted list

}