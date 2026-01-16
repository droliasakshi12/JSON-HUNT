# WORKING OF THIS PROJECT
# created a json file name json_hunt.json
# then imported the json module to access or fetch the data
# created CLASS AND OBJECT AND CONSTRUCTOR
# the folder and file access is dynamic means you can access the file if it is in your folder and if it  is outside the folder then also you can access it
# created a constructor where it will ask for file and folder input and will provide you the data from the file
# then created a function so you can get the value for the key or key for any value
# in the search function you can randomly search for anything either key or value
# made the use of ISINSTANCE keyword which helps to know what is the instance of the obj or data
# in value_from_keys and get_keys_by_value function we have take the Arbitrary Positional Arguments (*args) which means that we can as many arguments we want.
# made the use of MATCH CASE statement for choices inputs by the user

import json
import time

class view_json_data():
    def __init__(self):  # constructor created to be called automatically when the class is called
        global folder_input
        global file_input
        global file_path
        folder_input = input("enter the folder you want to access:")
        file_input = input("enter the json file you want to access:")

        if folder_input:
            file_path = fr"{folder_input}\{file_input}"
        else:
            file_path = f"{file_input}"

# viewing data from json file
        try:
            with open(fr"{file_path}", 'r') as file:
                self.data = json.load(file)
                print(self.data)
        except Exception as e:
            print(f"error{e}")

 # getting the values from the keys

    def value_from_keys(self, *key):
        try:
            with open(fr"{file_path}", 'r') as file:
                self.data = json.load(file)
                data = self.data
                
            value = []
            
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for k in key:
                            if k in item:
                                value.append(item[k])
                print(value)

            if isinstance(data, dict):
                for k in key:
                    if k in data:
                        value.append(data[k])
                print(value)    

        except Exception as e:
            print(f"error {e}")

# getting the key from the values
    def get_keys_by_value(self, value_input):
        try:
            with open(fr"{file_path}", 'r') as file:
                self.data = json.load(file)
                data = self.data

            if value_input.isdigit():
                value_input = int(value_input)
            try:
                if isinstance(data, list):  # if it is stored in list
                    for i in data:
                        for key, val in i.items():
                            if val == value_input:
                                print(key)
            except Exception as e:
                print("value not found", e)

            try:
                if isinstance(data, dict):
                    for i, j in data.items():
                        for k, l in j.items():
                            if k == value_input:
                                print(i)
                            elif l == value_input:
                                print(k)

            except Exception as e:
                print(f"ERROR{e}")

        except Exception as e:
            print(f"error {e}")

# creating a search function where we can search both the key and values whatenver we want from the whole json file.

    def search(self, key_value_input):
        # first creating a find key function
        # here the concept of RECURSION is used where a function calls itself within its function execution
        def find_from_key(data, key):
            results = []
            if isinstance(data, dict):
                for x, y in data.items():
                    if x == key:
                        results.append(y)
                    results.extend(find_from_key(y, key))
            elif isinstance(data, list):
                for items in data:
                    results.extend(find_from_key(items, key))

            return results

        def find_from_value(data, value):
            key_list = []

            if isinstance(data, dict):
                for key, val in data.items():
                    if val == value:
                        key_list.append(key)

                    if isinstance(val, (dict, list)):
                        key_list.extend(find_from_value(val, value))

            elif isinstance(data, list):
                for item in data:
                    key_list.extend(find_from_value(item, value))

            return key_list

        # getting the data from the json hunt file
        with open(fr"{file_path}", 'r') as file:
            data = json.load(file)

        # checking if the data entered is integer then,
        if key_value_input.isdigit():
            key_value_input = int(key_value_input)

        find_value = find_from_key(data, key_value_input)
        if find_value:
            print(f"found the value for the key {key_value_input}")
            for v in find_value:
                print(v)

        find_key = find_from_value(data, key_value_input)
        if find_key:
            print(f"found key for the value {key_value_input}")
            for k in find_key:
                print(k)


# asking for choices
#created a repeating loop to run the program until the user dosen't wants to end
while True:
    n = int(input("enter 1 to continue and 0 to end:"))

    if n == 1:
        choice = int(input(
            "CHOOSE\n1.FIND VALUE FORM KEYS\n2.FIND KEY FROM VALUES\n3.TO SEARCH ANY VALUE FROM ANY WHERE\nENTER YOUR CHOICE HERE:"))

        obj = view_json_data()  # constructor is called itself!
        start_time = time.perf_counter()
        match choice:
            case 1:
                args = int(
                    input("enter the number of arguments you want to pass:"))
                for i in range(args):
                    keys = input(
                        "enter the keys for the values you want to access:")
                    obj.value_from_keys(keys)
            case 2:
                args = int(
                    input("enter the number of arguments you want to pass:"))
                for i in range(args):
                    value_input = input(
                        "enter the value for the key you want:")
                    obj.get_keys_by_value(value_input)
            case 3:
                inputs = input("enter the key or value you want to find:")
                obj.search(inputs)

            case _:
                print("INCORRECT CHOICE! CHOOSE FROM THE ABOVE LIST PROVIDED!")

        end_time = time.perf_counter()

    else:
        print("THANK YOU!!")
        total_time = end_time - start_time
        print("TOTAL TIME TAKEN:", total_time)
        break