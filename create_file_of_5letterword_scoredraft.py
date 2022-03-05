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

words = open('draft12')
word_list = words.readlines()
outputfile = 'topscorewordle'
# lastletter = test[0]
column = 0
csv = open(outputfile + '.csv', 'w')
csv.write(outputfile +'\n')
wordnum = 0
letternum = 0
imperfectscore = 4
exactbonusscore = 1
strlocation = 0

word ="aaaaa"
points = 0
#testrange = 10
testrange = len(word_list)

# cycle through each word in the dictionary
# for count in range(len(word_list)):
for count in range(testrange):
    word = word_list[count].strip()
    print('\n')
    print(word)

    csv.write('\n')
    csv.write(word)
#reset points for each word
    points = 0
# check current word against each other word in the dictionary
#    for count2 in range(len(word_list)):
    for count2 in range(testrange):
        word2 = word_list[count2].strip()
# check each letter in "word" for its presence in "word2"
        for count3 in range(5):
            strlocation = word2.find(word[count3])
            if strlocation == count3:
                points = points + imperfectscore + exactbonusscore
                word2 = word2[:count3] + str(imperfectscore + exactbonusscore) + word2[count3 + 1:]
            elif (strlocation != -1):
                    points = points + imperfectscore
                    word2 = word2[:strlocation] + str(imperfectscore) + word2[strlocation + 1:]
#            print(str(count3)," ", word[count3]," ",str(strlocation), ' ', str(points))
#        csv.write("," + word2)
#        csv.write(" " + str(points))
        print(word," ",word2," ",str(points), " ")
    csv.write("," + str(points))
csv.write('\n')
csv.close()
