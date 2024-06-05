def getcal(x):
    num_list = []
    word = list(x)
    for letter in word:
        if letter.isnumeric():
            num_list.append(int(letter))
    number = [num_list[0], num_list[len(num_list) - 1]]
    return int("".join(map(str, number)))


text_file = open("input.txt", "r")
cal_list = text_file.readlines()

cal_sum = 0

for cal in cal_list:
    x = getcal(cal)
    cal_sum = cal_sum + x

print(cal_sum)
