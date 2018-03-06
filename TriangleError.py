# creates TriangleError class to be thrown when the three sides of a
# Triangle object cannot form a triangle

class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        
    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3
