DEFAULT_HEIGHT = 600
DEFAULT_WITH =  800

class Arguments:
    width: int
    height: int

def parseArguments(argv) :
    args = Arguments()
    args.width = 0
    args.height = 0
    return args