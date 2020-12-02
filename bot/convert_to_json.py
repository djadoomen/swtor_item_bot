import json,re

save_file = open("Items.json","a")
filename = "FullItems.json"

with open(filename) as file:
    lines = file.readlines()
for line in lines:
    match = re.search(r"({.+})$",line)
    if match is not None:
        print(match.group())
        save_file.write(match.group()+'\n')
save_file.close()
