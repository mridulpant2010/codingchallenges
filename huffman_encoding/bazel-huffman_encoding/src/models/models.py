class InternalNodes:
    def __init__(self, weight, left, right) -> None:
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight


class LeafNodes:
    def __init__(self, char, weight):
        self.char = char
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
