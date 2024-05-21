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


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !! YOU DO NOT NEED TO EDIT THIS FILE TO COMPLETE THE ASSIGNMENT !!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


CAT = """tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse"""

CUT = """tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default LIST=1)"""

PASTE = """tt.py paste FILENAME...
    Merge lines of files into one comma-separated text"""

GREP = """tt.py grep [-v] PATTERN FILENAME...
    Print lines of files matching PATTERN
    -v  Invert matching; print lines which DO NOT match PATTERN"""

HEAD = """tt.py head|tail [-n N] FILENAME...
    Output the first or last part of files
    -n  Number of lines to print (default N=10)"""

SORT = """tt.py sort FILENAME...
    Output lines of text file in sorted order"""

WC = """tt.py wc FILENAME...
    Print newline, word, and byte counts for each file"""


def usage(error=None, tool=None):
    """Provide a unified error reporting interface"""
    # Print a specific error message, if requested
    if error is not None:
        print(f"Error: {error}\n")

    # Print a tool-specific message where possible; otherwise, display
    # instructions for all tools
    if tool == 'cat' or tool == 'tac':
        print(f"{CAT}")
    elif tool == 'cut':
        print(f"{CUT}")
    elif tool == 'paste':
        print(f"{PASTE}")
    elif tool == 'grep':
        print(f"{GREP}")
    elif tool == 'head' or tool == 'tail':
        print(f"{HEAD}")
    elif tool == 'sort':
        print(f"{SORT}")
    elif tool == 'wc':
        print(f"{WC}")
    else:
        print("Python Text Tools Usage:\n========================",
              CAT, CUT, PASTE, GREP, HEAD, SORT, WC,
              sep="\n\n", end="\n\n")
