# file=open("input.txt","r")
# file2=open("output.txt","w")

# file2.write("hello world\n")  
# file2.write("hello world")  

# file2.close()  #alaways close korte hobe...

# var=file.read()
# var =file.readline()
# # print(var)
# var =file.readlines()
# print(var)
# temp =var.split("\n")
# print(temp[2])

# var2=file.read()
# print([var2])

# task 1 (a)

input_file = open("input.txt", 'r')
output_file = open("output.txt", 'w')

t = int(input_file.readline())

for i in range(t):
  n = int(input_file.readline())
  if n % 2 == 0:
    print(f"{n} is an Even number.", file = output_file)
  else:
    print(f"{n} is an Odd number.", file = output_file)

input_file.close()
output_file.close()
