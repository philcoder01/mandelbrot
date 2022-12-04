from ColorPalette import ColorPalette
from PpmGenerator import ColorCode
import pytest

def test_read_value_from_palette_txt():
    # GIVEN the ColorPalette Object
    palette = ColorPalette("src/test_files/test_palette.txt")
    
    # WHEN checking the RgbValue for a specific iteration count
    rgbValue : ColorCode = palette.findRgbValue(28)
    
    # THEN the correct RgbValue should return
    assert rgbValue.r == 255
    assert rgbValue.g == 255
    assert rgbValue.b == 51
    
def test_read_value_from_palette_txt_with_unordered_upperlimit():
    # GIVEN the ColorPalette Object
    palette = ColorPalette("src/test_files/test_palette.txt")
    
    # WHEN checking the RgbValue for a specific iteration count
    rgbValue : ColorCode = palette.findRgbValue(28)
    
    # THEN the correct RgbValue should return
    assert rgbValue.r == 255
    assert rgbValue.g == 255
    assert rgbValue.b == 51

def test_for_exception_when_reading_faulty_format_palette_txt():
    # GIVEN the ColorPalette Object WHEN reading a faulty palette file
    with pytest.raises(Exception) as exception_info:
        palette = ColorPalette("src/test_files/test_palette_faulty_format.txt")
    
    # THEN an exception should be thrown
    print(str(exception_info.value))
    assert str(exception_info.value) == 'Error in ColorPalette definition file : "src/test_files/test_palette_faulty_format.txt"'

def test_for_exception_if_colorvalue_is_greater_than_eightbit():
    # GIVEN the ColorPalette Object WHEN reading a faulty palette file
    with pytest.raises(Exception) as exception_info:
        palette = ColorPalette("src/test_files/test_palette_greater.txt")
    
    # THEN an exception should be thrown
    print(str(exception_info.value))
    assert str(exception_info.value) == 'Error in ColorPalette definition file : "src/test_files/test_palette_greater.txt"'

def test_for_exception_when_colorvalue_or_upperLimit_is_negative():
    # GIVEN the ColorPalette Object WHEN reading a faulty palette file
    with pytest.raises(Exception) as exception_info:
        palette = ColorPalette("src/test_files/test_palette_neg_value.txt")
    
    # THEN an exception should be thrown
    print(str(exception_info.value))
    assert str(exception_info.value) == 'Error in ColorPalette definition file : "src/test_files/test_palette_neg_value.txt"'
