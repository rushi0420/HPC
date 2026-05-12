import time
from multiprocessing import Pool, cpu_count


# Sequential Bubble Sort
def sequential_bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(n - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		if not swapped:
			break
	return arr


# Helper function for parallel swapping
def process_pair(args):
	arr, j = args
	if arr[j] > arr[j + 1]:
		return (j, arr[j + 1], arr[j])
	return None


# Parallel Bubble Sort (Odd-Even)
def parallel_bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		first = i % 2
		swapped = False
		indices = [(arr, j) for j in range(first, n - 1, 2)]
		with Pool(cpu_count()) as p:
			results = p.map(process_pair, indices)
		for res in results:
			if res:
				j, val1, val2 = res
				arr[j], arr[j + 1] = val1, val2
				swapped = True
		if not swapped:
			break
	return arr


# Main
if __name__ == "__main__":
	n = int(input("Enter number of elements: "))
	arr = list(map(int, input("Enter elements: ").split()))
	arr_seq = arr.copy()
	arr_par = arr.copy()

	# Sequential
	start = time.time()
	sequential_bubble_sort(arr_seq)
	end = time.time()
	print("\nSequential Sorted:", arr_seq)
	print("Time (Sequential):", end - start, "sec")

	# Parallel
	start = time.time()
	parallel_bubble_sort(arr_par)
	end = time.time()
	print("\nParallel Sorted:", arr_par)
	print("Time (Parallel):", end - start, "sec")