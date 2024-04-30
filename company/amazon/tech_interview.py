# List of dictionaires, can use all built-in module
# [{id:,name:,amount:,}]
# 1. Print the dictionairy with the maximum amount
# 2. Ouput all t‍‌‌‍‍‍‌‍‌‌‍‍‍‌‌‍‍‌‍he list to a tab delimited file.
# 3. Convert the list to json file

example = [{'id':1, 'name':'round1', 'amount': 100},{'id':2, 'name':'round2', 'amount': 200},{'id':3, 'name':'round3', 'amount': 300}]
def print_largest_amount(example):
    max_amount = -float("inf")
    # res = {}
    for h in example:
        if h['amount'] > max_amount:
            res = h
            max_amount = h['amount']
    print(res)

import os 
def write_file(example):
    file_name = 'tab_delimited.txt'
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__) # remember this!
    file_name = os.path.join(current_directory, file_name)
    with open(file_name,'w') as file:
        header = '\t'.join(example[0].keys()) +'\n' 
        file.write(header) # remember file.write(context)

        for i in example:
            body =[str(x) for x in i.values()]
            body = '\t'.join(body) + '\n'
            file.write(body)

import json 
def convert_json(example):
    file_name = 'convert_json.json'
    current_dir = os.path.dirname(__file__)
    file_name = os.path.join(current_dir, file_name)
    with open(file_name, 'w') as file:
        # file.write(example)
        json.dump(example, file) # remember json.dump(data, file)

print_largest_amount(example)
write_file(example)
convert_json(example)
