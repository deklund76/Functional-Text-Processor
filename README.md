# For-Esker-Inc
A repository featuring application questions and a small program to be viewed by employees of Esker Inc.

The program is a fully-functional text processor that takes a text file as an entry level parameter 
and generates a report describing the content in the following format: 

File name: D:\temp\file.txt

Number of lines: 85

Number of characters (total): 1441

Number of letters: 782

Number of figures: 17

Number of other characters: 642

Number of words: 195

Number of 1 letter words: 56

Number of 2 letters words: 27

[...]

Number of 16 letters words: 2

Number of 19 letters words: 1

Usage: in your command line run "python textanalyzer.py inputfile" where the inputfile is of course the file to be read, invalid inputs will lead to a FileNotFoundError.

Details: Characters include all ASCII characters other than newline characters.
         Words are defined as any string of alpha-numeric characters seperated by other characters or spaces.
         I had no exposure to functional programming whatsoever before writing this program so it took me ~8 hours.
