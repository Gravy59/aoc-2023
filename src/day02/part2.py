# run in root dir!
with open("inputs/2", "r") as file:
    lines = file.readlines()

# lines = [
#    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

total = 0
for game in lines:
    # removing the game ID from the data
    game_id, game = game.split(": ")
    min_cubes = {"red": 1, "green": 1, "blue": 1}
    for subset in game.split("; "):
        print(subset)
        for event in subset.split(","):
            num_cubes, color = event.split()
            if min_cubes[color] < int(num_cubes):
                min_cubes[color] = int(num_cubes)

    print(min_cubes)
    power = 1
    for value in min_cubes.values():
        power *= value

    print(power)
    total += power
    print("============")

print(total)
