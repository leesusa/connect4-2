import argparse, sys
import random
import json

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--player', type=int, help='an integer for the player number', default=1, nargs='?')
parser.add_argument('--height', type=int, help='an integer for the height of the grid', default=6, nargs='?')
parser.add_argument('--width', type=int, help='an integer for the width of the grid', default=7, nargs='?')

args = parser.parse_args()

player = args.__dict__["player"]
height = args.__dict__["height"]
width = args.__dict__["width"]

sys.stderr.write("player = " + str(player) + " ")
sys.stderr.write("width = " + str(width) + " ")
sys.stderr.write("height = " + str(height) + " ")

def main():

    while True:
        line = sys.stdin.readline()

        move = {}
        move['move'] = random.randint(0, 6)

        x = json.dumps(move)

        sys.stderr.write(x + "\n")

        sys.stdout.write(x + "\n")

        sys.stdout.flush()
        sys.stderr.flush()

main()