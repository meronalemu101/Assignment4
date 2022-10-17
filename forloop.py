1)
name = ['M', 'E', 'R', 'O', 'N']

for letter in name:

    if letter == 'M':
        letter = 'M'
    elif letter == 'E':
        letter = 'E'
    elif letter == 'R':
        letter = 'R'
    elif letter == 'O':
        letter = 'O'
    elif letter == 'N':
        letter = 'N'
    print(letter)
#answer printed: 
M
E
R
O
N

2)
name = ['M', 'E', 'R', 'O', 'N']
i = ['0', '1', '2', '3']
for i in name:
    letter = name + i
    if letter == 'M':
        letter = 'M'
    elif letter == 'E':
        letter = 'E'
    elif letter == 'R':
        letter = 'R'
    elif letter == 'O':
        letter = 'O'
    elif letter == 'N':
        letter = 'N'
    print(letter)

3)
names = ["Amy"]
for letter in names:
    if letter == 'A':
        letter = 'A'
        print(names[0][0:])
    elif letter == 'm':
        letter = 'm'
        print(names[0][1:])
    elif letter == 'y':
        letter = 'y'
    print(letter[0][0:])
names = ["Rory"]
for letter in names:
    if letter == 'R':
        letter = 'R'
        print(names[0][0])
    elif letter == 'o':
        letter = 'o'
        print(names[0][1])
    elif letter == 'r':
        letter = 'r'
        print(names[0][2])
    elif letter == 'y':
        letter = 'y'
    print(letter[0][0:])
names = ["River"]
for letter in names:
    if letter == 'R':
        letter = 'R'
        print(names[0][0])
    elif letter == 'i':
        letter = 'i'
        print(names[0][1])
    elif letter == 'v':
        letter = 'v'
        print(names[0][2])
    elif letter == 'e':
        letter = 'e'
        print(names[0][3])
    elif letter == 'r':
        letter = 'r'
    print(letter[0][0:])
#I was not able to get the full letters of each name only parts with index
