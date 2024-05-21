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

def wc(files):
    """print newline, word, and byte counts for each file"""

    if len(files)==0:
        usage("Please enter a valid filename.","wc")
        return
    
    totalLines=0
    totalWords=0
    totalChars=0
    for filename in files:
        f=open(filename)
        wholeText=f.read()
        lines=len(wholeText.split('\n'))-1
        words=len(wholeText.replace("\n"," ").split(" "))-1
        chars=len(wholeText)
        print(f'{lines} {words} {chars} {filename}')
        totalLines+=lines
        totalWords+=words
        totalChars+=chars
        f.close()
    if len(files)>1:
        print(f'{totalLines} {totalWords} {totalChars} total')
