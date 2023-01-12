import os
import re

folder_path = '/home/alzywelzy/Documents/hentai/s/'

# Get a list of all the folders in the specified directory
folders = [f for f in os.listdir(folder_path) if os.path.isdir(
    os.path.join(folder_path, f))]

# Use a regular expression to extract numbers from the folder names
numbers = []
for folder in folders:
    match = re.search(r'\[(\d+)\]', folder)
    if match:
        numbers.append(int(match.group(1)))

# print(numbers)

for number in numbers:
    with open("saucy.txt", "a") as f:
        # f.write(str(number)+"\n")
        # f.write(f'{number} [nhentai.net/g/{number}] \n')
        f.write(f'https://nhentai.net/g/{number} \n')
