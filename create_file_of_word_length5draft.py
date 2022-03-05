#!/usr/bin/env python3

# Made by Innovative Inventor at https://github.com/innovativeinventor.
# If you like this code, star it on GitHub!
# Contributions are always welcome.

# MIT License
# Copyright (c) 2017 InnovativeInventor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Usage: python3 scripts/create_json.py filename
# Example: python3 scripts/create_json.py words_alpha.txt

import sys
#import json

words = open('wlist_match12.txt')
word_list = words.readlines()
test = 'draft12'
# lastletter = test[0]
column = 0
f = open(test, 'w')
f.write(test + '\n')
#json_words = {}
csv = open(test + '.csv', 'w')
csv.write(test +'\n')
wordnum = 0
letternum = 0
w, h = 50,8;
matrix = [[' ' for x in range(w)] for y in range(h)]
total_words = 0
wordsperletter = 0
maxwordsperletter = 0
word ="aaaaa"
# cycle through each word in the dictionary
for count in range(len(word_list)):
    if  len(word_list[count].strip()) == 5  and word_list[count].strip() != word:
#        lastmatch = word_list[count].strip()
        total_words = total_words + 1
        word = word_list[count].strip()
        print(word)
        f.write(word)
        f.write('\n')

"""
        for count2 in range(len(word)):
            if  test.find(word[count2]) != -1: #check each letter in the word to see if it is found in the test set of letters
                matches = matches + 1
            if matches == len(word) and matches >=4: #if youreach the end of the word and there are more than 4 letters matching
                wordsperletter = wordsperletter + 1
                if word[0] != lastletter:  #new starting new column of words
                    letternum = letternum +1 #increment the column
                    wordcount = 0
                    if wordsperletter > maxwordsperletter:
                            maxwordsperletter = wordsperletter
                    wordsperletter = 0
                    print(word[0])
                    f.write('\n\n')
                    lastletter = word[0]
                    column = 1
                f.write(word)
                matrix[letternum][wordcount] = word
                print (matrix[letternum][wordcount])
                wordcount = wordcount + 1 #increment the row
                f.write(", ")
                if column % 5 == 0 and column != 0:
                    f.write('\n')
                column = column + 1
                total_words = total_words +1

"""
f.write('\n')
f.write(str(total_words))
f.close()
"""
startletter = 1
row = 0

while row < maxwordsperletter:
    outputline = ""
    while startletter <8:
        outputline = outputline  + matrix[startletter][row].ljust(9," ")
        startletter = startletter +1
    startletter = 1
    outputline = outputline + '\n'
    csv.write(outputline)
    row = row + 1
"""
csv.close()
print(total_words)
#    json_words[word_list[count].rstrip()] = '2'

#print(json.dumps(json_words, indent=4))
