#fanspeed

#Fanspeed value

class Fan():
    SLOW = 1
    MEDIUM = 2
    FAST = 3

#Constructor
    def __init__(self ,on , radius ,speed, color): 
        #Fan description
        self.speed = speed         
        self.radius = radius         
        self.color = color         
        self.on = on          
    #String method
    def __str__(self): 
        if self.on == True:             
            return ("\n\t Fan Speed = " + self.get_Speed() + "\n\t Fan Radius = " + str(self.radius) + "\n\t Fan Color = " + self.color + "\n")         
        else:
            return ("\n\t Fan is off" + "\n\t Fan Radius = " + str(self.radius) + "\n\t Fan Color = " + self.color  + "\n")      
    #method   
    def get_Speed(self):   
        #showing the speed
        if self.speed == 1:             
            return "SLOW"         
        elif self.speed == 2:             
            return "MEDIUM"         
        elif self.speed == 3:             
            return "FAST"  
        #speed set
    def set_Speed(self,speed):         
        self.speed = speed  
    #radius
    def get_Radius(self):         
        return self.radius      
    def set_Radius(self,radius):         
        self.radius = radius 
    #color
    def get_Color(self):         
        return self.color      
    def set_Color(self,color):         
        self.color = color
#on/off
    def Set_ON(self):         
        self.on = True      
    def Set_OFF(self):         
        self.on = False      
    def get_ON(self):         
        return self.on  

Fan_1 = Fan(True, 10, 3, "Yellow")
Fan_2 = Fan(True , 5 , 2 , "Blue") 
Fan_3 = Fan(False, 5,2,"Blue")

print("\n FAN 1 :") 
print(Fan_1)
print("\n FAN 2 :") 
print(Fan_2)
print("\n FAN 2 : AFTER") 
print(Fan_3)
