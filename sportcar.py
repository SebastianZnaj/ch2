from car import Car


class SportCar(Car):

    def __init__(self, size=1, company, model, color, max_speed):
        super().__init__(size, company, model, color)
        self.max_speed = max_speed

    def display_info(self):
        return "It's a {} {} {} {}, from {}".format(self.color, self.company, self.model, self.max_speed, self.year)
