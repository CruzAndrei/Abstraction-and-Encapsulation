
class Car(object):
# Constructor, takes arguments and constructs the class
    def __init__(self, year, make):
        self.__year_model = year    
        self.__make = make    
        self.__speed = 0      
#Accelerate method
    def accelerate(self):
    #Accelerate by 5"
        self.__speed += 5
#Brake method
    def brake(self):
        #Decelerate by 5
        self.__speed -= 5
#get_speed method
    def get_speed(self):
        #current speed of the car
        return self.__speed


#car method
# create a Car object
# calls the accelerate method

# calls the brake method five times.
