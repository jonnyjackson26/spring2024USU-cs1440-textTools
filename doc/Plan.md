# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
*   [ ] Explain what form the program's output will take.

## Cat Tool
**Rewrite instructions in my own words**
The cat tool takes a list of filenames. It joins them together into a longer file.
The data is printed to STDOUT by default. 
With just one filename, cat quickly prints the files context

**What I know how to do already**
 - Print to stdout
 - Do things repeatdly (for and while)

**What I dont know to do**
 - take a variable amount of arguments from command line
 - open and read files

**Input this program recieves**
 - command line arguments
 - data from files that are opened

**What the output looks like**
 - I'll know this program works if the output looks like all the text from all the files printed out together.

## Head
** Rewrite instructions in my own words **
The head tool prints the first 10 lines of a file (given as arguments). If the file has less than 10 lines, it just prints all of them. 
The head function can also take a paramater of how many lines to be printed with -n.
It can take multiple filenames and it'll do the same but with a little divider like ==> FILENAME <== between each file.

**What I know how to do already**
 - I know how to print to screen
 - open files
 - take multiple arguments
**What I dont know to do**
 - find the -n variable and throw the errors if its not correct and turn it into an int if it is.
**Input this program recieves**
 - 1 or more filenames
 - number of lines to be printed (-n)
**What the output looks like**
 - I'll know it works if it prints the first n lines of all listed files. The default for n is 10. If there's multiple files, it should differenciate between them. It should throw errors for files not found and invalid integer values.


## Tail
** Rewrite instructions in my own words **
 - This function is just like the head, just in reverse. It prints the last n lines of 1 or more files (n defaults to 10)

**What I know how to do already**
 - open files, use args
 - print to screen
 
**What I dont know to do**
 - for this assn, nothing (thankfully its very similar to the head function

**Input this program recieves**
 - an optional -n with an integer value after, and 1 or more filenames

**What the output looks like**
 - the last n lines of the listed filenames. If theres many files, they're seperated by ==> filename <==


## wc
** Rewrite instructions in my own words **
 - the wc function prints the number of lines, words (seperated by " "), and characters in a file. It can also take in multiple files and print the same, along with the total

**What I know how to do already**
 - Im familiar with .split(" ") which is a python function that can split a string. 
 - also len() returns number of characters
 - len(f.readlines) returns number of lines in the file 'f', i think.

**What I dont know to do**
 - it will be tricky to print to the screen the output spaced correctly.

**Input this program recieves**
 - one or more files

**What the output looks like**
 - basically like a table. first col is num of lines, second num of words, and third is num of characters in a file
 - each row is for each file passed in as arg.
 - a 'total' row is also added with more than one arguments


## Grep
** Rewrite instructions in my own words **
 - this function basically just finds substrings within the files that are passed as args. 
 - It can also take -v as a param which shows the lines that DONT have the substring. 
 - If you pass in many files, it'll print the results by saying filename:line

**What I know how to do already**
 - I already know how to print, find a substring in a line, and parse files
 - handle erros
 - take in args

**What I dont know to do**
 - I think i'm good here. The only possible problem I can see is maybe that itll be hard to write enough if statements or try catch blocks to see all the possible ways the user could crash the program

**Input this program recieves**
 - the optional -v paramater
 - a string
 - 1 or more filenames

**What the output looks like**
 - if there is many files, itll show all the lines in which the string is mentioned. filename:line's content
 - if theres a bad filename itll throw the normal python error
 - i'll write custom error messages for bad params

## Sort
** Rewrite instructions in my own words **
 - sorts lines of text in 1 or more files lexicographically

**What I know how to do already**
 - use pythons sort method
 - read lines of text from files
 - print to screen
**What I dont know to do**
 - i know everything, but it'll be interesting to see how i combine all the lines of all the files into one list

**Input this program recieves**
 - one or more filenames

**What the output looks like**
 - just individual lines from the files, printed in lexicographic order

## tac
** Rewrite instructions in my own words **
 - this is like cat, but the lines of each file are printed in reverse order.

**What I know how to do already**
 - I know how to reverse lines in python with reverse()
 - also, to read files
 - to print to screen
 
**What I dont know to do**
 - nothing. I worked out of order slighly and did tail before this so it should be easy.

**Input this program recieves**
 - one or more filenames

**What the output looks like**
 - each line of each file printed on its own line. the order of each line in the file is reversed but the order of the files is the same.

## Paste
** Rewrite instructions in my own words **
 - the paste function takes in one or more filenames and outputs each line from the files seperated by commas. 
 - the first outputted line will have fileA's Line 1's content , fileB's Line 1's content, fileC's Line1 content.
 - then the second outputted line will have fileA's Line2's content, fileB's line 2's content, file C's line 2 content. and so on.
 - if the file is too short, just put "" as that file's line content
 - the output will always be as many lines as the file with the most lines that was passed as an argument.

**What I know how to do already**
 - read files
 - parse lines
 - concatenate one string to another
 - print to screen

**What I dont know to do**
 - read multiple files at once

**Input this program recieves**
 - one or more filenames

**What the output looks like**
 - with just one file, like cat
 - with many files, like a .csv file

## Cut
** Rewrite instructions in my own words **
 - this function splits up csv files and prints an optional amount of columns. By defualt it just prints the first one. It can also take multiple files

**What I know how to do already**
 - check for options
 - use 2d lists
 - print to screen
 
**What I dont know to do**
 - it'll be tricky to parse the strings by commas 

**Input this program recieves**
 - an optional list of column indexes ( -f a,b,c ... )
 - 1 or more files

**What the output looks like**
 - if there were only one column index, it'd look like 'cat'
 - if there were many, like another (smaller) csv
 - it may alert for errors if bad/not enough filenames are given, or if -f is presented without numbers




Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    *   Describe important functions and classes in your program.  Include such details as:
        *   Names of functions/classes
        *   Parameter names and their types
        *   Types of data returned by functions
*   [ ] Explain what happens in the face of good and bad input.
    *   As you think of specific examples, write them under **Phase 3** so you can run them as soon as the program is functional.

## Cat Pseudocode

```
collect the filenames from the list of command line args
for each file in the argument list
	open the file
	for each lien of text in the file
		print the line to STDOUT
```

**With good input this program will:**
 - Copy lines of data from the input file to STDOUT
 - be an accureate reproduction of file's contents

**With bad output:**
 - a bad filename will cause the program to crash, leaving the stack trace.


## Head pseudocode
```
get n
verify that its positive and convert it to an integer.
if its not, throw an exception.
collect filenames from list of command line args
for each file in the list
	if the list of filenames is bigger than 1
		print the name of the file
	open the file
        for i in range 0 to n:
                if file has an nth line
			print the line
```
**With good input this program will:**
 - print 10 or any other number of lines of all the listed files to stdout. if there is many files they will be sepereated with ==> <==

**With bad output:**
 - a bad filename will cause the program to crash, leaving the stack trace.
 - error messages will be printed to stderr for having -n without anything after it or having -n without a valid integer after it.


## Tail psuedocode
```
print errors if -n is alone
print errors if -n is not followed by a valid int
collect filenames from list of command line args
for each file in the list:
        if the list of filenames is bigger than 1
                print the name of the file
        open the file
        for i in range n to 0:
                if file has an nth line
                        print the line
```
**With good input this program will:**
 - print the last 10 or any other number of lines of all the listed files to stdout. if there is many files, the names will be seperated with ==> <==

**With bad output:**
 - a bad filename will cause the program to crash, leaving the stack trace.
 - error messages will be printed to stderr for having -n without anything after it or not having an int after -n


## wc
```
totalLines=0
totalWords=0
totalChars=0
for file in args
	words= split file by " "
	lines= len(file.readlines())
	chars= length of the string of file
	print lines	words	chars	filename
	totalLines+=lines
	totalWords+=words
	totalChars+=chars
if args>1
	print totalLines	totalWords	totalChars	'total'

```
**With good input this program will:**
 - print num of lines, words, and chars in the given files.
 - also a total row, if there is many files given

**With bad output:**
 - throws the standard python error if a bad file name is passed through


## grep
```
boolean if -v was passed
boolean that says if more than one file was passed
for filename in args
	open file as f
	for line in f
		if -v was not passed: 
			if substring in line:
				if moreThanOneFileWasPassed:
					print filename:line
				else
					print line
		else:
			if substring not in line:
				if more thanone file was passed:
					print filename:line
				else
					print line
```
**With good input this program will:**
 - print the lines that contain the given substring of all the files passed thru as params. if there are many files, it'll show the name of the file together with the line

**With bad output:**
 - it'll give the default python error if theres a bad file name
 - itll tell you if a substring or a filename wasnt given



## Sort
```
check if there was 1 or more filename given
if not, raise error
allLines=[]
for each filename:
	append filename.readlines to allLines
sort allLines
print each line out in a for loop
```
**With good input this program will:**
 - print out in order all the lines of all the files passed through

**With bad output:**
 - error thrown for files that dont exist. python will do these errors itself. I wont check for any.
 - if there is no args passed through, it will ask for some.

## tac
```
if no args were passed
	print error saying you need some
for each file:
	for line in reversed(f.readlines()):
		print(line)
```
**With good input this program will:**
 - print the lines of each file in reverse order

**With bad input:**
 - error message if there is no filenames
 - it'll print the default python file not found error if it cant open a file




## Paste psuedocode
```
if len of args is 0
	stdout print "error, give me filenames"
	return
data = [[]] #2d array
for each file
	linesInFile=[]
	for each line in file:
		append line to linesInFile
	append linesInFile to data

//at this point we have the 2d data variable that's length is equal to number of files given and each index is a list of the lines in a file

for i in range(len(biggestIndex))
	line=''
	for j in range(len(data)):
		if i is less than data[j] length:
			line=line+data[j][i]
		if j is less than len(data)
			add comma
	print line


```
**With good input this program will:**
 - print a file that looks like a csv

**With bad input:**
 - with no filenames passed, it'll show an error and ask for some.
 - with a bad filename passed, it'll show the default python file not found error


## Cut psuedocode
```
if args < 0:
	ask for filenames
	return
indexes=[]
if args[o] is -f
	if args[1] is either an int or a list of ints seperated by commas:
		put them into indexes list (converted to ints)
	else:
		print error message, return
else:
	indexes is just the default first column

lines=[]
for file in args:
	f=open(file)
	lines.append(f.readlines)
	f.close()

 comment: at this point I have the lines list that each element is a list of lines of the files passed thru as args

for each line in lines
	split by comma. print indexes of that.


```
**With good input this program will:**
 - print a csv looking file, or as if it were cat in the case that only one -f is given
**With bad input:**
 - basic python error thrown if theres bad filenames
 - ill alert if theres 0 file names
 - throw error if -f is presented without an integer or list of integers seperated by commas directly after




Phase 2: Implementation
------------------------------------------------
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] Working code in the `src/` folder.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. what you learned, what didn't go according to plan.

## cat
 - this code worked great! It was very straightforward and I also basically copied it from Erik on gitlab.

## head
 - i learned that it was more complex than i thought to check for n. I had to do many if and elses to know exactly what the users input was.

## tail
 - i learned about the reversed() function in python that reverses a list
 - also about the .readlines() function that gets a list of the lines in a file
 - this made my code process be a lot more efficent.

# wc
 - i learned about .read() function for a file. This helped a lot on the logic side of my program.

## sort
 - this was incredibly quick to write. Once i had my psuedocode it was a breeze. 
 - I did expect allLines.append(f.readlines()) to work inside the "for each file" loop, but it didnt. I went instead with a nested for loop that appends each line of each file to allLines individually, and that worked.

## tac
 - everything was accoring to my psuedocode. 
 - i did forget though to close my file and return after the error message in my pseudocode.

## Paste
 - I did not consider that id have to get rid of \n at the end of each line
 - I also found that it was quicker to do .readlines() than going through each line of each file in a nested for loop
 - It took some fidling to get the comma to only show up between elements and not at the end


## Cut
 - This was easier after having done paste, a lot of logic was similar (for ex, getting rid of \n at the end of lines
 - I had troubles checking if the indexes that the user put in after -f were valid or not. I originally had many if statements but at the ended settled with a try-except block and converting everything split by "," into an int. If it worked, itll be an index. If not, it wont be an index.
 - It was tricky having to use a for loop in a for loop in a for loop but that is what I had to do in order for my program to work. Having the option of multiple indexes and also multiple files and obviously each file having multiple lines made this 3-times nested for loop neccesary. 



Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
    *   Include a description of what happened for *each test case*.
    *   For any bugs discovered, describe their cause and remedy.

## Cat
 - Case: python src/tt.py cat    (without args): This originally just didnt display anything, But i fixed it so that it would call usage() with the message to put valid filenames as args
 - case python src/tt.py cat <invalidfilename>: This shows the default python open file error, as expected. 
 - case: python src/tt.py cat <validfilename>: prints the lines, as expected.
 - case: python src/tt.py cat <validfilename> <validfilename> ... : prints all lines of all files, as expected

##  wc
 - Case: python src/tt.py wc  (without args): originally just returned nothing, I fixed it though to make it ask for filenames with usage().
 - Case: python src/tt.py wc  <validfilename>: as expected, prints out the line, word, and character count of the file.
 - Case: python src/tt.py wc  <valid filename> <valid filename> ... : as expected, prints out the line, word, and character count of all lines and also a combined total.
 - Case: python src/tt.py wc <invalid filename> : throws the default python file not found error, as expected.

## grep
 - Case: python src/tt.py grep (without args): originally returned nothing, but now it asks for a pattern and filename
 - Case: python src/tt.py grep -v : asks for pattern and filename with usage()
 - case: python src/tt.py grep -v <pattern> : asks for filename with usage()
 - case: python src/tt.py grep -v <filename> : asks for pattern with usage()
 - case: python src/tt.py grep -v <pattern> <filename> : as expected. prints lines from filename without instances of pattern.
 - case: python src/tt.py grep -v <pattern> <filename> <filename> : as expected, prints lines from all the files without instance of pattern. 
 - case: python src/tt.py grep -v <pattern> <invalid filename> : throws python default file not found error. 
 - case: python src/tt.py grep <pattern>: asks for pattern and filename with usage()
 - case: python src/tt.py grep <pattern> <filename> : as expected, prints instances of pattern in filename


## head
 - Case: python src/tt.py head (without args): originally would not print anything, but I fixed it to ask for a filename with usage()
 - Case: python src/tt.py head -n : Asks for a valid integer and filename with usage(), as expected
 - Case: python src/tt.py head -n <not an integer>: Asks for valid integer after -n, as expected.
 - Case: python src/tt.py head -n <an integer>: Asks for a filename, as expected. This didn't happen originally but I added it while testing and debugging.
 - Case: python src/tt.py head -n <an integer> <valid filename>: as expected, prints the first x lines of the file
 - Case: python src/tt.py head -n <an integer> <valid filename> <valid filename> ... : as expected, prints the first x lines of the files 
 - Case: python src/tt.py head -n <an integer> <invalid filename>: throws the default python file not found error, as expected
 - Case: python src/tt.py head <invalid filename>: throws python's default file not found error, as expected.
 - Case: python src/tt.py head <valid filename>: prints the first 10 lines of the file, as expected
 - Case: python src/tt.py head <valid filename> <valid filename> ... : prints the first 10 lines of all the files, as expected


## tail
 - Case: python src/tt.py tail (without args): originally would not print anything, but I fixed it in testing.
 - Case: python src/tt.py tail -n : Asks for a valid integer and filename with usage(), as expected
 - Case: python src/tt.py tail -n <not an integer>: Asks for valid integer after -n, as expected
 - Case: python src/tt.py tail -n <an integer>: Asks for a filename, as expected. This didn't happen before I fixed it while running tests.
 - Case: python src/tt.py tail -n <an integer> <valid filename>: as expected, prints the first x lines of the file 
 - Case: python src/tt.py tail -n <an integer> <valid filename> <valid filename> ... : as expected, prints the last X lines of all the files passed through
 - Case: python src/tt.py tail -n <an integer> <invalid filename>: throws the default python file not found error
 - Case: python src/tt.py tail <invalid filename>: throws python's default file not found error as expected
 - Case: python src/tt.py tail <valid filename>: prints the last 10 lines of the file, as expected
 - Case: python src/tt.py tail <valid filename> <valid filename> ... : prints the last 10 lines of the files, as expected

## sort
 - Case: python src/tt.py sort  (without args): as expected, asks for filenames with usage()
 - Case: python src/tt.py sort  <validfilename>: as expected, sorts the lines of the file
 - Case: python src/tt.py sort  <valid filename> <valid filename> ... : as expected, sorts the lines of the files
 - Case: python src/tt.py sort <invalid filename> : as expected, throws the default python file not found error

## tac
 - Case: python src/tt.py tac   (without args): asks for a valid filename with usage()
 - case: python src/tt.py tac <invalidfilename>: This shows the default python open file error, >
 - case: python src/tt.py tac <validfilename>: prints the lines in reverse order, as expected.
 - case: python src/tt.py tac <validfilename> <validfilename> ... : prints all lines of all files in reverse, as expected

## cut
 - Case: python src/tt.py cut (without args): asks for a filename with usage():
 - Case: python src/tt.py cut <invalid filename> : default python file not found error
 - Case: python src/tt.py cut <valid filename> : as expected, prints out the first column of data from the filename. 
 - Case: python src/tt.py cut -f <integer x> <valid filename>: prints out the xth column of the filename
 - case: python src/tt.py cut -f <valid filename> : asks for valid integer with usage()
 - case: python src/tt.py cut -f : asks for integer and valid filename with usage()
 - case: python src/tt.py cut -f <integers a,b,c> <valid filename> : prints out the ath, bth, and cth column of valid filename
 - case: python src/tt.py cut -f <negative integer> <valid filename> : asks for positive integer with usage()
 - case: python src/tt.py cut -f <integer(s)> <valid filename> <valid filename> ... : as expected, prints out the integer(s) columns of each file.

## paste
 - case: python src/tt.py paste (without args): asks for a filename with usage()
 - case: python src/tt.py paste <valid filename> : as expected, behaves like cat
 - case: python src/tt.py paste <invalid filename> : throws python default error for file not found
 - case: python src/tt.py paste <valid filename> <valid filename> ... : as expected, pastes the files into csv. 

Phase 4: Deployment
-------------------
*(5% of your effort)*

Deliver:

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


Phase 5: Maintenance
--------------------

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
	* I think it's generally pretty decent. I think the usage.py module is a little tricky to read but thats mainly because of the spacing of the lines (because it's printed out to the terminal)
        *   Are there parts of your program which you aren't quite sure how/why they work?
		* To be honest, I understand all the lines of the code in this project. The line I understand least is in the word count file, when I find out the number of words with words=len(wholeText.replace("\n"," ").split(" "))-1 . This code works, the only problem with it is it's kind of long and uses some built in python functions
        *   If a bug is reported in a few months, how long would it take you to find the cause?
		* It would depend on what the bug is and how it's reported to me. I find it possible that in a few months some small bugs that take an hour might appear, but it is also possible a bug that I cant figure out could take me up to 6 hours to locate and solve.
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
		* Hopefully! I think some parts may be slightly tricky (for example: the pseudocode if the reader is not a programmer). I tried my best to describe the purpose and plan of each of these text tools, but it's very probable that others could find that difficult to read. Overall, I think if you study my documentation a little bit you'll be able to understand it.
        *   ...yourself in six month's time?
		* I have worked on projects and after some months, returned without knowing at all what my code did. This, however, is my first time writing documentation for my code, so hopefully I'll be able to understand everything after 6 months.
    *   How easy will it be to add a new feature to this program in a year?
		* I think very easy. The nature of the structure of this project makes it very scalable. Each text tool is divided into its own python file. All you'd need to do to add a new feature is add the python file with the working code, add an elif in the tt.py file for it, and maybe add an error message/info block of text into the Usage.py file.
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
		* It should, as long as python is installed this program should have no problems.
        *   ...the operating system?
		* It should. The only thing is maybe how the operating system counts lines in files / characters in lines of text files. But the code will continute to work regardless.
        *   ...to the next version of Python?
		* Yes, as long as python does not remove any features that I've put in my program.
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
