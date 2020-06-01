import re

def grepimitation(regex):
    try:
        myfile = open('mbox.txt', 'r')
    except FileNotFoundError:
        print(f'Your file could not be opened, sorry.')
        exit()
    
    linecount = 0
    for line in myfile:
        result = re.findall(regex, line)
        if len(result) > 0:
            linecount += 1
    
    return linecount

regex = input(f'Please enter a regular expression: ')
print(f'There are {grepimitation(regex)} lines that match your regular expression.')
