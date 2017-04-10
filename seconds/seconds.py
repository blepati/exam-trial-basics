def seconds(long_list):
    short_list = []
    for item in range(2, len(long_list), 2):
        short_list.append(item)
    return short_list
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

print(seconds([1, 2, 3, 4, 5]))
