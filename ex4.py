# gives "cars" variable a certain value
cars = 100
# gives variable "space_in_a_car" a certain value
space_in_a_car = 4
# gives variable "drivers" a certain value
drivers = 30
# gives variable "passengers" a certain value
passengers = 90
# sets equation for variable "cars_not_driven" to assign it a value
cars_not_driven = cars - drivers
# sets equation for variable "cars_driven" to assign it a value
cars_driven = drivers
# sets equation for variable "carpool_capacity" to assign it a value
carpool_capacity = cars_driven * space_in_a_car
# sets equation for variable "average_passengers_per_car" to assign it a value
average_passengers_per_car = passengers / cars_driven


# prints phrases in the quotation marks and the number value of each variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "people today."
print "We need to put about", average_passengers_per_car, "in each car."
