"""
Demonstration #2

Given a non-empty array of integers `nums`, 
every element appears twice except except for one. 
Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10

todo:
- find the num that only appears once in the array
- return that num


whenever you're trying to find an item in an array,
you can rest assured that you need to look at every element in the arr [loop]

U: return the num that only appears once
P: look at each item | are there duplicates of this item? | count() can check for duplicates | 
E: do the brute force | improve after initial solving
R: evaluate the runtime analysis & improve your code - will always be asked this in an interview
"""

def single_number(nums):
    # #Method 1: runtime O(n^2)
    #loop over each item
    for num in nums: # O(n)
        #count the item
        count = nums.count(num) # O(n)
        # check if there are duplicates
        if count > 1: # all these are O(1)
            continue
        else:
            return num

    #method 2: O(n) [improved by using a dict]
    count_dict = {} # O(1)
    for num in nums: # O(n)
        # if new num, add to dict
        if num not in count_dict: # O(1) all the if statement
            count_dict[num] = 1
         #else, increase the count
        else:
            count_dict[num] += 1
    
    for num in nums: # O(n)
        if count_dict[num] == 1: # O(1)
            return num


print(single_number([3,3,2]))
print(single_number([5,2,3,2,3]))

'''
Dictionary

- has with key, value pairs
- also known as hashes, objects, hashmaps, hash tables
- dictionaries are very efficient at finding values since you can look things up by their key
- this has a runtime of O(1)

phonebook = {
    'Kadie': 234,
    "Danny': 789
}
'''