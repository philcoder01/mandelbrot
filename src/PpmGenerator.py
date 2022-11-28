from typing import TextIO

#Abstract class
class PPMConsumer:
    def write(content: str):
        raise NotImplementedError()

# actually saving into a file
class FilePPMConsumer(PPMConsumer):
    def __init__(self, path: str):
        self.file : TextIO = open(path, "w")

    def write(self, content: str):
        self.file.write(content)

    def close(self):
        self.file.close()

# test-implementation that offers content as string
class StringPPMConsumer(PPMConsumer):
    def __init__(self):
        self.content = ""

    def write(self, content: str):
        self.content += content

    def getContent(self)-> str:
        return self.content

# console print implementation
class ConsolePPMConsumer(PPMConsumer):
    def __init__(self, additionConsumer: PPMConsumer) -> None:
        self.addConsumer = additionConsumer
        
    def write(self, content: str):
        self.addConsumer.write(content)
        print(content)

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


    def getImg(self, file1: PPMConsumer):        
        self.createHeader(file1) 
        file1.write("\n")
        self.createPixels(file1)
        # Closing file

 
    def createHeader(self, file : PPMConsumer):
        file.write("P3 {} {} 255".format(self.width, self.height))

    
    def createPixels(self, file : PPMConsumer):
        output = ""
        for row in range(self.height):
            for col in range(self.width):
                currentPixelColor = self.colorArray[col][row]
                if (currentPixelColor is None) :
                   file.write("0 0 0\n")
                else :
                    file.write("{} {} {}\n".format(currentPixelColor.r, currentPixelColor.g, currentPixelColor.b))
    
class ColorCode:
    def __init__(self, r, g, b) -> None:
        self.r = r
        self.g = g
        self.b = b
        pass
