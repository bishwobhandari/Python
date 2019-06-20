try:
  new_file = open("sample.txt",'r')
  print(new_file.readlines(1))
  print(new_file.read(5))
  print(new_file.read(6))
except:
  print("file not found, please check your file path")

finally:
  print("This is the last call!")
  new_file.close()
print("Good Bye!!")

