my_list = ['atagwhdakdehfehfekfhefoefho']

# How many elements each
# list should have
n = 4

# using list comprehension
final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n)]
print(final)