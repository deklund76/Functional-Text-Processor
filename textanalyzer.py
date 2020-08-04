from functools import reduce
from operator import add
import os, sys, re


# Regular expressions cheat sheet:
# '[^a-zA-Z]'= all non-alphabetic characters
# '[^0-9]' = all non-numeric characters
# '[a-zA-Z0-9\n]'= alpha-numeric and newline characters
# '[^a-zA-Z0-9]' = all non-alphanumeric characters


def main(argv):
    report = open("report.txt", "w")
    report.write("File name: " + os.path.abspath(argv) + "\n"
                 + "Number of lines: " + str(get_num_lines(argv))
                 + "\nNumber of characters (total): "
                 + str(get_num_chars(argv)) 
                 + "\nNumber of letters: " + str(get_num_letters(argv))
                 + "\nNumber of figures: " + str(get_num_figures(argv))
                 + "\nNumber of other characters: " 
                 + str(get_num_others(argv)) 
                 + "\nNumber of words: " + str(get_num_words(argv))
                 + "\n" + n_letter_words(argv))
    report.close()


def get_num_lines(inputfile):
    infile = open(inputfile)
    count = map(count_lines, infile)
    total = reduce(add, count)
    return total


def get_num_chars(inputfile):
    infile = open(inputfile)
    count = map(count_chars, infile)
    total = reduce(add, count)
    return total
    

def get_num_letters(inputfile):
    infile = open(inputfile)
    count = map(count_letters, infile)
    total = reduce(add, count)
    return total


def get_num_figures(inputfile):
    infile = open(inputfile)
    count = map(count_figures, infile)
    total = reduce(add, count)
    return total
    

def get_num_others(inputfile):
    infile = open(inputfile)
    count = map(count_others, infile)
    total = reduce(add, count)
    return total
    

def get_num_words(inputfile):
    return len(get_words(inputfile))


def n_letter_words(inputfile):
    words = get_words(inputfile)
    lengths = list(map(measure_words, words))
    length_occurrences = [count_lengths(x, lengths) for x in lengths]
    unsorted_numlengths = dict(zip(lengths, length_occurrences))
    numlengths = sorted(list(unsorted_numlengths.items()))
    report_lines = list(map(write_report_line, numlengths))
    result = "\n".join(report_lines)
    return result


def count_lines(line):
    return 1

def count_chars(line):
    return len(line.rstrip('\n'))

def count_letters(line):
    letters = re.sub(r'[^a-zA-Z]', "", line)
    return len(letters)

def count_figures(line):
    figures = re.sub('[^0-9]', "", line)
    return len(figures)

def count_others(line):
    other = re.sub(r'[a-zA-Z0-9\n]', "", line)
    return len(other)

def get_words(inputfile):
    infile = open(inputfile)
    lines_of_words = map(get_lines_of_words, infile)
    words_plus_empty_entries = list(reduce(add, lines_of_words))
    words = list(filter(None, words_plus_empty_entries))
    return words

def measure_words(word):
    return len(str(word))

def count_lengths(length, lengths):
    return lengths.count(length)

def write_report_line(numlength):
    report_line = ("Number of " + str(numlength[0])
                 + " letter words: " + str(numlength[1]))
    return report_line

def get_lines_of_words(line):
    words_plus_junk = re.split('[^a-zA-Z0-9]', line)
    lines_of_words = list(map(get_alphanum, words_plus_junk))
    return lines_of_words

def get_alphanum(string):
    return re.sub('[^a-zA-Z0-9]', "", string)


if __name__ == "__main__":
    main(sys.argv[1])