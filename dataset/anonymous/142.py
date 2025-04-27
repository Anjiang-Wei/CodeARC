def solution(arr):
	max_so_far = min_ending = max_ending = arr[0]
	for n in arr[1:]:
		min_ending, max_ending = min(n, min_ending * n, max_ending * n), max(n, min_ending * n, max_ending * n)
		max_so_far = max(max_so_far, max_ending)
	return max_so_far

