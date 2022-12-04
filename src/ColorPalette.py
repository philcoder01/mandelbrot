from PpmGenerator import ColorCode

class ColorPalette:
    def __init__(self, file) -> None:
        self.colorDict : dict = self.readFile(file)
        pass

    def readFile(self, file) -> dict:
        paletteDef = open(file, "r")
        
        lines = paletteDef.readlines()
        
        temp_dict : dict = {}
        
        for line in lines:
            line = line.replace('\n', '')
            row_value = line.split(", ")
            if (len(row_value) != 4):
                raise Exception('Error in ColorPalette definition file : "{}"'.format(file))
            elif (int(row_value[1]) > 255 or int(row_value[2]) > 255 or int(row_value[3]) > 255):
                raise Exception('Error in ColorPalette definition file : "{}"'.format(file))
            elif (int(row_value[0]) < 0 or int(row_value[1]) < 0 or int(row_value[2]) < 0 or int(row_value[3]) < 0):
                raise Exception('Error in ColorPalette definition file : "{}"'.format(file))
            temp_dict[int(row_value[0])] = ColorCode(int(row_value[1]), int(row_value[2]), int(row_value[3]))
        
        paletteDef.close()
        
        return dict(sorted(temp_dict.items()))


    def findRgbValue(self, iteration_number) -> ColorCode:
        for key, value in self.colorDict.items():
            if (iteration_number <= key):
                return self.colorDict[key]


    
