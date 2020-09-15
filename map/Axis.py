class Axis:
    def __init__(self, value, data=None):
        self.value = value
        self.contained_values = []
        self.data = data

    def __float__(self):
        return float(self.value)

    def __gt__(self, other):
        return self.value > float(other)

    def __lt__(self, other):
        return self.value < float(other)

    def __eq__(self, other):
        return self.value == float(other)
