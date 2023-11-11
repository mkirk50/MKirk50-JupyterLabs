
class vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class automobile(vehicle):
    pass

    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Create list of valid options
dooroptions =[2,4]
roofoptions = ['Solid', 'Sun']

# Inputs and appropriate validations
var_vehicle = vehicle(input("Please enter vehicle type (car, truck, plane, boat, or a broomstick): "))
varyear = input('Please Enter Vehicle Year: ')
varmake = input('Please Enter Vehicle Make: ')
varmodel = input('Please Enter Vehicle Model:')


# This validates door numbers
vardoors = int(input('Please Enter Vehicle Number Of Doors (2 or 4):'))
while not vardoors in dooroptions:
    vardoors =int(input('Please Enter Vehicle Number Of Doors (2 or 4): '))


# This validates roof options

varroof = input('Please Enter Vehicle Roof Type(Solid or Sun):')
while not varroof in roofoptions:
    varroof = input('Please Enter Vehicle Roof Type(Solid or Sun): ')

# This sets values for the automobile class
var_automobile = automobile( varyear, varmake, varmodel, vardoors, varroof)

print('Vehicle Type: ' + var_vehicle.vehicle_type)
print('Year: ' + var_automobile.year)
print('Make: ' + var_automobile.make)
print('Model: ' + var_automobile.model)
print('Doors: ' + str(var_automobile.doors))
print('Roof: ' + var_automobile.roof)

