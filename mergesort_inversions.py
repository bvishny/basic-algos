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
class Counter(object):
    def __init__(self):
        self.total = 0
    
    def incr(self, amt):
        self.total += amt
    
    def count(self):
        return self.total

def merge(array1, array2, counter):
    idx1, idx2, result = 0, 0, []

    while idx1 < len(array1) or idx2 < len(array2):
        if idx2 >= len(array2) or (idx1 < len(array1) and array1[idx1] <= array2[idx2]):
            result.append(array1[idx1])
            idx1 += 1
        else:
            result.append(array2[idx2])
            idx2 += 1
            counter.incr(len(array1) - idx1)
        
    return result


# MERGESORT:
def mergesort(array, counter = Counter()):
    if len(array) > 1:
        arr1, arr2 = split_array(array)
    else:
        return array
    
    return merge(mergesort(arr1, counter), mergesort(arr2, counter), counter)

c = Counter()
result3 = mergesort([1,5,2, 0, 3], c)

print(c.count())

