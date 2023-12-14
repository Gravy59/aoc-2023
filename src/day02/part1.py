# run in root dir!
with open("inputs/2", "r") as file:
    lines = file.readlines()

"""
Our problem appears simple: Given a data representation (represented below), we
need to isolate the lines where total cube amounts are <= the maximum allowed.

Our Data Representation:
Game <line>: <game 1>; <game 2>; <game 3>
<game> = <red>?, <green>?, <blue>?

This is really just a table:
| Game ID | Game 1 | Game 2 | Game 3 |
(maybe seperate the game 1 results to the total num of each cube)

Conclusion: I love and hate string manipulation.
"""

max_possible = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0
invalid_games = 100
for game in lines:
    # removing the game ID from the data
    game_id, game = game.split(": ")
    valid_game = True
    for subset in game.split("; "):
        for outcome in subset.split(", "):
            num_cubes, color = outcome.split()
            if int(num_cubes) > max_possible.get(color):
                valid_game = False
    if valid_game:
        total += int(game_id.split()[-1])
        invalid_games -= 1
    else:
        print(
            f"{game_id} has a subset that is greater than the max allowed for {color}"
        )

print(total)
print(invalid_games)
