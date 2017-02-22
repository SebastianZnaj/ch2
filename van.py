from car import Car


class Van(Car):

    def __init__(self, size=2, company, model, color, max_space):
        super().__init__(size, company, model, color)
        self.max_space = max_space

    def display_info(self):
        return "It's a {} {} {} {}, from {}".format(self.color, self.company, self.model, self.max_space, self.year)
