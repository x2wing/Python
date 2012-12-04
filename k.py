import stat, sys, os, string, commands


try:

    pattern = raw_input("Enter the file pattern to search for:\n")

    commandString = "find " + pattern
    commandOutput = commands.getoutput(commandString)
    findResults = string.split(commandOutput, "\n")
    for i in findResults:
    	print i

except:
    print "There was a problem - check the message above"