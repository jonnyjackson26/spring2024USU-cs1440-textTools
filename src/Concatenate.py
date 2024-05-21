#            Copyright © 2024 DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it is not allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macramé, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).


import sys
from Usage import usage

def cat(args):
    """concatenate files and print on the standard output"""
    if(len(args)==0):
         usage("Please enter at least one valid filename","cat")
         return
    for filename in args:
        f = open(filename)
        for line in f:
            print(line, end="")
        f.close()




def tac(args):
    """concatenate and print files in reverse"""
    """
    if no args were passed
        print error saying you need some
    for each file:
            for line in reversed(f.readlines()):
                    print(line)
    """
    if len(args)==0:
        usage("Please enter at least one valid filename","tac")
        return
    for filename in args:
        f=open(filename)
        for line in reversed(f.readlines()):
                    print(line,end='')
        f.close()

