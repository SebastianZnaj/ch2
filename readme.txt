garage(size, localization)
*AddCar(car)
*LoadCarsFromCsv(csv_file)
*SpaceLeft()
*DisplayCars()


sportcar (size = 1, company, moder, year, color, max_speed)

*DisplayInfo()
   return "It's a (color) (company) (model), from (year), max speed:xxx"

-----------------------------------------------------------------------------
van (size = 2, company, model, year, color, max_space)

*DisplayInfo()
   return "It's a (color) (company) (model), from (year), max space:xxx"

-----------------------------------------------------------------------------
truck (size = 3, company, model, year, color, max_space, wheel_count)

*DisplayInfo()
   return "It's a (wheel_count)-wheels (color) (company) (model), from (year), max space:xxx"
