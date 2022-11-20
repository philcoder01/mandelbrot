from src import CliParser
import pytest

def test_it_should_return_defaults() :
    #GIVEN no additional arguments
    argv = ["curentPath"]

    #WHEN the arguments get parsed
    args = CliParser.parseArguments(argv);

    # THEN we expect the default arguments
    assert args.height == CliParser.DEFAULT_HEIGHT
    assert args.width == CliParser.DEFAULT_WITH


def test_it_should_parse_height() :
    #GIVEN just the height parameter
    argv = ["curentPath", "-h", "400"]

    #WHEN the arguments get parsed
    args = CliParser.parseArguments(argv)

    # THEN we expect the correct heigth
    assert args.height == 400


def test_throw_exception_if_unknown_parameter() :
    #GIVEN an unknown parameter
    argv1 = ["curentPath", "-x"]

    #WHEN the arguments get parsed
    with pytest.raises(Exception) as exception_info:
        CliParser.parseArguments(argv1)

    # THEN an exception should have been thrown
    assert str(exception_info.value) == 'unknown parameter "-x"'

