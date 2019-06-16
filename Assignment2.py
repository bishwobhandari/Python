

# number 1
x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5 + 5j], 4000]

print(x[4][0:2])
print(x[4][6])
print(x[4][4][2:4])
print(x[4][3:6])

# number 2
print("Answer to number 3 ")
x = range(1, 21)

sum = 0
new_list = []
for i in x:
    sum += i
    if sum % 2 == 0:
        new_list.append(i)
print(new_list)
print("The sum is", sum)


# number 4
x = range(1, 50)
l = list()
for i in x:
    if i % 2 != 0:
        y = i ** 3
        if y in x:
            l.append(i)
print("Answer to number 4: ")
print(l)

# number 5
import copy
print("Answer to number 5: ")
original_list = list(range(1, 20))
print("original list is", original_list)

list_copy = copy.deepcopy(original_list)
new_list = [i*3 for i in list_copy]
print("new list is ", new_list)

# number 6

print("Answer to number 6: ")
user_input = input(" please enter a sentence ")
split_texts = user_input.split()

for i in split_texts:
    word_length = len(i)
    print(" the length of ", i, " is ", word_length)




# number 1
x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5 + 5j], 4000]

print(x[4][0:2])
print(x[4][6])
print(x[4][4][2:4])
print(x[4][3:6])

# number 2
print("Answer to number 3 ")
x = range(1, 21)

sum = 0
new_list = []
for i in x:
    sum += i
    if sum % 2 == 0:
        new_list.append(i)
print(new_list)
print("The sum is", sum)


# number 4
x = range(1, 50)
l = list()
for i in x:
    if i % 2 != 0:
        y = i ** 3
        if y in x:
            l.append(i)
print("Answer to number 4: ")
print(l)

# number 5
import copy
print("Answer to number 5: ")
original_list = list(range(1, 20))
print("original list is", original_list)

list_copy = copy.deepcopy(original_list)
new_list = [i*3 for i in list_copy]
print("new list is ", new_list)

# number 6

print("Answer to number 6: ")
user_input = input(" please enter a sentence ")
split_texts = user_input.split()

for i in split_texts:
    word_length = len(i)
    print(" the length of ", i, " is ", word_length)


