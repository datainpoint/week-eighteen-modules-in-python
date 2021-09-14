class SimpleCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "a: {}, b: {}".format(self.a, self.b)
    def add(self):
        return self.a + self.b