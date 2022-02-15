# divide and conquer
def mergesort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergesort(L)
  
        # Sorting the second half
        mergesort(R)
  
        # merge arrays
        mergearrays(arr, L, R)

def mergearrays(arr, L, R):
	i = j = k = 0
	# Copy data to temp arrays L[] and R[]
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Checking if any element was left
	while i < len(L):
		arr[k] = L[i]
		i += 1
		k += 1

	while j < len(R):
		arr[k] = R[j]
		j += 1
		k += 1

test_array = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
test_array = [12, 11, 13, 5, 6, 7]
mergesort(test_array)
print(test_array)