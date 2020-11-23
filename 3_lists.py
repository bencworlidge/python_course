my_list = ["Steve", "Barry", "Mary", "Jane", "Susie"]  # Same as JS
random_numbers = [49, 56, 43, 15, 56, 90, 56, 104]
print(my_list[3])  # Jane
print(my_list[-3])  # Mary
print(my_list[3:])  # Jane Susie
print(my_list[1:3])  # Barry Mary. Up to but not including 3rd index

my_list.extend(random_numbers)  # Adds list to another list
print(my_list)

random_numbers.append(3456)  # Adds item to list
print(random_numbers)

my_list.insert(3, "George")  # Adds item to list at given index
print(my_list)

my_list.remove("Steve")  # Removes item from list
print(my_list)

my_list.pop()  # Pops last element off list
print(my_list)

print(my_list.index("Jane"))  # Shows index of element

# Counts how many times the element is in the list
print(random_numbers.count(56))

random_numbers.sort()  # Orders list
print(random_numbers)

random_numbers.reverse()  # Reverses list
print(random_numbers)

second_list = my_list.copy()  # Copies list to new list
print(second_list)

my_list.clear()  # Clears list
print(my_list)
