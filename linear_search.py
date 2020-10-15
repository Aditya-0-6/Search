def get_input():
    array = []
    keepgoing = True
    while keepgoing:
        value = input("Enter a value (Exit to stop): ")
        if value == "Exit":
            keepgoing = False
        else:
            array.append(value)
    return array

def linear_search(array, search):
    for value in array:
        if value == search:
            return True
    return False

### Main ###
array = get_input()
search = input("Enter the value you want to search for: ")
if linear_search(array, search):
    print("Found")
else:
    print("Not Found")
