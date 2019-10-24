import re
def success(book):
    if type(book) != str:
        raise TypeError("Not a string")
    result = re.findall('[A-Za-z]*at\\b', book)
    boxes = []
    for element in result:
        if len(element) > 3:
            boxes.append(element)
    return boxes
source = open('auntjo.txt')
jo = source.read()
print jo
