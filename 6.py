
print("Q6")

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

list1 = eval(input("Enter a list of numbers containing duplicates inside []:"))
list2 = Remove(list1)
print(list2)

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


bubbleSort(list2)

print('Sorted List in Ascending Order by Bubble sort:')
print(list2)

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


list3 = Remove(list1)
size = len(list3)
selectionSort(list3, size)
print('Sorted Array in Ascending Order by Selection sort:')
print(list3)
