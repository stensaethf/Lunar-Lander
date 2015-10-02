# interfaces.py
# A module containing two interfaces for the lunar lander game.
#
# Please mess around with this program, have fun with this game!
#
# by Andy Exley
# Edited by Frederik Roenn Stensaeth

# Import graphics and rectanglebutton
from graphics import *
from rectanglebutton import *


# Define TextLanderInterface class with no parameters. Functions as text
#interface for Lunar Lander game.
class TextLanderInterface:
    """Text-based interface for lander game."""


    # Define show_info method. Takes self and lander as parameters. Prints the
    # altitude, velocity, and fuel of the Lunar Lander
    def show_info(self, lander):
        
        print ("Lander Status: Altitude %d, Velocity %d, Fuel %d" % 
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel()))


    # Define get_thrust method. Takes self as parameter. Returns amount of
    #thrust
    def get_thrust(self):
        
        # Ask user for amount of thrust to be used
        amtstr = raw_input("Thrust amount?")
        # Return amount of thrust
        return int(amtstr)


    # Define show_crash method. Takes self as parameter. Prints a message.
    def show_crash(self):
       
        # Print string
        print "Crash! Oh noes!"


    # Define show_landing method. Takes self as parameter. Prints a message
    def show_landing(self):
        
        # Print string
        print "Hooray, the Eagle has landed!"


    # Define close method. Takes self as parameter. Prints message
    def close(self):
        
        # Print string
        print "Goodbye"


# Define GraphicLanderInterface. Takes self as parameter. Functions as graphics
#interface for Lunar Lander game.
class GraphicLanderInterface:
    """GraphicLanderInterface class is a graphical interface 
        for your lunar lander game"""


    # Define constructor. Takes self as parameter. Sets up graphics window,
    #graphics, and buttons
    def __init__(self):
        """Constructor that initializes the graphics window
        and shapes that we will use for drawing things"""

        # initialize window
        self.window = GraphWin("Lunar Lander Game", 300, 500)
        # transform coordinates
        self.window.setCoords(0, -30, 300, 600)

        # Call create_surface() method and store result
        figure1, figure2, figure3 = self.create_surface()
        self.surface_polygon1 = figure1
        self.surface_polygon2 = figure2
        self.surface_polygon3 = figure3
        # Draw polygons in graphics window
        self.surface_polygon1.draw(self.window)
        self.surface_polygon2.draw(self.window)
        self.surface_polygon3.draw(self.window)
        
        # Make button for thrust
        self.thrust = RectangleButton(Point(60, 525), 100, 75, 'Thrust')
        # Draw button
        self.thrust.draw(self.window)
        # Activate button
        self.thrust.activate()
        
        # Make button for no thrust
        self.no_thrust = RectangleButton(Point(240, 525), 100, 75, 'No Thrust')
        # Draw button
        self.no_thrust.draw(self.window)
        # Activate button
        self.no_thrust.activate()

        # Define lander_polygon and amounts
        self.lander_polygon = None
        self.amounts = None


    # Define show_info method. Takes self and lander as parameters. Updates
    #and draws lander polygon in correct space in graphics window, and updates
    #the altitude, velocity, and fuel counts displayed in graphics window
    def show_info(self, lander):
        """This method currently gets the lander info then draws it.
        That's it. It doesn't actually show any information."""
        
        # Get and store altitude of lander
        alt = lander.get_altitude()
        # if amounts is drawn, undraw it
        if self.amounts:
            self.amounts.undraw()
        # Store result of info method
        self.amounts = self.info(lander)
        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        # Create polygon and store as lander polygon
        self.lander_polygon = Polygon(Point(self.window.width / 2 - 10, alt),
                Point(self.window.width / 2 - 3, alt + 10),
                Point(self.window.width / 2 - 8, alt + 50),
                Point(self.window.width / 2 - 8, alt + 80),
                Point(self.window.width / 2, alt + 100),
                Point(self.window.width / 2 + 8, alt + 80),
                Point(self.window.width / 2 + 8, alt + 50),
                Point(self.window.width / 2 + 3, alt + 10),
                Point(self.window.width / 2 + 10, alt))
        # Fill lander polygon with darkgrey color
        self.lander_polygon.setFill("darkgrey")
        # Draw lander polygon and amounts
        self.lander_polygon.draw(self.window)
        self.amounts.draw(self.window)
    
    
    # Define info method. Takes self and lander as parameters. Gets information
    #about lander and returns information as a text object. Also checks if
    #lander has more fuel left and deactivates thrust button if fuel is empty
    def info(self, lander):
    
        # Get altitude, velocity, and fuel of lander
        alt =  lander.get_altitude()
        vel = lander.get_velocity()
        fuel = lander.get_fuel()
        # Store alt, vel, and fuel in a string
        information = ('Altitude: %d, Velocity: %d, Fuel: %d' % 
                      (alt, vel, fuel))
        # If lander has no more fuel deactivate thrust button
        if lander.get_fuel() == 0:
            self.thrust.deactivate()
        # Make text object centered at point (150, 450) with text being
        #information about lander
        x = Text(Point(150, 450), information)
        # Return x
        return x

    
    # Define get_thrust method. Takes self as parameter. Waits for user to
    #click a button and acts accordingly
    def get_thrust(self):
        """This method waits for a user's mouse click then returns 0 or 1
            thrust amount depending on whether the user clicked the Thrust
            button or No Thrust button."""
        
        # While loop to loop forever until user clicks a button
        while True:
            # Store mouse click point
            x = self.window.getMouse()
            # If thrust button was clicked return 1
            if self.thrust.clicked(x):
                return 1
            # If no thrust button was clicked return 0
            elif self.no_thrust.clicked(x):
                return 0


    # Define show_crash method. Takes self as parameter. Makes mushroom
    # explosion and displays a message
    def show_crash(self):
        """Crash message"""
        
        # Make mushroom explosion
        oval = Oval(Point(self.window.width / 2 - 70, 175),
                   Point(self.window.width / 2 + 70, 125))
        oval2 = Oval(Point(self.window.width / 2 - 100, 210), 
                   Point(self.window.width / 2 + 100, 95))
        polygon = Polygon(Point(self.window.width / 2 - 20, 0),
                      Point(self.window.width / 2 - 40, 150),
                      Point(self.window.width / 2 + 40, 150),
                      Point(self.window.width / 2 + 20, 0))
        # Fill mushroom explosion with red and orange color
        oval.setFill('Orange')
        oval2.setFill('Red')
        polygon.setFill('Orange')
        oval.setOutline('Red')
        oval2.setOutline('Orange')
        polygon.setOutline('Orange')
        # Draw mushroom explosion
        oval2.draw(self.window)
        oval.draw(self.window)
        polygon.draw(self.window)
        
        # Create text objects with message
        x = Text(Point(150, 300), "Crash! Oh noes!")
        y = Text(Point(150, 270), '(Click to quit)')
        # Set font size of text object to 20
        x.setSize(20)
        # Draw text objects
        x.draw(self.window)
        y.draw(self.window)


    # Define show_landing method. Takes self as parameter. Displays message
    def show_landing(self):
        """Landing message"""
        
        # Create text objects with message
        x = Text(Point(150, 300), "Hooray, the Eagle has landed!")
        y = Text(Point(150, 270), '(Click to quit)')
        # Set font size of text object to 20
        x.setSize(20)
        # Draw text objects
        x.draw(self.window)
        y.draw(self.window)


    # Define close method. Takes self as parameter. Closes window
    def close(self):
        
        # Wait for mouse click before closing graphics window
        self.window.getMouse()
        self.window.close()


    # Define create_surface method. Takes self as parameter. Creartes moon
    #surface
    def create_surface(self):
        """Draws the surface of the moon"""
        
        # Create figure to be moon surface, make it grey, and draw it
        oval = Oval(Point(-20,0),Point(320,-100))
        oval.setFill("gray")
        oval.setOutline('grey')
        # Create polygon figure to be moon crater, make it grey, and draw it
        crater = Polygon(Point(self.window.width / 4 - 30, -15),
                     Point(self.window.width / 4 - 15, 10),
                     Point(self.window.width / 4, 5),
                     Point(self.window.width / 4 + 15, 10),
                     Point(self.window.width / 4 + 30, -15))
        crater.setFill('grey')
        crater.setOutline('grey')
        # Clone moon crater and move clone
        crater2 = crater.clone()
        crater2.move((self.window.width / 4) * 2, 0)
        # Return figures that make up moon surface
        return oval, crater, crater2
        
        
    # Define score method. Takes self and lander as parameters. Calculates
    #score and displays it
    def score(self, lander):
        
        # Get fuel and velocity of lander and store values
        fuel = lander.get_fuel()
        velocity = lander.get_velocity()
        # If velocity is less than -10 set score to be 0
        if velocity < -10:
            score = 'Score: 0'
        # If velocity is greater than -10 calculate score
        else:
            points = fuel + velocity / 2
            score = ('Score: %d' % points)
        # Make text object with score as text
        x = Text(Point(150, 225), score)
        # Set font size of text object to 16
        x.setSize(16)
        # Draw text ojbect
        x.draw(self.window)
