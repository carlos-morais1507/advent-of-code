input = open('mini-input.txt', 'r').readlines()

line = input[0]

number = []
numbers = []

for i in range(len(line)):
    if line[i] != ".":
        print(line[i])


