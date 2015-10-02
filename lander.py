# lander.py
# Python module to play Lunar Lander game
# Created by Frederik Roenn Stensaeth
# 02.28.14

# Import interface class
from interfaces import *


# Define LunarLander class. Takes self, alt, vel, and fuel as parameters.
#Keeps information about the lunar lander
class LunarLander:
    
    
    # Define constructor. Takes self, alt, vel, and fuel as parameters and
    #stores the values
    def __init__(self, alt, vel, fuel):
        
        # Store alt, vel, and fuel values
        self.altitude = alt
        self.velocity = vel
        self.fuel = fuel
       
        
    # Define get_altitude method. Takes self as parameter. Returns altitude
    #of self
    def get_altitude(self):
        
        # Return altitude of self
        return self.altitude
    
    
    # Define get_velocity method. Takes self as parameter. Returns velocity
    #of self
    def get_velocity(self):
        
        # Return velocity of self
        return self.velocity
        
    
    # Define get_fuel method. Takes self as parameter. Returns fuel of self
    def get_fuel(self):
        
        # Return fuel of self
        return self.fuel
    
    
    # Define update method. Takes self and thrustamount as parameters. Updates
    #fuel, velocity, and altitude of self, depending on thrustamount
    def update(self, thrustamount):
        
        # If thrustamount is less than or equal to fuel execute if body
        if thrustamount <= self.get_fuel():
            # Set fuel to be fuel minus fuel used
            self.fuel = self.get_fuel() - thrustamount
            # Calculate new velocity of self
            self.velocity = self.get_velocity() + 4 * thrustamount 
        # If thrustamount if larger than fuel amount execute else body
        else:
            # Calculate new velocity of self
            self.velocity = self.get_velocity() + 4 * self.get_fuel() 
        # Subtract two from velocity to account for gravity
        self.velocity = self.get_velocity() - 2
        # Calculate new altitude of self
        self.altitude = self.get_altitude() + self.get_velocity()
        # If altitude is less than 0, set altitude to 0
        if self.get_altitude() < 0:
            self.altitude = 0
    

# Define LunarGame class. Takes self and interface as parameters. Sets up
#lander and interface. Contians method for playing Lunar Lander game.
class LunarGame:
    
    
    #Define constructor. Takes self and interface as parameters. Creates lunar
    #lander object and sets up interface.
    def __init__(self, interface):
        
        # Create lunar lander object
        self.lander = LunarLander(200, 0, 30)
        # Set up interface
        self.interface = interface
    
    
    # Define play method. Takes self as parameter. Plays game
    def play(self):        
        
        # While loop to run as long as altitude of lander is greater than 0
        while self.lander.get_altitude() > 0:
            # Call show_info method of interface with lander object
            self.interface.show_info(self.lander)
            # Store result of get thrust method
            x = self.interface.get_thrust()
            # Update lander information considering thrust amount desired
            self.lander.update(x)
        # Set altitude of lander to 0
        self.lander.altitude = 0
        # Call show_info method of interface with lander object
        self.interface.show_info(self.lander)
        # If velocity of lander is less than -10 execute if body
        if self.lander.get_velocity() < -10:
            # Get score
            self.interface.score(self.lander)
            # Show crash
            self.interface.show_crash()
        # If velocity of lander is not less than -10 execute else body
        else:
            # Get score
            self.interface.score(self.lander)
            # Show landing
            self.interface.show_landing()


# Define main function. Takes no parameters. Creates interface, and a lunar
#lander game with that interface. Plays the game.
def main():
    
    
    # Create graphical interface
    c = GraphicLanderInterface()
    # Create lunar lander game with interface
    Apollo = LunarGame(c)
    # Play lunar lander game
    Apollo.play()
    # Close game
    c.close()
    

if __name__ == '__main__':
    main()