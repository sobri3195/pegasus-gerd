#!/usr/bin/python
# If you don't have Termcolor installed do this cmd => pip install termcolor
import os
import sys
logo = ""
logo +="                        _____       \n"
logo +="                  |___/             \n\n"
from termcolor import colored
print colored(logo,"red")
print colored("Created by Sobri the Pegasus / Indonesia ","yellow")
print ""
import optparse 
parser = optparse.OptionParser()
parser.add_option('--ip',dest="question",help="test ")
opt , args = parser.parse_args()

if opt.question :
   question = (opt.question)
elif not (opt.question) :
   print("--ip option is required ")
   sys.exit()
#end ip = option

os.system("python files/ipscan.py --ip=%s" % question)
