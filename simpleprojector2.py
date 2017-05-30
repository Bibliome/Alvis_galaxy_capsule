



import sys
import os
import re
import string
import commands
from tempfile import NamedTemporaryFile


# This function is exceedingly useful, perhaps package for reuse?
def getopts(argv):
    opts = {}
    while argv:
	if argv[0][0] == '-':
	    opts[argv[0]] = argv[1]
	    argv = argv[2:]
	else:
	    argv = argv[1:]
    return opts



def main():
    args = sys.argv[1:]

    try:
        opts = getopts(args)
    except IndexError:
        print "Usage:"
 	print "-noColors       colors"
	print "-dictFile       dictionary file"
	print "-trieSink       output file"
	print "-targetLayerName             "
	print "-valueFeatures               "
	print "-keyIndex                    " 

    verbose = opts.get("-verbose")
    if verbose == None:
        print "No value specified"
        return -1

    colors = opts.get("-noColors")
    if colors == None:
        print "No value specified"
        return -2

    dictFile = opts.get("-dictFile")
    if dictFile == None:
        print "No value specified"
        return -3

    trieSink = opts.get("-trieSink")
    if trieSink == None:
        print "No value specified"
        return -4

    targetLayerName = opts.get("-targetLayerName")
    if targetLayerName == None:
        print "No value specified"
        return -5

    valueFeatures = opts.get("-valueFeatures")
    if valueFeatures == None:
        print "No value specified"
        return -6

    keyIndex = opts.get("-keyIndex")
    if keyIndex == None:
        print "No value specified"
        return -7

    # generate alvisnlp commandOptions
    commandOptions =""
    if verbose == "true" :
	commandOptions = " -verbose "

    if colors == "true" :
	commandOptions = commandOptions + "-noColors "

    commandline = "alvisnlp %s -param search dictFile %s -param search trieSink %s -param search targetLayerName %s -param search valueFeatures %s -param search keyIndex %s simpleprojector2.plan" % ( commandOptions , dictFile , trieSink , targetLayerName , valueFeatures , keyIndex )

    # run alvisnlp
    print commandline

    # errorcode, stdout = commands.getstatusoutput(commandline)
    os.system(commandline)     
 
    # return error code
    #return errorcode


if __name__ == "__main__":
    main()

