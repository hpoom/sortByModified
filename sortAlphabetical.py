from os import walk

filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file

# printing the list using loop
for currentfile in range(len(filenames)):
    print filenames[currentfile],
