class GameController:

    def start_game(self):
        print("Game started")


class Maze:

    def load_maze(self):
        print("Maze loaded")


class Light:

    def move(self):
        print("Light moving through the maze")


class Mirror:

    def reflect(self):
        print("Mirror reflecting the light")


class Goal:

    def check_goal(self):
        print("Checking if the light reached the goal")


# testing objects

game = GameController()
maze = Maze()
light = Light()
mirror = Mirror()
goal = Goal()

game.start_game()
maze.load_maze()

light.move()
mirror.reflect()

goal.check_goal()
