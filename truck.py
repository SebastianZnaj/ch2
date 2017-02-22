from car import Car


class Truck(Van):

    def __init__(self, size=3, company, model, color, max_space, wheel_count):
        self.wheel_count = wheel_count
        super().__init__(company, model, color, max_space)

    def display_info(self):
        return "It's a {} {} {} {} {}, from {}".format(self.color, self.company, self.model, self.max_speed, self.wheel_count, self.year)
