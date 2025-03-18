# Create an empty list
my_list = []
print("Empty list:", my_list)

# Append the following to the list(10, 20, 30, 40)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Appended list:", my_list)

# Insert the value 15 at the second position
my_list.insert(1, 15)
print("New list:", my_list)

# Extend the list with another list[50, 60, 70]
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print("Updated list:", my_list)

# Remove the last element
my_list.pop()
print("Removed last element of list:", my_list)

# Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Print final list
print("Final list:", my_list)