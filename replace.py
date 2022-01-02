def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, "w") as f:
        print(
            'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        )
        s = s.replace(old_string, new_string)
        f.write(s)


# import required module
import os

# assign directory
directory = input("directory [ignore if file is in current directory]: ")

if directory == "":
    directory = os.path.dirname(os.path.realpath(__file__))
# iterate over files in
# that directory
old_string = input("old string: ")
new_string = input("new string: ")

for filename in os.scandir(directory):
    if filename.is_file():
        inplace_change(filename.path, f"{old_string}", f"{new_string}")
