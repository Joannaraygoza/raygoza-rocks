"""
#Looking for the most common word in a file
name = input('Enter file:')
handle = open(name, 'r')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
"""
"""
def computepay(hours, rate): #Computing pay with overtime, with error checking
    pay = hours * rate
    if hours > 40:
        pay += (hours-40) * rate/2
    return pay
try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    print(computepay(hours, rate))
except ValueError:
    print("Please enter a numerical value.")
"""
"""
def computegrade(score):
    try:
        score = float(score)
        if score > 1:
            return "Bad score"
        elif score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"
    except:
        return "Bad score"

score = input("Please enter a score between 0.0 and 1.0: ")
print(computegrade(score))
"""
"""
#Find max and min of inputted numbers
lst = []
while True:
    inp = input("Please enter a number, or 'done' when finished. ")
    if inp == 'done':
        break
    try:
        val = float(inp)
        lst.append(val)
    except ValueError:
        print("Invalid input")
print(f'Maximum: {max(lst)}; Minimum: {min(lst)}')
"""
"""
def count(string, letter):
    num_let = 0
    for let in string:
        if let == letter:
            num_let += 1
    return num_let
    
print(count("Hello World!", "o"))
"""
"""
#Counting the time distribution in when the emails were sent in the mbox files
filename = input("Please enter the file name: ")
try:
    file1 = open(filename, "r")
except FileNotFoundError:
    print(f'File cannot be opened: {filename}')
    exit()

count_dict = {}
for line in file1:
    if line.startswith("From"):
        words = line.split()
        if len(words) != 7: continue
        time = words[5]
        hour = (time.split(":"))[0] #Splitting time into its components and then grabbing the hour
        count_dict[hour] = count_dict.get(hour, 0) + 1
hour_counts = list(count_dict.items())
hoursorted = sorted(hour_counts)
for hour in hoursorted:
    print('{} {}'.format(*hour))
file1.close()
"""
"""
def chop(lst):
    del lst[0]
    del lst[-1]
    return None

mylst = [0, 1, 2, 3, 4, 5]
print(mylst)
chop(mylst)
print(f'Chopped list is {mylst}')
"""
"""
with open('romeo.txt', 'r') as romeo:
    word_list = []
    for line in romeo:
        words = line.split()
        for word in words:
            if word.rstrip() not in word_list:
                word_list.append(word)
    print(sorted(word_list))
"""
"""
#Sorting for the most frequent word in romeo. If there's a tie, reverse alphabetical sort.
import string
filename = input("Please enter the file name: ")
try:
    file1 = open(filename, "r")
except FileNotFoundError:
    print(f'File cannot be opened: {filename}')
    exit()

wordlist = {}
for line in file1:
    line = line.rstrip().lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        wordlist[word] = wordlist.get(word, 0) + 1

valfirst = []
for key, val in wordlist.items():
    valfirst.append((val, key))

valfirst.sort(reverse = True)
for item in valfirst[:10]:
    print(item[0], item[1])

file1.close()
"""
"""
#Learning about helper functions and decorators
import pdb
pdb.set_trace()
def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
    print(i, factorial(i))
"""
"""
#Coding problem: Find the highest square under 1000.
import math
def highest_square(maxsquare):
    if maxsquare < 0:
        raise Exception('Not currently set up to handle negative numbers.')
    toohigh = math.sqrt(maxsquare)
    desiredroot = math.floor(toohigh)
    return (desiredroot, desiredroot**2)
print("Root is {}, and its square is {}".format(*highest_square(-1)))
"""
"""
#Calling *args within a function
def hello(*args):
    for arg in args:
        print(f'Hello {arg}')
    return None

hello("Bob", 'Bill', 'Jane')
"""
"""
import string
let_counts = {}
def letterfrequency(chosenfile):
    try:
        myfile = open(chosenfile, 'r')
    except FileNotFoundError:
        print(f'File {chosenfile} cannot be opened, sorry.')
        exit()
    for line in myfile:
        line = line.lower()
        for letter in line:
            if letter.isalpha():
                let_counts[letter] = let_counts.get(letter, 0) + 1
    sortedlets = sorted(let_counts.items(), key=lambda x:x[1], reverse=True)
    myfile.close()
    return sortedlets
chosenfile = input("What is the name of the file "
                   "you'd like to inspect? ")
sortedlets = letterfrequency(chosenfile)
for item in sortedlets:
    print(*item)

#Using regex to find various data in the mbox files
import string
import re
def find_data(chosenfile):
    try:
        myfile = open(chosenfile, 'r')
    except FileNotFoundError:
        print(f'File {chosenfile} could not be opened, sorry.')
        exit()
        
    email_list = []
    dspam_nums = []
    rev_nums = []
    hours_sent = []
    numrevisions = 0
    revisiontotal = 0

    for line in myfile:
        #Regex expression: this one starts with any alphanumeric character, 
        #then a bunch of any characters, then an @ symbol, then some
        #other characters, then a period, and some more characters,
        #and finally ends with an alpha character.
        emails = re.findall(r'\w\S*@\S*\.\S*[a-zA-Z]', line)
        if len(emails) > 0:
            email_list.append(emails)
         
        #Now to find numbers on lines that start with X-DSPAM
        dspam_num = re.findall(r'X-DSPAM\S*: ([0-9.]+)', line)
        if len(dspam_num) > 0:
            dspam_nums.append(dspam_num)

        #And now to extract the revision numbers
        rev_num = re.findall(r'Details: .*rev=([0-9]+)', line)
        if len(rev_num) > 0:
            revisiontotal += int(rev_num[0])
            rev_nums.append(rev_num)
             
        #How about the hour the email was sent
        hour_sent = re.findall(r'From .* ([0-9][0-9]):', line)
        if len(hour_sent) > 0:
            hours_sent.append(hour_sent)

        #Number of lines of the format New Revision: (number)
        revision = re.findall(r'^New Revision: ([0-9]*)', line)
        if len(revision) > 0:
            numrevisions += 1

    print(revisiontotal, numrevisions)
    avg_revision = revisiontotal / numrevisions

    return email_list, dspam_nums, rev_nums, hours_sent, avg_revision
returndata = (find_data('mbox-short.txt'))
print(int(returndata[4]))
"""
"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
"""
"""
coor1 = [[0,0],[0,5],[5,5],[5,0]]


def checkStraightLine(coordinates):
    xdiff = coordinates[1][0] - coordinates[0][0]
    ydiff = coordinates[1][1] - coordinates[0][1]

    if xdiff != 0:
        slope = ydiff / xdiff
    else:
        slope = "infinity"
    #print(xdiff, ydiff, slope)

    prevcoordinate = coordinates[0]  # implementation with a for loop
    for coordinate in coordinates[1:]:
        thisxdiff = coordinate[0] - prevcoordinate[0]
        thisydiff = coordinate[1] - prevcoordinate[1]
        if slope == 'infinity':
            if thisxdiff == 0:
                prevcoordinate = coordinate
                continue
            else:
                return False
        elif slope != 'infinity':
            if thisxdiff == 0:
                return False
            else:
                if abs(thisydiff / thisxdiff - slope) > 0.01:
                    return False
        prevcoordinate = coordinate
    return True

print(checkStraightLine(coor1))
"""