input_test = "Game 1: 1 green, 2 blue; 1 red, 2 blue, 3 green; 4 green, 3 red"

game_list = open("input.txt", "r").readlines()
counter = 0


def get_matches(game):
    matches = game.split(": ")[1]
    return matches.split("; ")


def validate_matches(game):
    matches = get_matches(game)
    cvalid = 0
    for match in range(len(matches)):
        cred = cblue = cgreen = 0
        words = matches[match].split()
        for i in range(len(words)):
            if "red" in words[i]:
                cred = int(words[i - 1])
            if "green" in words[i]:
                cgreen = int(words[i - 1])
            if "blue" in words[i]:
                cblue = int(words[i - 1])
        if cred <= 12 and cgreen <= 13 and cblue <= 14:
            cvalid += 1
    if cvalid == len(matches):
        return True
    else:
        return False


for game in range(len(game_list)):
    if validate_matches(game_list[game]):
        print(game + 1, ", Valid!")
        counter += game + 1
    else:
        print(game + 1, ", Not valid!")

print("Total: ", counter)
