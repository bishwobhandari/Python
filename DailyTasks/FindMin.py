data_list = input("Please enter a list of numbers")
new_input = data_list.split()
int_data = [int(x) for x in new_input]
new_list = []

while int_data:
    minimum = int_data[0]  # arbitrary number in list 
    for x in int_data: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    int_data.remove(minimum)    

print(new_list[0])