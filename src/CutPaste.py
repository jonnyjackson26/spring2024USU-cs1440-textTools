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

def paste(args):
    """merge lines of files"""
    if len(args)==0:
        usage("Please enter at least one filename","paste")
        return
    data=[]
    for file in args:
        f=open(file)
        data.append(f.readlines())
        f.close()
        

    #get rid of \n at the end of file
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=data[i][j].split("\n")[0]

    biggestIndex=0
    for i in range(len(data)):
        if len(data[i])>len(data[biggestIndex]):
            biggestIndex=i
    
    for i in range(len(data[biggestIndex])):
        thisLine = ''
        for j in range(len(data)):
            if i < len(data[j]):
                thisLine += data[j][i]
            if j < len(data) - 1:
                    thisLine += ","
        print(thisLine)

    



def cut(args):
    """remove sections from each line of files"""
    if len(args)==0:
        usage("Please enter at least one valid filename","cut")
        return
    
    indexes=[]
    startingIndexOfFilenames=0
    if args[0]=="-f":
        if len(args)>1:
            for thing in args[1].split(','):   
                try:
                    indexes.append(int(thing))
                    if indexes[-1]<0:
                        usage("ensure all your integers are positive","cut")
                        return
                except:
                    usage("After -f, only enter integers (or a list of them seperated by commas without spaces)","cut")
                    return
            startingIndexOfFilenames=2 
            if len(indexes)==0:
                usage("please enter an integer (or list of them, seperated by commas) after -f.","cut")
                return
        else:
            usage("Please give an integer or a list of integers split by commas after -f.","cut")
    else:
        indexes.append(1)

    indexes.sort()

    data=[]
    for filename in args[startingIndexOfFilenames:]:
        f=open(filename)
        data.append(f.readlines())
        f.close()

    #get rid of \n at the end of file
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=data[i][j].split("\n")[0]

    for i in range(len(data)):
        for j in range(len(data[i])):
            line=''
            for indexA in range(len(indexes)):
                if indexes[indexA]-1<len(data[i][j].split(',')):
                    line=line+str(data[i][j].split(',')[indexes[indexA]-1])
                else:
                    line+=""
                if indexA<len(indexes)-1:
                        line+=","
            print(line)
            