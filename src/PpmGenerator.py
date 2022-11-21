class PPM :
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.colorArray = [[None for x in range(width)] for y in range(height)]
    
    def setPixel(self, x, y, r, g ,b):
        if (x <= 0 or y <= 0) :
            raise IndexError("Pixel ({}, {}) not in range (1-{}, 1-{})".format(x, y, self.width, self.height))
        try:
            self.colorArray[x-1][y-1] = ColorCode(r, g, b)
        except IndexError:
            raise IndexError("Pixel ({}, {}) not in range (1-{}, 1-{})".format(x, y, self.width, self.height))
    
    def getImg(self) -> str:
        return self.createHeader() + "\n" + self.createPixels()
    
    def createHeader(self):
        return "P3 {} {} 255".format(self.width, self.height)
    
    def createPixels(self):
        output = ""
        for row in range(self.height):
            for col in range(self.width):
                currentPixelColor = self.colorArray[col][row]
                if (currentPixelColor is None) :
                    output += "0 0 0\n"
                else :
                    output += "{} {} {}\n".format(currentPixelColor.r, currentPixelColor.g, currentPixelColor.b)
        return output
    
class ColorCode:
    def __init__(self, r, g, b) -> None:
        self.r = r
        self.g = g
        self.b = b
        pass
