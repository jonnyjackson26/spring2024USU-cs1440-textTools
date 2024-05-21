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

def grep(args):
    """print lines that match patterns"""
    if not len(args)>0:
        usage("Please enter a pattern and a valid filename.",tool="grep")
        return
    multipleFilesPassed=False
    inverseSelection=False
    if args[0]=="-v":
        inverseSelection=True
        if len(args)>1:
            substr=args[1]
            if len(args)==2:
                usage("Enter a pattern and valid filename.",tool='grep')
                return
            filenames=args[2:]
            if len(args)>3:
                multipleFilesPassed=True
                
        else:
            usage("make sure you provide a substring to be searched for.",tool='grep')
            return
    else:
        substr=args[0]
        if not len(args)>1:
            usage("please provide a filename.","grep")
            return
        if len(args)>2:
            multipleFilesPassed=True
        filenames=args[1:]

    
    for filename in filenames:
        f=open(filename)
        for line in f:
            if not inverseSelection:
                if substr in line:
                    if multipleFilesPassed:
                        print(f'{filename}:{line}',end='')
                    else:
                        print(line,end='')
            else:
                if not substr in line:
                    if multipleFilesPassed:
                        print(f'{filename}:{line}',end='')
                    else:
                        print(line,end='')
        f.close()

