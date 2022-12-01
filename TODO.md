# TODO

## ColorPallete
Create a class that provides the color-palette for the mandelViewer. The palette should read its
data from a file `palette.txt` that looks like this:
```
upperLimit, red, green, blue
```
so an example file looks like this:
```
1, 255, 102, 255
2, 0, 102, 204
3, 102, 178, 255
4, 0, 253, 253
5, 102, 204, 255
10, 102, 204, 0
30, 255, 255, 51
50, 255, 153, 51
70, 255, 102, 102
90, 255, 0, 0
999999, 0, 0, 0
```
- If the mandel-number of a pixel is 1, we get `[255, 102, 255]` as a color (because `0 < x <= 1` ).
- If the mandel-number of a pixel is 6,7,8,9 or 10, we get `[102, 204, 255]` as a color (`because 5 < x <= 10`).
- If the mandel-number of a pixel is 11, 12, 13 ... 29, 30, we get `[255, 255, 51]` as a color (`because 10 < x <= 30`).
- etc.

ℹ️ think about how to test this properly
ℹ️ take educated assumptions for missing specifications

## MandelViewer
Implement the Mandelviewer (the so called controller) which orchestrates the whole process.
- the controller first asks the `CliParser` to pares the user's input.
- then for every pixel according to the user's input
   - ... the MandelCalculator calculates the mandelbrot-value for that pixel
   - ... it grabs the r,g,b values for the given mandelbrot-value from the pallete
   - ... it sets the according pixel with the r,g,b
- finally it saves the file to a ppm-file
