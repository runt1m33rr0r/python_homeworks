class Fibs(object):
    def __init__(self):
        self.last_number = 0
        self.prelast_number = 0

    def next(self):
        if self.prelast_number == 0 and self.last_number == 0:
            self.last_number = 1
            return 0
        
        result = self.last_number + self.prelast_number
        self.last_number = self.prelast_number
        self.prelast_number = result

        return result

    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f < 1000:
        print f
    else:
        break