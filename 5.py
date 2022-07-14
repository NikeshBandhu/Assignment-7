print("Q5")
#5a

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

n = eval(input("Enter a list in [] brackets:"))

print(quicksort(0,len(n)-1,n))

#5b
def binary_search(list1, x):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < x:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > x:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial list1    
x = int(input("Enter the element you want to search :"))
  
# Function call   
result = binary_search(n, x)  
  
if result != -1:  
    print("Element is present at index", n.index(x))  
else:  
    print("Element is not present in list1")  

#5c
count = 0
for i in n:
    if i == x:
        count += 1
print(f'Number of occurences of element {x} is: {count}')
