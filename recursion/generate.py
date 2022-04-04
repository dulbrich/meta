def helper(arr: list[int], target: int, idx_subproblem: int, partial_solution: list[int], total: int, result: list[list[int]]):
    #prune
    if total > target:
        return
    # base case
    if idx_subproblem == len(arr):
        if total == target and partial_solution not in result:
            partial_solution.sort()
            result.append(list(partial_solution))
        return

    # exclude
    helper(arr, target, idx_subproblem + 1, partial_solution, total, result)

    # include
    total += arr[idx_subproblem]
    partial_solution.append(arr[idx_subproblem])
    helper(arr, target, idx_subproblem + 1, partial_solution, total, result)
    partial_solution.pop()
    total -= arr[idx_subproblem]

def generate_all_combinations(arr, target):
    result = []
    arr.sort()
    helper(arr, target, 0, [], 0, result)
    return result

print(generate_all_combinations([1,1,1,1], 2))
print(generate_all_combinations([42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93], 83))
print(generate_all_combinations([94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94], 2256))
#print(generate_all_combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 300))

# [94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94]
# 2256

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# 300

#  [42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93]
# 83