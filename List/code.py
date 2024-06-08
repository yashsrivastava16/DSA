# List in python.

# List is the collection of multiple items in a single variable.
# List are changeable meanning adding deleting can happen.
# List allows duplicate entries.

# e.g
myFruitList = ["apple","banana","cherry"]

# Accessing the elements.
print(myFruitList[0])

# Negetive indexing.
print(myFruitList[-1]) # -1 refers to the last element.

# Range of indexes
print(myFruitList[1:2])
print(myFruitList[:2])
print(myFruitList[1:])
print(myFruitList[-1:-2])

# Checking if item exists.

if "apple" in myFruitList:
    print("yes")
print("No")


# Chnaging the items value

myFruitList[1] = "orange"
myFruitList[0:1] = ["orange","grapes"]


# Adding items to list

myFruitList.append("cherry") # to end of the list
myFruitList.insert(1,"cherry") # to specific index

# appending new list
myLovableFruits = ["blueberry"]
myFruitList.extend(myLovableFruits)

# Removing items from list
myFruitList.remove("banana") # removes specified items it items appears more than 1 times it only remove the first occurrence
myFruitList.pop(1) # fom specifed index
myFruitList.pop() # if not specifed the index this will remove from last.

# del keyword also does the same task with index.

myFruitList.clear() # will clear the list



# Looping

for i in myFruitList:
    print(myFruitList[i])

for i in range(len(myFruitList)):
    print(myFruitList[i])

# List comprehension

newList = []
for x in myFruitList:
    if "b" in x:
        newList.append(x)

# Or we can go with shorter approach.

# for [x for x in myFruitList if "b" in x] 

# Sorting the list

myFruitList.sort() # will sort the list alphanumerically, ascending, by default:
myFruitList.sort(reverse = true) # To sort descending


# Copy list

mySelectedFruits = myFruitList.copy()
mySelectedFruits = list(myFruitList)

# Joining list

# with + operator or just use .extend function.



