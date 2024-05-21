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

def head(args):
    """output the first part of files"""
    if len(args)==0:
        usage("Please enter a valid filename.","head")
        return

    if args[0]=="-n":
        if len(args)>2 :
            try:
                n=int(args[1])
                args=args[2:]
                if len(args)==0:
                    usage("Make sure you enter a valid filename","head")
                    return
            except:
                usage("Make sure that after -n you enter a valid integer","head")
                return
        else:
            usage("Please enter a valid integer and one or more filenames after -n.","head")
            return
    else:
        n=10


    for filename in args:
        if len(args)>1:
            print(f"==>{filename}<==")
        cntr=0
        f=open(filename)
        for line in f:
                if cntr<n:
                    print(line,end="")
                    cntr+=1
        f.close()
        print("") #to have a line break



def tail(args):
    """output the last part of files"""

    if len(args)==0:
        usage("Please enter a valid filename.","tail")
        return
    
    if args[0]=="-n":
        if len(args)>2 :
            try:
                n=int(args[1])
                args=args[2:]
                if len(args)==0:
                    usage("Make sure you enter a valid filename","tail")
                    return
            except:
                usage("Make sure that after -n you enter a valid integer","tail")
                return
        else:
            usage("Please enter a valid integer and one or more filenames after -n.","tail")
            return
    else:
        n=10


    for filename in args:
        if len(args)>1:
            print(f"==>{filename}<==")
        cntr=0
        f=open(filename)
        for line in reversed(f.readlines()):
                if cntr<n:
                    print(line,end="")
                    cntr+=1
        f.close()
        print("") #to have a line break
