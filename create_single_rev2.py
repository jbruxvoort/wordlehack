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
column = 1
words = open('words_alpha.txt')
word_list = words.readlines()
test = 'mrtpnyo'
lastletter = test[0]
col = 0
f = open(test, 'w')
f.write(test + '\n')
#json_words = {}
total_words = 0
# cycle through each word in the dictionary
for count in range(len(word_list)):
    if  any(i in test[0] for i in word_list[count]):
        matches = 0
        word = word_list[count].strip()
        for count2 in range(len(word)):
            if  test.find(word[count2]) != -1: #check each letter in the word to see if it is found in the test set of letters
                matches = matches + 1
            if matches == len(word) and matches >=4: #if youreach the end of the word and there are more than 4 letters matching
                if word[0] != lastletter:
                    f.write('\n\n')
                    lastletter = word[0]
                    column = 1
                f.write(word)
                f.write(", ")
                if column % 5 == 0 and column != 0:
                    f.write('\n')
                column = column + 1
                total_words = total_words +1


f.write('\n')
f.write(str(total_words))
f.close()
print(total_words)
#    json_words[word_list[count].rstrip()] = '2'

#print(json.dumps(json_words, indent=4))
