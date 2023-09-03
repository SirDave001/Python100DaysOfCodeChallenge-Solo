class Journey:
    def __init__(self, *MovementList):
        self.travel = MovementList
    def RoundTrip(self):
        xPos, yPos = 0, 0
        for movement in self.travel:
            xPos += movement[0]
            yPos += movement[1]
        return xPos == 0 and yPos == 0
    
    
# movement in east and north directions
PeteItineray = [[90, 50], [-80, -40], [-10, -10]]
PeteJourney = Journey(*PeteItineray)
print(PeteJourney.RoundTrip())


StanItineray = [[50, 40], [-60, 10], [20, 70], [10, 30]]
StanJourney = Journey(*StanItineray)
print(StanJourney.RoundTrip())