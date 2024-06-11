input_test = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

game_list = open("input.txt", "r").readlines()
counter = 0


def count_min(game):
    matches = game.split(": ")[1].split("; ")
    cred = cgreen = cblue = 0
    for i in range(len(matches)):
        match = matches[i].split()
        for term in range(len(match)):
            if "red" in match[term]:
                count = int(match[term - 1])
                if cred < count:
                    cred = count
            if "green" in match[term]:
                count = int(match[term - 1])
                if cgreen < count:
                    cgreen = count
            if "blue" in match[term]:
                count = int(match[term - 1])
                if cblue < count:
                    cblue = count

    return cred * cgreen * cblue


for game in game_list:
    counter += count_min(game)

print(counter)
