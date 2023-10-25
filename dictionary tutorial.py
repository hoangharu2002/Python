#sample dictionary
light_num = ["Light 1", "Light 2", "Light 3"]   #list of keys
light_color = ["Red", "Green", "Yellow"]    #list of value

expected_dict = {"Light 1": "Red", "Light 2": "Green", "Light 3": "Yellow"} #our expected dictionary

print(f"The number of lights are: {light_num}")
print(f"The colors of liogts are: {light_color}")
print(f"The expected dictionary: {expected_dict}")

print("\n")

                                    ### How to create a dictionary ###
## Using {} bracket
dic = {"One": 1, "Two": 2, "Three": 3}
print(dic, "# Using {} brackets")
## Using dict() function
# Declare parameters
dic = dict(One = 1, Two = 2, Three = 3)
print(dic, "# Declare parameters")
# Using another dictionary with dict()
dic1 = dict(dic)
print(dic1, "# Using another dic")
# Combine iterator with parameters
dic = dict([("One", 1), ("Two", 2)], Three=3)
print(dic, "# Using iterator (and parameters)")

print("\n")

                                ### How to get a single value in dictionary ###
# Using [] bracket
print("Light 1's color: ", expected_dict["Light 1"])

#Using get() method
print("Light 2's color: ", expected_dict.get("Light 2"))

print("\n")

                            ### How to create a dictionary from 2 lists in Python ###
# Naive method
light_dict = {}

for num in light_num:
    for color in light_color:
        light_dict[num] = color
        light_color.remove(color)
        break

print("The dict using naive method: " + str(light_dict))

# Dictionary comprehension method
light_color = ["Red", "Green", "Yellow"]
light_dict1 = {light_num[i]: light_color[i] for i in range(len(light_num))}

print("The dict using dictionary comprehension: " + str(light_dict1))
