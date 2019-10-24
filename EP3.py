import re
def success(book):
    if type(book) != str:
        raise TypeError("Not a string")
    result = re.findall('at', book)
    for element in book:
        if len(element) >= 3:
            
