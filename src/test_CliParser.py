import CliParser
import pytest

def test_it_should_return_defaults() :
    #GIVEN no additional arguments
    argv = ["currentPath"]

    #WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)

    # THEN we expect the default arguments
    assert args.height == CliParser.DEFAULT_HEIGHT
    assert args.width == CliParser.DEFAULT_WIDTH


def test_it_should_parse_height() :
    #GIVEN just the height parameter
    argv = ["currentPath", "-h", "400"]

    #WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)

    # THEN we expect the correct height
    assert args.height == 400


def test_throw_exception_if_unknown_parameter() :
    #GIVEN an unknown parameter
    argv1 = ["currentPath", "-x"]

    #WHEN the arguments get parsed
    with pytest.raises(Exception) as exception_info:
        CliParser.parseArguments(argv1)

    # THEN an exception should have been thrown
    print(exception_info.value)
    assert str(exception_info.value) == 'unknown parameter "-x"'


def test_if_the_width_is_input_correctly() :
    # GIVEN the width parameter
    argv = ["currentPath", "-w", "200"]
    
    # WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)
    
    # THEN that the width is correct
    assert args.width == 200


def test_if_width_and_height_can_be_input_correctly() :
    # GIVEN the width and height parameter
    argv = ["currentPath", "-w", "200", "-h", "400"]
    
    # WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)
    
    # THEN that the width is correct
    assert args.width == 200
    assert args.height == 400
    

def test_if_height_and_width_can_be_input_correctly() :
    # GIVEN the width and height parameter
    argv = ["currentPath", "-h", "200", "-w", "400"]
    
    # WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)
    
    # THEN that the width is correct
    assert args.height == 200
    assert args.width == 400