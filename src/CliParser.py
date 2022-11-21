DEFAULT_HEIGHT = 600
DEFAULT_WIDTH =  800

class Arguments:
    width: int
    height: int

def parseArguments(argv : list[str]) :
    args = Arguments()
    if (len(argv) == 1): 
        args.width = DEFAULT_WIDTH
        args.height = DEFAULT_HEIGHT
    else :
        i = 1
        while (i < len(argv)):
            if (argv[i] == '-h'):
                args.height = int(argv[i + 1])
            elif (argv[i] == '-w'):
                args.width = int(argv[i + 1])
            else :
                raise Exception('unknown parameter "{}"'.format(argv[i]))
            i += 2

    return args