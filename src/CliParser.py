DEFAULT_HEIGHT = 600
DEFAULT_WIDTH =  800
DEFAULT_X_START = -2.0
DEFAULT_X_END = 1.0
DEFAULT_Y_START = -1.0
DEFAULT_Y_END = 1.0
DEFAULT_MAX_ITER = 100
DEFAULT_INFINITY_LIMIT = 4

class Arguments:
    width: int
    height: int
    x_start: float
    x_end: float
    y_start: float
    y_end: float
    max_iter: int
    infinity_limit: int

def parseArguments(argv : list[str]) :
    args = Arguments()

    args.width = DEFAULT_WIDTH
    args.height = DEFAULT_HEIGHT
    args.x_start = DEFAULT_X_START
    args.x_end = DEFAULT_X_END
    args.y_start = DEFAULT_Y_START
    args.y_end = DEFAULT_Y_END
    args.max_iter = DEFAULT_MAX_ITER
    args.infinity_limit = DEFAULT_INFINITY_LIMIT

    i = 1
    while (i < len(argv)):
        if (argv[i] == '-h'):
            args.height = int(argv[i + 1])
        elif (argv[i] == '-w'):
            args.width = int(argv[i + 1])
        elif (argv[i] == '-x_start'):
            args.x_start = float(argv[i + 1])
        elif (argv[i] == '-x_end'):
            args.x_end = float(argv[i + 1])
        elif (argv[i] == '-y_start'):
            args.y_start = float(argv[i + 1])
        elif (argv[i] == '-y_end'):
            args.y_end = float(argv[i + 1])
        elif (argv[i] == '-max_iter'):
            args.max_iter = int(argv[i + 1])
        elif (argv[i] == '-infinity_limit'):
            args.infinity_limit = int(argv[i + 1])
        else :
            raise Exception('unknown parameter "{}"'.format(argv[i]))
        i += 2

    return args