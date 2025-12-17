import math 
print("pi:",math.pi)
print("Euler's number:",math.e)
print("Square root of 16:",math.sqrt(16))
print("sin(pi/2):",math.sin(math.pi/2))
print("cos(0):",math.cos(0))
print("Natural log of 10:",math.log(10))
print("log base 10 of 100:",math.log10(1000))
print("factorial of 5:",math.factorial(5))

#code for OS module
import os
print("current Directory:",os.getcwd())
print("Directory contents:",os.listdir())

dir_name = "test_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")
else:
    print(f"Directory '{dir_name}' to '{new_name}'.")

new_name = "renamed_folder"
if os.path.exists(dir_name):
    os.rename(dir_name, new_name)
    print(f"Renamed '{dir_name}' to '{new_name}'.")

if os.path.exists(new_name):
    os.rmdir(new_name)
    print(f"Directory '{new_name}' removed.")
    


