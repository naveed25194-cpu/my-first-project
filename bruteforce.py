# def has_common_bruteforce(A, B):
#     for a in A:
#         for b in B:
#             if a == b:
#                 return True
#     return False

# # Test
# A = [3, 8, 1, 5, 9]
# B = [4, 2, 7, 8, 6]
# print(has_common_bruteforce(A, B))  # True






# # sorting + binary search
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False

# def has_common_sort_search(A, B):
#     A_sorted = sorted(A)
#     for b in B:
#         if binary_search(A_sorted, b):
#             return True
#     return False

# # Test
# A = [3, 8, 1, 5, 9]
# B = [4, 2, 7, 8, 6]
# print(has_common_sort_search(A, B))  # True








# # On hashing method
# def has_common_hashing(A, B):
#     set_A = set(A)  # Convert to hash set - O(n)
#     for b in B:      # Check each element - O(n)
#         if b in set_A:  # O(1) average
#             return True
#     return False

# # Even shorter:
# def has_common_hashing2(A, B):
#     return len(set(A) & set(B)) > 0

# # Test
# A = [3, 8, 1, 5, 9]
# B = [4, 2, 7, 8, 6]
# print(has_common_hashing(A, B))  # True









# algorithm to find max in an array and count comparisons and show that it is n-1 comparisons in all cases (best, worst, random)
def findMaxWithCount(E):
    """Find max and count comparisons"""
    comparisons = 0
    max_val = E[0]
    
    for i in range(1, len(E)):
        comparisons += 1  # Count this comparison
        if max_val < E[i]:
            max_val = E[i]
    
    return max_val, comparisons

# Test it
test_arrays = [
    [100, 90, 80, 70],  # Best case (but still n-1 comparisons!)
    [10, 20, 30, 40],   # Worst case (n-1 comparisons)
    [5, 2, 8, 1, 9],    # Random case (n-1 comparisons)
]

for arr in test_arrays:
    max_val, comps = findMaxWithCount(arr)
    print(f"Array: {arr}")
    print(f"Max: {max_val}, Comparisons: {comps}")
    print(f"n-1 = {len(arr)-1}, Optimal? {comps == len(arr)-1}\n")