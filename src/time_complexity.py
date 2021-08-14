'''
algos with the number of steps are more efficient
teh size of the input is also important when considering the efficiency of an algo
will the algo hold up at 10, 20, and 100 input . . .
the input dictates the amount of steps we need when building an algo

'''

# constant time - regardless of the input, the num of steps doesnt change
# best algo for performance
# O(1)
def print_first(items):
    print(items[0])

#constant time O(1) - num of steps dont change that much
def print_first(items):
    print(items[0])
    print(items[0])
    print(items[0])
    print(items[0])
    print(items[0])

# Linear time - O(n)
# as the input increases, the steps increase - there are n steps if you through n items at us
def print_all_items(items):
  for item in items:
    print(item)
    print(item)

#Quadratic time - O(n^2) has a curved shaped and has bad performance
# polynomial time - O(n^2)
def print_pairs(items):
    for item1 in items:
        for item2 in items:
            print(item1, item2)

# arr = ['a', 'e', 'i', 'o', 'u']
# print_pairs(arr)
# with 5 items, this will run 25 times

'''
How to figure out runtime
- go line by line
- for each line, analyze its runtime
- add each runtime together
- if you find a loop:
  1. go line by line inside the loop and figure out the runtime for each line
  2. add up all runtimes inside the loop
  3. multiply the sum of all runtimes by the runtime of the loop itself O.o
'''
def do_some_stuff(items):
  print(items[0]) # O(1) constant

  print("hello world") # O(1) constant

  print(2 + 2) # O(1) constant

  # print all items
  for item in items:
    print(item) # O(n) linear


# nested loops are not always quadratic
# this is a constant loop - will only run 100 times
def constant_loop():
  for item in range(10):
    for item2 in range(10):
      print(item, item2)
