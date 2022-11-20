import sys
import CliParser

sys.argv
args = CliParser.parseArguments(sys.argv)
print(args.width, args.height)