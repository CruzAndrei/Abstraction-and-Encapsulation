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
            return 
        else:
            return
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
#method for speed
#radius
#color
#on/off
