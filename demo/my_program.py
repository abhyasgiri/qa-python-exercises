from my_first_module import divisible

num_one = int(input("Input the value for a: "))             #NB: we don't have to specify the variables as a and b as in the main function. Once they pass the main function (divide1), they pass as a and b
num_two = int(input("Input the value for b: "))

print("Answer: " + str(divisible.divisible(num_one, num_two))) 