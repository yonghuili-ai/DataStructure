# Input
# {
#     "name": "test",
#     "email": "test.gmail.com",
#     "number_of_reports": "3",
#     "employments": [
#         {"title": "nuclear engineer",
#          "is_current": "False"},
#         {"title": "mechanical engineer",
#          "is_current": "True"}
#     ],
#     "bonus": {
#         "amount":"1000",
#         "cadence":"yearly"
#     },
#     "is_full_time":"True"
# }

# Output
# Object
# --- name: String
# --- email: String
# --- number_of_reports: Number
# --- employments: Array
# ------ Object
# --------- title: String
# --------- is_current: Boolean
# --- bonus: Object
# ------ amount: Number
# ------ cadence: String
# --- is_full_time: Boolean


# Input:
# ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Output:
# Array
# --- String

# python
def get_type(value) -> str:
    if isinstance(value, list):
        return "Array"
    elif isinstance(value, dict):
        return "Object"
    elif isinstance(value, bool):
        return "Boolean"
    elif isinstance(value, (int, float)):
        return "Number"
    elif isinstance(value, str):
        return "String"

# check the element type inside "Array" type
def check_ele_in_arr(prefix, ele):
    # if element is "Array", recursive call this function
    # Since it is one level down from array, need to add '---' additional to prefix
    if get_type(ele) == "Array":
        check_ele_in_arr(prefix+'---', ele[0])
    # if element is "Object", call check_in_object function 
    # Since it is one level down from array, need to add '---' additional to prefix
    elif get_type(ele) == "Object":
        print(f'{prefix} Object')
        for level_down_k, level_down_v in ele.items():
            check_in_object(prefix+'---', level_down_k,level_down_v) 
    # if element is other three types, no need to check deeper, print out directly. 
    elif get_type(ele) in ("Boolean","Number","String"):
        print(f'{prefix} {get_type(ele)}')

        
# check the value type in "Object" type
def check_in_object(prefix, k,v):
    # if element is other three types, no need to check deeper, print out directly. 
    if get_type(v) in ("Boolean","Number","String"):
        print(f"{prefix}{k}: {get_type(v)}")
    # if element is "Object", call check_in_object function to recursively unpack nested object
    elif get_type(v) == "Object":
        print(f"{prefix}{k}: Object")
        for level_down_k, level_down_v in v.items():
            # one level down, add --- for indentation
            check_in_object(prefix+'---',level_down_k,level_down_v) 
    elif get_type(v) == "Array":
        print(f"{prefix}{k}: Array")
        # one level down, add --- for indentation
        check_ele_in_arr(prefix+'---', v[0])


def initial_check(input):
    if get_type(input) == "Array":
        print("Array")
        check_ele_in_arr('---',input[0])
        return "Array"
    elif get_type(input) == "Object":
        print("Object")
        for k, v in input.items():
            check_in_object('---',k,v)
        return "Object"



input_1 = {
    "name": "test",
    "email": "test.gmail.com",
    "number_of_reports": 3,
    "employments": [
        {"title": "nuclear engineer",
         "is_current": False},
        {"title": "mechanical engineer",
         "is_current": True}
    ],
    "bonus": {
        "amount":"1000",
        "cadence":"yearly"
    },
    "is_full_time":True
}
initial_check(input_1)
print('\n')


input_2 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

initial_check(input_2)
print('\n')


input_3 = {
    "name": "test",
    "email": "test.gmail.com",
    "number_of_reports": 3,
    "employments": [
        {"title": "nuclear engineer",
         "is_current": False},
        {"title": "mechanical engineer",
         "is_current":True}
    ],
    "background":[
        {"clearance": True,
         "states": ["IA", "PA", "OH"]}
    ],
    "bonus": {
        "amount":"1000",
        "cadence":"yearly"
    },
    "is_full_time":True
}

initial_check(input_3)
print('\n')