class Space:
    def __init__(self, num_coal, num_oil, num_garbage, num_uranium):
        self.coal = num_coal
        self.oil = num_oil
        self.garbage = num_garbage
        self.uranium = num_uranium

class Materials:
    def __init__(self):
        self.spaces = self.load_spaces()

    def load_spaces(self):
        spaces = {}
        [spaces.update({x:Space(3,3,3,1)}) for x in range(8)]
        [spaces.update({((x+6)*2):Space(0, 0, 0, 1)}) for x in range(4)]
        return spaces
