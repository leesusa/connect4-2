import sys,json
import numpy as np
from ast import literal_eval

class data_reader:
    def __init__(self, width, height):
        self.grid = np.zeros((height,), dtype=int)
        self.width = width
        self.height = height

    def readGrid(self):
#        with open('test.json') as f:
#           data = f.readline()
        self.grid = np.zeros((self.height), dtype=int)
        data = sys.stdin.readline()
        sys.stderr.write(data + "\n")
        sys.stderr.flush()

        data = literal_eval(data)

        #data = json.load(data)
        for column in data['grid']:
            g = np.asarray(column)
            self.grid = np.column_stack((self.grid, g))

        self.grid = np.delete(self.grid, 0,axis=1)

        return self.grid