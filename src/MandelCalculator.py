
class MandelCalculator: 
    def __init__(self, x_start, x_delta, y_start, y_delta, max_iterations, infinity_limit) -> None:
        self.x_start = x_start
        self.x_delta = x_delta
        self.y_start = y_start
        self.y_delta = y_delta
        self.max_iterations = max_iterations
        self.infinity_limit = infinity_limit



    def getMandelValue(self, x :int, y :int) -> int:

        c = complex(x,y)
        zn = c
        i = 0
        # z1 = z0**2 + c
        # z2 = z1**2 + c
        while((i < self.max_iterations) and (abs(zn) < self.infinity_limit)):
            zn = zn**2 + c
            i = i + 1
        return i
        
        #<Number of iterations until mandelbrot formula goes to infinity>
