
class Pet():
#constructor with arugments
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = ''

#name method to return name
    def get_name(self):
        return self.__name
#name method to set the name
    def set_name(self, name):
        self.__name = name
#animal type to return type
    def get_animal_Type(self):
        return self.__animal_type
#animal type to set type
    def set_animal_Type(self, animal_Type):
        self.__animal_type = animal_Type
#age type to return age
    def get_age(self):
        return self.__age
#age type to set age
    def set_age(self, age):
        self.__age = age

# Creating the pet object
animal = Pet()
#Asking user for inputs
#name
pet_name= input('\nPlease enter the name : ')
animal.set_name(pet_name)
#type
#age

#print result