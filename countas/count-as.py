def count_as(file_name):
    try:
        content_to_count = open(file_name)
        letters_to_count = content_to_count.read()
        num_of_as = 0
        content_to_count.close()

        for letter in letters_to_count.lower():
            if letter == "a":
                num_of_as += 1
        return num_of_as

    except FileNotFoundError:
            return 0

    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
