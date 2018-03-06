from TriangleError import TriangleError

class Triangle:
    def __init__(self, color = "green", filled = True, \
                    side1 = 1, side2 = 1, side3 = 1):

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

        try:
            if side1 + side2 <= side3 or side1 + side3 <= side2 \
               or side2 + side3 <= side1:
                raise TriangleError(side1, side2, side3)   
        finally:
            self.__color = color
            self.__filled = filled
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        set.__filled = filled

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3)/2.0
        return math.sqrt(s*(s - self.side1)*(s - self.side2) \
            *(s - self.side3))

    def getPerimeter(self):
        return (self.side1 + self.side2 + self.side3)

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + \
            + " side2 = " + str(self.__side2) \
            + " side3 = " + str(self.__side3)
