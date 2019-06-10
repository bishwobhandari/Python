print('Hello My name is "Rishab". i love coding')
print(" This is 'My first program'. ")

x = input('please enter x value')
y = input('please enter y value ')
z = input('please enter z value ')

print(" User entered x = ", x, "," " y = ", y, "," " z = ", z)
print(' Output:  "value1 = ', x, "," " value2 = ", y, "," ' value3 = ', z, '"')
print(" The data type of  x is ", type(x), " y is ", type(y), " z is ", type(z))


#2 problem

print("Hello! My name is xyZ")
print(' "Hello I am a Candidate" ')
print(' "234.56" ')
print(' "34" ')
print(" a+3j ")

#3 problem

x = 10+20*(45+67.0)
print(type(x))

x = (True and False) or False
print(type(x))

x = (True or True) and (not False and True)
print(type(x))

x = (3>89) or (34>32)
print(type(x))

x = not True and False
print(type(x))


#4

x = int(input("pleas enter a numeric value "))
if x % 2 <= 0 and x % 5 <= 0:
    print("Hurray it is What i am looking for")
else:
    print("wrong  input")



#5
# not including 10 and 50 on both limits.

x = int(input("please enter a number "))
if 10 < x < 50:
    print("Yes i am in the range")
else:
    print("oops")





