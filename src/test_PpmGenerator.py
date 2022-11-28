from PpmGenerator import PPM, StringPPMConsumer, ConsolePPMConsumer
import pytest

def test_generate_a_1_by_1_default_pixel_file() :
    # GIVEN a 1 by 1 ppm file
    ppm = PPM(1, 1)
    
    # WHEN we generate the Image
    consumer = StringPPMConsumer()
    ppm.getImg(ConsolePPMConsumer(consumer))
    img = consumer.getContent()
    
    
    # THEN we expect the following valid ppm file
    assert img == """P3 1 1 255
0 0 0
"""

def test_generate_a_2_by_2_default_pixel_file() :
    # GIVEN a 2 by 2 ppm file
    ppm = PPM(2, 2)
    
    # WHEN we generate the Image
    consumer = StringPPMConsumer()
    ppm.getImg(consumer)
    img = consumer.getContent()
    
    
    # THEN we expect the following valid ppm file
    assert img == """P3 2 2 255
0 0 0
0 0 0
0 0 0
0 0 0
"""

def test_generate_a_2_by_2__pixel_file_with_black_and_white_pixels() :
    # GIVEN a 2 by 2 ppm file
    ppm = PPM(2, 2)
    
    # WHEN we set some pixels to white
    ppm.setPixel(2, 1, 255, 255, 255)
    ppm.setPixel(1, 2, 255, 255, 255)
    
    # AND generate the Image
    consumer = StringPPMConsumer()
    ppm.getImg(consumer)
    img = consumer.getContent()
    
    
    # THEN we expect the following valid ppm file
    assert img == """P3 2 2 255
0 0 0
255 255 255
255 255 255
0 0 0
"""

def test_try_to_set_pixel_out_of_range_above() :
    # GIVEN a 2 by 2 ppm file
    ppm = PPM(2, 2)
    
    # WHEN we set some pixels to white    
    with pytest.raises(IndexError) as exception_info:
        ppm.setPixel(43, 30, 255, 255, 255)

    # THEN we expect the following valid ppm file
    assert str(exception_info.value) == "Pixel (43, 30) not in range (1-2, 1-2)"

def test_try_to_set_pixel_out_of_range_negative() :
    # GIVEN a 2 by 2 ppm file
    ppm = PPM(2, 2)
    
    # WHEN we set some pixels to white    
    with pytest.raises(IndexError) as exception_info:
        ppm.setPixel(0, 0, 255, 255, 255)

    # THEN we expect the following valid ppm file
    assert str(exception_info.value) == "Pixel (0, 0) not in range (1-2, 1-2)"