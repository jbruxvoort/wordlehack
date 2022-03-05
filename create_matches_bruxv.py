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

words = open('words_alpha.txt')
word_list = words.readlines()
#json_words = {}
total_words = 0
for count in range(len(word_list)):
#    count = count +1
    if  any(i in 'l' for i in word_list[count]):
#        total_words = total_words + 1
        word = word_list[count]
        for count2 in range(len(word_list[count])):
                if  all(j in word[count2] for j in 'clmnouy'):
                    print(word_list[count])

#    print(word_list)
#    json_words[word_list[count].rstrip()] = '2'

print(total_words)
#print(json.dumps(json_words, indent=4))
