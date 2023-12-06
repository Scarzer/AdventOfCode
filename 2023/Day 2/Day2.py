valid_blocks = {"red": 12, "green": 13, "blue": 14}

games = {}

class CubeGame():
    game_number = -1

    def __init__(self, game_string: str):
        game_split = game_string.split(":")
        self.game_number = game_split[0].removeprefix("Game ")
        self.rounds = {} 

        for round_num, round in enumerate(game_split[1].split(";")):
            self.rounds[round_num] = {}
            for color in round.split(","):
                self.block_color = color.split()[1]
                self.rounds[round_num][self.block_color] = color.split()[0]

        self.min_blue = self.getMinOfColor("blue")
        self.min_green = self.getMinOfColor("green")
        self.min_red = self.getMinOfColor("red")
    
    def isPossible(self) -> bool:
        possible = True
        for round in self.rounds:
            for color in self.rounds[round]:
                if int(self.rounds[round][color]) > valid_blocks[color]:
                    possible = False

        return possible

    def getMinOfColor(self, color: str) -> int:
        vals = []
        for r in self.rounds:
            if self.rounds[r].get(color) is not None:
                vals.append(int(self.rounds[r][color]))
        return max(vals)

    def getPower(self) -> int:
        return self.min_blue * self.min_green * self.min_red


    def __repr__(self) -> str:
        return f"Game #{self.game_number} - Power {self.getPower()} - {self.min_red} {self.min_green} {self.min_blue}\n"
        


def parseGameLine(game_string: str):
    game_split = game_string.split(":")
    game_number = game_split[0].removeprefix("Game ")
    
    for round in game_split[1].split(";"):
        for color in round.split(","):
            count = color.split()[0]
            block_color = color.split()[1]
            # print(f"Game #{game_number} - {block_color} has {count}")
            if int(count) > valid_blocks[block_color]:
                print(f"Game {game_number} is invalid")
                return 0

    return int(game_number)

def part_1_main():
    game_ID_sum = 0
    # with open("/home/scarzer/Projects/AdventOfCode/2023/Day 2/test_input.txt") as test:
    with open("/home/scarzer/Projects/AdventOfCode/2023/Day 2/day2_input.txt") as test:
        for line in test.readlines():
            game_ID_sum += parseGameLine(line.replace("\n", ""))
    
    print(game_ID_sum)


def part_2_main():
    game_ID_sum = 0
    games = []
    # with open("/home/scarzer/Projects/AdventOfCode/2023/Day 2/test_input.txt") as test:
    with open("/home/scarzer/Projects/AdventOfCode/2023/Day 2/day2_input.txt") as test:
        for line in test.readlines():
            g = CubeGame(line)
            games.append(g)
            print(g)
    powers = [x.getPower() for x in games]
    print(sum(powers))

if __name__ == "__main__":
    # part_1_main()
    part_2_main()
