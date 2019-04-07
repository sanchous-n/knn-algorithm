import statistics


class Flower:

    def __init__(self, coord, name):
        self.coord = coord
        self.name = name

    def checkAssumption(self, kList):
        try:
            tName = statistics.mode(kList)
        except statistics.StatisticsError:
            return 0
        a = self.name == tName
        print(f"Assumption: {tName}; Actual name: {self.name}; {a}")
        return a
