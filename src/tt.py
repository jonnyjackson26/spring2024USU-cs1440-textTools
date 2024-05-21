#!/usr/bin/env python

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

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage


# Print statement debugging: display command line arguments
# This block of code may be removed before you submit your project
# You can keep this so long as the output goes to sys.stderr
#for i, arg in enumerate(sys.argv):
#    num = f"arg #{i})"
#    print(f"{num:<8} {arg}", file=sys.stderr)
#print(file=sys.stderr)


if len(sys.argv) < 2:
    usage("Too few arguments")
    sys.exit(1)
else:
    if sys.argv[1]=="cat":
        cat(sys.argv[2:])
    elif sys.argv[1]=="tac":
        tac(sys.argv[2:])
    elif sys.argv[1]=="head":
        head(sys.argv[2:])
    elif sys.argv[1]=="tail":
        tail(sys.argv[2:])
    elif sys.argv[1]=="grep":
        grep(sys.argv[2:])
    elif sys.argv[1]=="wc":
        wc(sys.argv[2:])
    elif sys.argv[1]=="cut":
        cut(sys.argv[2:])
    elif sys.argv[1]=="paste":
        paste(sys.argv[2:])
    elif sys.argv[1]=="sort":
        sort(sys.argv[2:])
    else:
        usage(f"{sys.argv[1]} is not a valid program.")
        sys.exit(1)
