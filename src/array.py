# ---- properties of arrays ----

# a sequence of elements
# all elements are the same data type
# occupies a contiguious block of memory
# look up equation for any element is: memory_address = starting_address + (index * size_of_data_type)


# ---- properties of hash funtions ----

# deterministic: for the same input the function always gives the same output
# no redundancy: function uses ALL the input data
# uniform: function uniformly distributes all output values evenly across all possible output values
# chaotic: function produces very different values for similar inputs
# non invertible
# predictable speeds. Hash tables fast, decrypt hashes slow


# ---- properties of hash tables ----

# Have an array like structure
# Indexed using a hash function, in an unordered way; arrays are always indexed by contiguous ordered indices




# Add up and print the sum of the all of the minimum elements of each inner array:
arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

sum = 0

for elem in arr:
    min_elem = min(elem)
    sum += min_elem
print(sum)


# Add up and print the sum of the all of the minimum elements of each inner array. Each array may contain additional arrays nested arbitrarily deep, in which case the minimum value for the nested array should be added to the total.
arr = [
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18],
]
# The expected output for the above input is:
# 8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
sum = 0
def array_min_sum(arr):
    global sum
    nums = []
    for elem in arr:
        if type(elem) is int:
            nums.append(elem)
        else:
            return sum + array_min_sum(elem)
    if len(nums) >= 1:
        return sum + min(nums)

print(array_min_sum(arr))