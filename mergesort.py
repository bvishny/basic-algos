# Basic Merge Sort Implementation
# Components
# 1. split_array(array) array array - takes an array and splits it at the midpoint into two other arrays
# 2. merge(array, array) array - takes two split arrays and merges them together sorted
# 3. mergesort(array) array - takes an array and sorts it using mergesort

def split_array(array):
    split_pt = (len(array) / 2)
    return (array[:split_pt], array[split_pt:])

# Tests:
# Empty Array:
arr1, arr2 = split_array([])

if not (len(arr1) == 0 and len(arr2) == 0):
    print("Empty array failed")

# 1 Elem Array
arr1, arr2 = split_array([1])

if not (len(arr1) == 0 and len(arr2) == 1 and arr2[0] == 1):
    print("1 Elem array failed")

# Odd Elem Array
arr1, arr2 = split_array([1,2,4])

if not (len(arr1) == 1 and len(arr2) == 2 and arr2[-1] == 4):
    print("Odd Elem Array Failed")

# Even Elem Array
arr1, arr2 = split_array([1,2,3, 4])

if not (len(arr1) == 2 and len(arr2) == 2 and arr1[-1] == 2):
    print("Even Elem Array Failed")
    
# MERGE:

def merge(array1, array2):
    idx1, idx2, result = 0, 0, []

    while idx1 < len(array1) or idx2 < len(array2):
        if idx2 >= len(array2) or (idx1 < len(array1) and array1[idx1] <= array2[idx2]):
            result.append(array1[idx1])
            idx1 += 1
        else:
            result.append(array2[idx2])
            idx2 += 1
        
    return result

# Tests
result1 = merge([1,3,5], [2,4, 6])

if result1 != [1, 2, 3, 4, 5, 6]:
    print("Test 1: Same size failed")

result2 = merge([1,3], [2,4, 6])

if result2 != [1, 2, 3, 4, 6]:
    print("Test 2: Different sizes failed")

result3 = merge([1,3,5, 8], [2,4, 6])

if result3 != [1, 2, 3, 4, 5, 6, 8]:
    print("Test 3 failed")

result4 = merge([],[])

if result4 != []:
    print("Test 4: merge empty failed")

# MERGESORT:
def mergesort(array):
    if len(array) > 1:
        arr1, arr2 = split_array(array)
    else:
        return array
    
    return merge(mergesort(arr1), mergesort(arr2))
    

# Tests
result1 = mergesort([])

if result1 != []:
    print("Empty testfailed")

result2 = mergesort([1])

if result2 != [1]:
    print("1 test failed")
    
result3 = mergesort([1,5,2, 0, 3])

if result3 != [0,1,2,3,5]:
    print("Odd test failed")
    
result4 = mergesort([1,4,20, 2, 8, 5])

if result4 != [1,2,4,5,8,20]:
    print("Even test failed")

# Runtime Analysis - First Attempt:
# For a n size array, it will be split log(n) times. At each split there is also a merge, together comprising n elements merged
# across all the recursive calls. For this reason, the runtime is nlog(n)

# Runtime Analysis - Deeper Glance
# There are log2n + 1 (k) levels (cause n can be between 2 log2's), each with 2^j subproblems, of size n / 2^j 
# There are 4-6 operationsper eachitem