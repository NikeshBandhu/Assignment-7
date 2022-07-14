def partition(l, r, nums):
	
	pivot, ptr = nums[r], l
	for i in range(l, r):
		if nums[i] <= pivot:
			
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr += 1
	
	nums[ptr], nums[r] = nums[r], nums[ptr]
	return ptr


def quicksort(l, r, nums):
	if len(nums) == 1: 
		return nums
	if l < r:
		pi = partition(l, r, nums)
		quicksort(l, pi-1, nums) 
		quicksort(pi+1, r, nums) 
	return nums


example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quicksort(0, len(example)-1, example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
print(quicksort(0, len(example)-1, example))
def heapify(nums, heap_size, root_index):
    
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)
def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))