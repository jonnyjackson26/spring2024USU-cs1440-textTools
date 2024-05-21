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

def sort(args):
    """sort lines of text files"""
    """
    check if there was 1 or more filename given
    if not, raise error
    allLines=[]
    for each filename:
            append filename.readlines to allLines
    sort allLines
    print each line out in a for loop
    """
    if len(args)==0:
        usage(error='Please pass through 1 or more valid file name.',tool='sort')
        return
    allLines=[]
    for filename in args:
        f=open(filename)
        for line in f:
            allLines.append(line)
        f.close()
    allLines.sort()
    for line in allLines:
        print(line,end="")
