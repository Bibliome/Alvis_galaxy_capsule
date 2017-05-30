#!/usr/bin/python2

# Filename: grep.py
# Author: Mouhamadou Ba
# Version: 20/07/2016

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
 	print "-input      text corpus"
	print "-dict       dictionary file"
	print "-output      output file"


    input_p = opts.get("-input")
    if input_p == None:
        print "No value specified"
        return -1

    dict_p = opts.get("-dict")
    if dict_p == None:
        print "No value specified"
        return -2

    output_p = opts.get("-output")
    if output_p == None:
        print "No value specified"
        return -3

    # generate alvisnlp commandOptions
    commandOptions =""
    if verbose == "true" :
	commandOptions = " -verbose "

    if colors == "true" :
	commandOptions = commandOptions + "-noColors "

    commandline = "alvisnlp -param input %s -param dict %s -param output %s plans/alvis-annotator.plan" % ( input_p , dict_p , output_p )

    # run alvisnlp
    print commandline

    # errorcode, stdout = commands.getstatusoutput(commandline)
    os.system(commandline)     
 
    # return error code
    #return errorcode


if __name__ == "__main__":
    main()

