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
    assert args.x_start == CliParser.DEFAULT_X_START
    assert args.x_end == CliParser.DEFAULT_X_END
    assert args.y_start == CliParser.DEFAULT_Y_START
    assert args.y_end == CliParser.DEFAULT_Y_END


def test_it_should_parse_height() :
    #GIVEN just the height parameter
    argv = ["currentPath", "-h", "400"]

    #WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)

    # THEN we expect the correct height
    assert args.height == 400


def test_throw_exception_if_unknown_parameter() :
    #GIVEN an unknown parameter
    argv1 = ["currentPath", "-u"]

    #WHEN the arguments get parsed
    with pytest.raises(Exception) as exception_info:
        CliParser.parseArguments(argv1)

    # THEN an exception should have been thrown
    print(exception_info.value)
    assert str(exception_info.value) == 'unknown parameter "-u"'


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

def test_if_x_start_value_can_be_input_correctly():
    #Given the x start Value parameter
    argv = ["currentPath", "-x_start", "-1.3"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the x_start is correct
    assert args.x_start == -1.3
    assert args.x_end == CliParser.DEFAULT_X_END
    assert args.y_start == CliParser.DEFAULT_Y_START
    assert args.y_end == CliParser.DEFAULT_Y_END

def test_if_x_end_value_can_be_input_correctly():
    #Given the x end Value parameter
    argv = ["currentPath", "-x_end", "0.7"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the x_end is correct
    assert args.x_start == CliParser.DEFAULT_X_START
    assert args.x_end == 0.7
    assert args.y_start == CliParser.DEFAULT_Y_START
    assert args.y_end == CliParser.DEFAULT_Y_END

def test_if_y_start_value_can_be_input_correctly():
    #Given the y start Value parameter
    argv = ["currentPath", "-y_start", "-1.3"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the y_start is correct
    assert args.x_start == CliParser.DEFAULT_X_START
    assert args.x_end == CliParser.DEFAULT_X_END
    assert args.y_start == -1.3
    assert args.y_end == CliParser.DEFAULT_Y_END

def test_if_y_end_value_can_be_input_correctly():
    #Given the y end Value parameter
    argv = ["currentPath", "-y_end", "1.3"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the y_end is correct
    assert args.x_start == CliParser.DEFAULT_X_START
    assert args.x_end == CliParser.DEFAULT_X_END
    assert args.y_start == CliParser.DEFAULT_Y_START
    assert args.y_end == 1.3
    
def test_if_max_iterations_can_be_input_correctly():
    #Given the max Iterations parameter
    argv = ["currentPath", "-max_iter", "50"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the max iterations is correct
    assert args.max_iter == 50
    assert args.infinity_limit == CliParser.DEFAULT_INFINITY_LIMIT

def test_if_infinity_limit_can_be_input_correctly():
    #Given the infinity limit parameter
    argv = ["currentPath", "-infinity_limit", "2"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the infinity limit is correct
    assert args.max_iter == CliParser.DEFAULT_MAX_ITER
    assert args.infinity_limit == 2

def test_if_xy_start_xy_end_hight_and_infinity_limit_value_can_be_input_correctly():
    #Given the xy start, xy end, hight and infinity limit Value parameter
    argv = ["currentPath", "-x_start", "-1.3", "-x_end", "0.7", "-y_start", "-0.7", "-y_end", "1.3", "-h", "300", "-infinity_limit", "6"]

    #When the arguments get parsed
    args = CliParser.parseArguments(argv)

    # Then check that the xy start, xy end, hight and infinity limit value is correct
    assert args.height == 300
    assert args.width == CliParser.DEFAULT_WIDTH
    assert args.x_start == -1.3
    assert args.x_end == 0.7
    assert args.y_start == -0.7
    assert args.y_end == 1.3
    assert args.infinity_limit == 6
    assert args.max_iter == CliParser.DEFAULT_MAX_ITER


    
