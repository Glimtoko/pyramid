class Pyramid():
    def __init__(self, initial):
        self.data = [[initial]]

    def __repr__(self):
        result = ""
        for entry in reversed(self.data):
            result += str(entry) + "\n"
        result += "\n"
        return result

    def add(self, value):
        # First, add value to bottom level of pyramid
        self.data[0].append(value)

        # Now extend pyramid
        for i in range(len(self.data)):
            v1 = self.data[i][-1]
            v2 = self.data[i][-2]

            try:
                self.data[i + 1].append(v1 + v2)
            except IndexError:
                self.data.append([v1 + v2])
